from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random
import copy

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User class
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

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
        return User(user['id'], user['username'])
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

        if not username or not password:
            flash('Username and password are required.', 'warning')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if existing_user:
            flash('Username already exists.', 'danger')
            conn.close()
            return redirect(url_for('register'))

        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful! You can now log in.', 'success')
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
            login_user(User(user['id'], user['username']))
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

if __name__ == '__main__':
    app.run(debug=True)