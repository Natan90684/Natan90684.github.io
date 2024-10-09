@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle the form submission (processing)
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        birthday = request.form['birthday']

        # Database insertion logic and user validation
        # ...

        flash("Registration successful!")
        return redirect(url_for('login'))

    return render_template('signup.html')
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Extract data from the request
    email = data['email']
    username = data['username']
    password = data['password']
    birthday = data['birthday']

    # Perform validation and store in the database
    if username == "" or password == "":
        return jsonify({'success': False, 'error': 'Invalid input'})

    # If everything is fine, return success
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
