from flask import Flask, request, redirect, url_for, make_response, render_template_string

# Initialize Flask app
app = Flask(__name__)

# Pre-defined valid username and password
VALID_USERNAME = "user1"
VALID_PASSWORD = "password123"

# HTML templates with inline CSS styling
login_form_template = '''
    <html>
        <head>
            <title>Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .login-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                }
                h2 {
                    text-align: center;
                    color: #333;
                }
                form {
                    display: flex;
                    flex-direction: column;
                }
                label, input {
                    margin-bottom: 10px;
                }
                input[type="text"], input[type="password"] {
                    padding: 8px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    padding: 10px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                input[type="submit"]:hover {
                    background-color: #218838;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>Login Page</h2>
                <form method="POST" action="/login">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <input type="submit" value="Login">
                </form>
            </div>
        </body>
    </html>
'''

protected_page_template = '''
    <html>
        <head>
            <title>Protected</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .protected-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                h2 {
                    color: #333;
                }
                a {
                    color: #007bff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="protected-container">
                <h2>Welcome, {{ username }}! You are logged in.</h2>
                <a href="/logout">Logout</a>
            </div>
        </body>
    </html>
'''

@app.route('/')
def home():
    # Check if the user is logged in by checking the cookie
    username = request.cookies.get('username')
    
    if username:
        # If logged in, show the protected page
        return render_template_string(protected_page_template, username=username)
    else:
        # If not logged in, redirect to login page
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the credentials are correct
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # If correct, create a response and set a cookie
            response = make_response(redirect(url_for('home')))
            response.set_cookie('username', username)
            return response
        else:
            # If incorrect, show login form again with an error message
            return '''
            <html>
                <body>
                    <h2>Login Failed! Invalid credentials.</h2>
                    <a href="/login">Try again</a>
                </body>
            </html>
            '''
    else:
        # If it's a GET request, display the login form
        return render_template_string(login_form_template)

@app.route('/logout')
def logout():
    # Create a response that redirects to the login page and clears the cookie
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    return response

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5041)

