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
