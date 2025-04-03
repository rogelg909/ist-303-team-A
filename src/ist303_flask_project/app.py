from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random
import copy
from xhtml2pdf import pisa
from io import BytesIO
from datetime import datetime
from flask import render_template_string

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role  # 👈 Add role attribute

# Database connection helper function
def get_db_connection():
    db_path = app.config.get('DATABASE', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'], user['role'])  # 👈 Include role
    return None

@app.route('/')
@login_required
def index():
    conn = get_db_connection()
    last_score = conn.execute(
        'SELECT score, category, taken_at FROM quiz_scores WHERE user_id = ? ORDER BY taken_at DESC LIMIT 1',
        (current_user.id,)).fetchone()

    leaderboard = conn.execute('''
        SELECT users.username, MAX(quiz_scores.score) AS high_score, quiz_scores.category, MAX(quiz_scores.taken_at) AS taken_at
        FROM quiz_scores
        JOIN users ON quiz_scores.user_id = users.id
        GROUP BY users.id
        ORDER BY high_score DESC, taken_at ASC
        LIMIT 10
    ''').fetchall()
    conn.close()

    leaderboard_data = [{'rank': i+1, 'username': row['username'], 'score': row['high_score'],
                         'category': row['category'], 'date': row['taken_at']} for i, row in enumerate(leaderboard)]

    if last_score is None:
        last_score = {"score": "No score yet", "category": "N/A", "taken_at": "Never"}

    return render_template('index.html', user=current_user, last_score=last_score, leaderboard=leaderboard_data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        teacher_code = request.form.get('teacher_code', '').strip()

        # ✅ Validate fields
        if not username or not password:
            flash('Username and password are required.', 'warning')
            return redirect(url_for('register'))

        # 🎓 Assign role
        TEACHER_SECRET_CODE = 'supersecret123'  # This can be moved to config in production
        role = 'teacher' if teacher_code == TEACHER_SECRET_CODE else 'student'

        # 🔐 Hash password
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        existing_user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            conn.close()
            return redirect(url_for('register'))

        # ✅ Insert user
        conn.execute(
            'INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
            (username, hashed_password, role)
        )
        conn.commit()
        conn.close()

        flash(f'Registration successful! You registered as a {role}. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            # Pass role to the User class
            login_user(User(user['id'], user['username'], user['role']))
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/start_quiz/<category>')
@login_required
def start_quiz(category):
    category = category.lower()
    if category not in ["easy", "medium", "hard"]:
        flash("Invalid quiz category!", "danger")
        return redirect(url_for('index'))

    conn = get_db_connection()
    used_question_ids = set(session.get('used_question_ids', []))

    all_questions = conn.execute('''
        SELECT id, question, option_a, option_b, option_c, option_d, correct_answer, explanation 
        FROM quiz_questions WHERE category = ?
    ''', (category,)).fetchall()
    conn.close()

    all_questions = [dict(q) for q in all_questions]
    unique_questions = [q for q in all_questions if q['id'] not in used_question_ids]

    if len(unique_questions) < 10:
        unique_questions = all_questions

    selected_questions = random.sample(unique_questions, min(10, len(unique_questions)))
    randomized_questions = []

    for q in selected_questions:
        options = [
            ('A', q['option_a']),
            ('B', q['option_b']),
            ('C', q['option_c']),
            ('D', q['option_d']),
        ]
        random.shuffle(options)

        new_q = copy.deepcopy(q)
        for idx, (label, text) in enumerate(options):
            new_q[f'option_{chr(97 + idx)}'] = text

        for idx, (label, text) in enumerate(options):
            if label == q['correct_answer']:
                new_q['correct_answer'] = chr(65 + idx)
                break

        randomized_questions.append(new_q)

    session['quiz'] = randomized_questions
    session['quiz_index'] = 0
    session['score'] = 0
    session['used_question_ids'] = list(used_question_ids.union({q["id"] for q in selected_questions}))

    return redirect(url_for('quiz_question', category=category))

@app.route('/quiz/question/<category>', methods=['GET', 'POST'])
@login_required
def quiz_question(category):
    if 'quiz' not in session or session['quiz_index'] >= len(session['quiz']):
        return redirect(url_for('quiz_result', category=category))

    question = session['quiz'][session['quiz_index']]

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().upper()
        correct_option = question['correct_answer'].strip().upper()

        is_correct = user_answer == correct_option
        option_mapping = {
            "A": question["option_a"],
            "B": question["option_b"],
            "C": question["option_c"],
            "D": question["option_d"],
        }

        session['last_question'] = {
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_option,
            "user_answer_text": option_mapping.get(user_answer, ""),
            "correct_answer_text": option_mapping.get(correct_option, ""),
            "is_correct": is_correct
        }

        if is_correct:
            session['score'] += 1

        session['quiz_index'] += 1

        return redirect(url_for('quiz_feedback', category=category))

    return render_template('quiz_question.html', question=question, category=category)

@app.route('/quiz/feedback/<category>')
@login_required
def quiz_feedback(category):
    if 'last_question' not in session:
        return redirect(url_for('quiz_question', category=category))

    last_question = session.pop('last_question')
    return render_template('quiz_feedback.html', question=last_question["question"],
                           user_answer=last_question["user_answer"],
                           is_correct=last_question["is_correct"], category=category)

@app.route('/quiz/result/<category>')
@login_required
def quiz_result(category):
    score = session.get('score', 0)

    conn = get_db_connection()
    conn.execute('INSERT INTO quiz_scores (user_id, score, category) VALUES (?, ?, ?)',
                 (current_user.id, score, category))
    conn.commit()
    conn.close()

    session.pop('quiz', None)
    session.pop('quiz_index', None)
    session.pop('score', None)

    return render_template('quiz_results.html', score=score, category=category)

@app.route('/quiz/share/<category>')
@login_required
def share_results(category):
    score = session.get('score', 0)
    return render_template('quiz_share.html', user=current_user, score=score, category=category)

# ----------------------------------------------
# 🔐 Admin Panel: Only accessible by teachers
# ----------------------------------------------
@app.route('/admin')
@login_required
def admin_panel():
    if current_user.role != 'teacher':
        flash("Access denied: Only teachers can access this page.", "danger")
        return redirect(url_for('index'))

    # ✅ Get filter inputs
    category = request.args.get('category', '').strip().lower()
    topic = request.args.get('topic', '').strip().lower()

    # ✅ Build query based on filters
    conn = get_db_connection()
    query = "SELECT * FROM quiz_questions WHERE 1=1"
    params = []

    if category:
        query += " AND LOWER(category) = ?"
        params.append(category)
    if topic:
        query += " AND LOWER(topic) LIKE ?"
        params.append(f"%{topic}%")

    questions = conn.execute(query, tuple(params)).fetchall()
    conn.close()

    return render_template("admin_panel.html", questions=questions,
                           filter_category=category, filter_topic=topic)

@app.route('/admin/generate_quiz', methods=['GET'])
@login_required
def generate_quiz():
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    # 🔄 Fetch distinct topics for the dropdown
    conn = get_db_connection()
    topics = conn.execute("SELECT DISTINCT topic FROM quiz_questions WHERE topic != '' ORDER BY topic ASC").fetchall()
    conn.close()

    topic_list = [row['topic'] for row in topics]
    return render_template('generate_quiz.html', topics=topic_list)

@app.route('/admin/generate', methods=['GET'])
@login_required
def preview_quiz():
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    # 🔍 Get filter inputs
    category = request.args.get('category', '').strip().lower()
    topic = request.args.get('topic', '').strip().lower()
    limit = request.args.get('limit', '10').strip()  # ✅ Default to 10 if missing
    show_answers = request.args.get('show_answers', '1') == '1'
    export = request.args.get('export', '').strip().lower() == 'pdf'

    # 🔍 Query construction
    conn = get_db_connection()
    query = "SELECT * FROM quiz_questions WHERE 1=1"
    params = []

    if category:
        query += " AND LOWER(category) = ?"
        params.append(category)

    if topic:
        query += " AND LOWER(topic) LIKE ?"
        params.append(f"%{topic}%")

    query += " ORDER BY RANDOM()"
    if limit and limit.isdigit():
        query += " LIMIT ?"
        params.append(int(limit))

    questions = conn.execute(query, tuple(params)).fetchall()
    conn.close()

    # ✅ Store quiz in session for export/email
    session['export_questions'] = [dict(q) for q in questions]
    session['export_metadata'] = {
        'category': category,
        'topic': topic,
        'show_answers': show_answers
    }

    if export:
        return redirect(url_for('export_quiz_pdf'))

    return render_template(
        'quiz_preview.html',
        questions=questions,
        category=category,
        topic=topic,
        limit=limit,  # ✅ Needed for toggling answers correctly
        show_answers=show_answers
    )

@app.route('/admin/add', methods=['GET', 'POST'])
@login_required
def add_question():
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    if request.method == 'POST':
        data = {k: request.form[k].strip() for k in request.form}
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO quiz_questions (category, topic, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['category'], data.get('topic', ''), data['question'], data['option_a'], data['option_b'],
            data['option_c'], data['option_d'], data['correct_answer'], data['explanation']
        ))
        conn.commit()
        conn.close()
        flash("Question added successfully!", "success")
        return redirect(url_for('admin_panel'))

    return render_template('add_question.html')

@app.route('/admin/edit/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    conn = get_db_connection()
    question = conn.execute("SELECT * FROM quiz_questions WHERE id = ?", (question_id,)).fetchone()

    if not question:
        flash("Question not found.", "warning")
        conn.close()
        return redirect(url_for('admin_panel'))

    if request.method == 'POST':
        data = {k: request.form[k].strip() for k in request.form}
        conn.execute('''
            UPDATE quiz_questions
            SET category=?, topic=?, question=?, option_a=?, option_b=?, option_c=?, option_d=?, correct_answer=?, explanation=?
            WHERE id = ?
        ''', (
            data['category'], data.get('topic', ''), data['question'], data['option_a'], data['option_b'],
            data['option_c'], data['option_d'], data['correct_answer'], data['explanation'], question_id
        ))
        conn.commit()
        conn.close()
        flash("Question updated!", "info")
        return redirect(url_for('admin_panel'))

    conn.close()
    return render_template('edit_question.html', question=question)

@app.route('/admin/delete/<int:question_id>')
@login_required
def delete_question(question_id):
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute("DELETE FROM quiz_questions WHERE id = ?", (question_id,))
    conn.commit()
    conn.close()

    flash("Question deleted.", "danger")
    return redirect(url_for('admin_panel'))

#pdf export
@app.route('/admin/export_pdf')
@login_required
def export_quiz_pdf():
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    questions = session.get('export_questions', [])
    if not questions:
        flash("No questions available for export.", "warning")
        return redirect(url_for('generate_quiz'))

    category = request.args.get('category', '').strip().lower()
    topic = request.args.get('topic', '').strip().lower()
    show_answers = request.args.get('show_answers', '1') == '1'  # 👈 NEW
    now = datetime.now()

    rendered = render_template(
        'quiz_pdf_template.html',
        questions=questions,
        category=category,
        topic=topic,
        now=now,
        show_answers=show_answers  # 👈 NEW
    )

    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(rendered, dest=pdf)

    if pisa_status.err:
        flash("PDF generation failed.", "danger")
        return redirect(url_for('generate_quiz'))

    topic_safe = topic.replace(" ", "_") if topic else "quiz"
    date_str = now.strftime("%Y%m%d")
    suffix = "_answers" if show_answers else "_noanswers"
    filename = f"{topic_safe}{suffix}_{date_str}.pdf"

    pdf.seek(0)
    response = make_response(pdf.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename={filename}'
    return response


#Email sending (for future use)
@app.route('/admin/send_quiz_email')
@login_required
def send_quiz_email():
    if current_user.role != 'teacher':
        flash("Access denied", "danger")
        return redirect(url_for('index'))

    questions = session.get('export_questions', [])
    if not questions:
        flash("No questions available to email. Please generate a quiz first.", "warning")
        return redirect(url_for('generate_quiz'))

    # 🧠 Extra filters for context
    category = request.args.get('category', '').strip().lower()
    topic = request.args.get('topic', '').strip().lower()
    show_answers = request.args.get('show_answers', '1') == '1'
    now = datetime.now()

    # 📧 Simulated Email Preview
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body { font-family: Arial; padding: 2rem; }
            .meta { color: #555; font-size: 0.9rem; margin-bottom: 1rem; }
            .question { margin-bottom: 1rem; }
            .answer, .explanation { margin-left: 1rem; font-size: 0.9rem; }
        </style>
    </head>
    <body>
        <h2>📧 Simulated Quiz Email Sent!</h2>
        <p class="meta">
            Exported on {{ now.strftime('%Y-%m-%d %H:%M') }} <br>
            {% if category %}📘 Difficulty: <strong>{{ category.capitalize() }}</strong>{% endif %}
            {% if topic %} {% if category %} | {% endif %}🏷️ Topic: <strong>{{ topic }}</strong>{% endif %}
            <br>
            {% if show_answers %}✅ Answers & Explanations Included{% else %}🚫 Answers Hidden{% endif %}
        </p>

        {% for q in questions %}
        <div class="question">
            <strong>Q{{ loop.index }}:</strong> {{ q['question'] }}<br>
            <div class="answer">A. {{ q['option_a'] }}</div>
            <div class="answer">B. {{ q['option_b'] }}</div>
            <div class="answer">C. {{ q['option_c'] }}</div>
            <div class="answer">D. {{ q['option_d'] }}</div>

            {% if show_answers %}
            <div class="explanation">
                ✅ Answer: <strong>{{ q['correct_answer'] }}</strong>
                {% if q['explanation'] %} | 💡 {{ q['explanation'] }}{% endif %}
            </div>
            {% endif %}
        </div>
        {% endfor %}

        <hr>
        <p><a href="{{ url_for('generate_quiz') }}">🔙 Back to Quiz Generator</a></p>
    </body>
    </html>
    """, questions=questions, category=category, topic=topic, now=now, show_answers=show_answers)

if __name__ == '__main__':
    app.run(debug=True)