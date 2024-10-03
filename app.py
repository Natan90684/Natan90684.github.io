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

