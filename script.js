document.getElementById('signupForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form data
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const birthday = document.getElementById('birthday').value;

    // For demonstration, log the data to the console
    console.log('Email:', email);
    console.log('Username:', username);
    console.log('Password:', password);
    console.log('Birthday:', birthday);

    // Here, you would typically send the data to your backend server
    // Since GitHub Pages does not support backend processing, you can:
    // - Use a service like Firebase, Formspree, or another API to handle form submissions

    // Reset the form after submission
    document.getElementById
