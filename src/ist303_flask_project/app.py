from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import random

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
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Load user function
@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user:
        return User(user['id'], user['username'])
    return None

# Home page (fetch last quiz score)
@app.route('/')
@login_required
def index():
    conn = get_db_connection()
    last_score = conn.execute(
        'SELECT score, category, taken_at FROM quiz_scores WHERE user_id = ? ORDER BY taken_at DESC LIMIT 1',
        (current_user.id,)
    ).fetchone()
    conn.close()

    if last_score is None:
        last_score = {"score": "No score yet", "category": "N/A", "taken_at": "Never"}

    return render_template('index.html', user=current_user, last_score=last_score)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
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

# Login route
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

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Start quiz (Fetch random 10 questions)
@app.route('/start_quiz/<category>')
@login_required
def start_quiz(category):
    category = category.lower()  # Ensure consistency
    if category not in ["easy", "medium", "hard"]:
        flash("Invalid quiz category!", "danger")
        return redirect(url_for('index'))

    conn = get_db_connection()
    questions = conn.execute(
        '''SELECT id, question, option_a, option_b, option_c, option_d, correct_answer, explanation 
           FROM quiz_questions WHERE category = ? ORDER BY RANDOM() LIMIT 10''',
        (category,)
    ).fetchall()
    conn.close()

    if not questions:
        flash("No questions available in this category.", "warning")
        return redirect(url_for('index'))

    session['quiz'] = [dict(q) for q in questions]  # Store in session
    session['quiz_index'] = 0  # Track question number
    session['score'] = 0  # Initialize score

    return redirect(url_for('quiz_question', category=category))

# Load next question
@app.route('/quiz/question/<category>', methods=['GET', 'POST'])
@login_required
def quiz_question(category):
    if 'quiz' not in session or session['quiz_index'] >= len(session['quiz']):
        return redirect(url_for('quiz_result', category=category))

    question = session['quiz'][session['quiz_index']]
    
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        correct_answer = question['correct_answer']

        if user_answer == correct_answer and 'answered_correctly' not in question:
            session['score'] += 1  # Count only the first attempt
            question['answered_correctly'] = True  # Mark as answered correctly
        
        session['quiz_index'] += 1  # Move to next question

        return render_template('quiz_feedback.html', question=question, user_answer=user_answer, category=category)

    return render_template('quiz_question.html', question=question, category=category)

# Show final quiz results
@app.route('/quiz/result/<category>')
@login_required
def quiz_result(category):
    score = session.get('score', 0)

    # Save result in database
    conn = get_db_connection()
    conn.execute('INSERT INTO quiz_scores (user_id, score, category) VALUES (?, ?, ?)', (current_user.id, score, category))
    conn.commit()
    conn.close()

    # Fix: Change template name to match your actual file
    return render_template('quiz_results.html', score=score, category=category)


# Share results
@app.route('/quiz/share/<category>')
@login_required
def share_results(category):
    score = session.get('score', 0)
    return render_template('quiz_share.html', user=current_user, score=score, category=category)

if __name__ == '__main__':
    app.run(debug=True)
