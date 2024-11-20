from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json

# Print current working directory and file location
print(f"Current working directory: {os.getcwd()}")
print(f"This file location: {os.path.abspath(__file__)}")

# Get the absolute path to the templates directory
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
print(f"Template directory: {template_dir}")
print(f"Template directory exists: {os.path.exists(template_dir)}")
if os.path.exists(template_dir):
    print(f"Template directory contents: {os.listdir(template_dir)}")

# Create Flask app with explicit template folder
app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'debug-key'  # Change this in production!

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user class (replace with database model later)
class User(UserMixin):
    def __init__(self, id, username, password_hash, is_admin=False):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.is_admin = is_admin

# Dummy user storage (replace with database later)
users = {
    1: User(1, 'admin', generate_password_hash('admin'), is_admin=True)
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

# Initialize empty lists for data storage
categories = []
questions = []

# File paths for persistent storage
GAME_DATA_FILE = 'game_data.json'

# Load game data from file
def load_game_data():
    global categories, questions
    if os.path.exists(GAME_DATA_FILE):
        try:
            with open(GAME_DATA_FILE, 'r') as f:
                data = json.load(f)
                categories = data.get('categories', [])
                questions = data.get('questions', [])
                print(f"Loaded {len(categories)} categories and {len(questions)} questions")  # Debug print
        except Exception as e:
            print(f"Error loading game data: {e}")

# Save game data to file
def save_game_data():
    try:
        with open(GAME_DATA_FILE, 'w') as f:
            json.dump({
                'categories': categories,
                'questions': questions
            }, f, indent=2)
            print(f"Saved {len(categories)} categories and {len(questions)} questions")  # Debug print
    except Exception as e:
        print(f"Error saving game data: {e}")

# Load data at startup
load_game_data()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Find user by username
        user = next((u for u in users.values() if u.username == username), None)
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/game')
def game():
    # Get all categories and their questions
    game_categories = []
    for category in categories:
        category_questions = [q for q in questions if q['category_id'] == category['id']]
        game_categories.append({
            'name': category['name'],
            'questions': category_questions
        })
    print(f"Game categories: {game_categories}")  # Debug print
    return render_template('game.html', categories=game_categories)

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('You must be an admin to access this page.', 'error')
        return redirect(url_for('index'))
    return render_template('admin.html', categories=categories)

@app.route('/admin/add_category', methods=['POST'])
@login_required
def add_category():
    if not current_user.is_admin:
        flash('You must be an admin to add categories.', 'error')
        return redirect(url_for('index'))
    
    name = request.form.get('name')
    if name:
        # Generate new ID based on existing categories
        new_id = max([cat["id"] for cat in categories], default=-1) + 1
        categories.append({
            "id": new_id,
            "name": name
        })
        save_game_data()  # Save after adding category
        flash('Category added successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/add_question', methods=['POST'])
@login_required
def add_question():
    if not current_user.is_admin:
        flash('You must be an admin to add questions.', 'error')
        return redirect(url_for('index'))
    
    category_id = request.form.get('category_id')
    question_text = request.form.get('question')
    answer_text = request.form.get('answer')
    value = request.form.get('value')
    
    if category_id and question_text and answer_text and value:
        questions.append({
            "category_id": int(category_id),
            "question": question_text,
            "answer": answer_text,
            "value": int(value)
        })
        save_game_data()  # Save after adding question
        flash('Question added successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/reset', methods=['POST'])
@login_required
def reset_game():
    if not current_user.is_admin:
        flash('You must be an admin to reset the game.', 'error')
        return redirect(url_for('index'))
    
    # Clear all categories and questions
    global categories, questions
    categories = []
    questions = []
    save_game_data()  # Save after resetting
    
    flash('Game has been reset successfully!', 'success')
    return redirect(url_for('admin'))

if __name__ == '__main__':
    print("\nStarting Flask app...")
    print(f"Template folder: {app.template_folder}")
    print(f"Static folder: {app.static_folder}")
    app.run(debug=True, port=5001)
