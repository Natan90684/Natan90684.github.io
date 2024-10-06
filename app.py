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
