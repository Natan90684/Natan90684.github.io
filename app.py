from flask import Flask, request, redirect, render_template, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a strong key in production

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']
        
        # Calculate user age
        birthdate = datetime.strptime(birthday, '%Y-%m-%d')
        age = calculate_age(birthdate)

        if age < 12:
            flash("You must be 12 years or older to sign up.")
            return redirect('/register')

        # Add logic to store the user in the database (e.g., hashed password)
        flash('Registration successful!')
        return redirect('/success')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Add logic to verify user (e.g., password hash checking)
        flash('Login successful!')
        return redirect('/')
    
    return render_template('login.html')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
pip install Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for signup (registration)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']

        # Add logic to store user data into the database here

        return redirect(url_for('home'))  # Redirect to the homepage after signup
    return render_template('signup.html')  # Render signup form (GET request)

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add login logic (authenticate user)

        return redirect(url_for('home'))  # Redirect to homepage after login
    return render_template('login.html')  # Render login form (GET request)

# Home route (logged-in users)
@app.route('/home')
def home():
    return render_template('home.html')

# Error handling for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(e):
    return "405 Method Not Allowed", 405

if __name__ == '__main__':
    app.run(debug=True) 
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    # Handle registration logic here
    return "Registration successful"
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for signup (registration)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']

        # Add logic to store user data into the database here

        return redirect(url_for('home'))  # Redirect to the homepage after signup
    return render_template('signup.html')  # Render signup form (GET request)

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add login logic (authenticate user)

        return redirect(url_for('home'))  # Redirect to homepage after login
    return render_template('login.html')  # Render login form (GET request)

# Home route (logged-in users)
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    # Handle registration logic here
    return "Registration successful"
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for signup (registration)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']

        # Add logic to store user data into the database here

        return redirect(url_for('home'))  # Redirect to the homepage after signup
    return render_template('signup.html')  # Render signup form (GET request)

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add login logic (authenticate user)

        return redirect(url_for('home'))  # Redirect to homepage after login
    return render_template('login.html')  # Render login form (GET request)

# Home route (logged-in users)
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    # Handle registration logic here
    return "Registration successful"
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database setup (SQLite for simplicity)
def init_db():
    conn = sqlite3.connect('natan.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, email TEXT, username TEXT, password TEXT, birthday TEXT)''')
    conn.commit()
    conn.close()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']

        # Check if user already exists
        conn = sqlite3.connect('natan.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ? OR username = ?", (email, username))
        existing_user = c.fetchone()

        if existing_user:
            flash("User already exists. Try logging in instead.")
            return redirect(url_for('signup'))
        
        # Insert new user into database
        c.execute("INSERT INTO users (email, username, password, birthday) VALUES (?, ?, ?, ?)", 
                  (email, username, password, birthday))
        conn.commit()
        conn.close()

        flash("Registration successful! Please log in.")
        return redirect(url_for('login'))

    return render_template('signup.html')

# Log in page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verify user credentials
        conn = sqlite3.connect('natan.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Please try again.")
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    init_db()  # Ensure database is initialized
    app.run(debug=True)
@app.route('/signup', methods=['GET', 'POST'])
