from flask import Flask, render_template, request, redirect, url_for, flash
from users import UserManager
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
user_manager = UserManager()

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/profile')
def profile():
    # For demonstration, we'll use a mockup list of posts
    posts = [
        {"content": "Hello World! This is my first post! 🥳", "image": "path/to/image1.jpg"},
        {"content": "Check out my cool new project!", "image": "path/to/image2.jpg"}
    ]
    return render_template('profile.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']
        if user_manager.is_valid_registration(email, username, password, birthday):
            user_manager.add_user(email, username, password)
            flash('Registration successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid registration details.')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_manager.is_valid_login(username, password):
            flash('Login successful!')
            return redirect(url_for('profile'))
        else:
            flash('Invalid login credentials.')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/banned/<username>')
def banned_user(username):
    if username in user_manager.banned_users:
        return render_template('banned.html', username=username)
    else:
        abort(404)
/natan_project/
│
├── app.py          # Main Python file for your Flask app
├── /templates/     # Folder containing your HTML files
│   ├── home.html
│   ├── profile.html
│   ├── register.html
│   ├── login.html
│   ├── banned.html  # Updated banned user page
│   ├── 404.html
│   ├── settings.html
│   └── explore.html
│
├── /static/        # Folder for static files like CSS and images
│   ├── styles.css
│   └── profile_pictures/
│
└── requirements.txt # For dependencies
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# Example user manager (you should implement this with real logic)
class UserManager:
    def __init__(self):
        self.banned_users = []

    # Add methods for user management as needed

user_manager = UserManager()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile/<username>')
def profile(username):
    # Logic for displaying user profile
    return render_template('profile.html', username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/banned/<username>')
def banned_user(username):
    if username in user_manager.banned_users:
        return render_template('banned.html', username=username)
    else:
        abort(404)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
pip install -r requirements.txt
python app.py

