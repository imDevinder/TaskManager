from flask import Flask, render_template, redirect, url_for, request, session, g, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('tasks'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')

        try:
            db = get_db()
            db.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            db.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already taken!', 'error')
            return redirect(url_for('register'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            db = get_db()
            user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                flash('Login successful!', 'success')
                return redirect(url_for('tasks'))
            else:
                flash('Invalid credentials!', 'error')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db.execute('INSERT INTO tasks (user_id, title, description) VALUES (?, ?, ?)',
                   (session['user_id'], title, description))
        db.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('tasks'))

    tasks = db.execute('SELECT * FROM tasks WHERE user_id = ?', (session['user_id'],)).fetchall()
    return render_template('tasks.html', tasks=tasks)

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (task_id, session['user_id']))
    db.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    init_db()  # Initialize the database schema
    app.run(debug=True)
