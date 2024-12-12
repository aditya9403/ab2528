from flask import Flask, request, abort

# Initialize Flask app
app = Flask(__name__)

# Pre-defined correct password
CORRECT_PASSWORD = "patil333"

@app.route('/')
def home():
    return '''
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
                    width: 300px;
                    text-align: center;
                }
                h2 {
                    color: #333;
                }
                label, input {
                    display: block;
                    width: 100%;
                    margin-bottom: 10px;
                }
                input[type="password"] {
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
                <h2>Enter the password to access:</h2>
                <form action="/login" method="POST">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def login():
    # Retrieve the password entered by the user
    password = request.form['password']

    # Check if the password is correct
    if password != CORRECT_PASSWORD:
        # If password is incorrect, abort with a 401 Unauthorized error
        abort(401)

    # If the password is correct, return a success message
    return '''
    <html>
        <head>
            <title>Access Granted</title>
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
                .success-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 300px;
                }
                h2 {
                    color: #28a745;
                }
                p {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="success-container">
                <h2>Access Granted!</h2>
                <p>Welcome to the protected area!</p>
            </div>
        </body>
    </html>
    '''

# Custom error handler for 401 Unauthorized
@app.errorhandler(401)
def unauthorized_error(error):
    return '''
    <html>
        <head>
            <title>Unauthorized Access</title>
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
                .error-container {
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 300px;
                }
                h2 {
                    color: #dc3545;
                }
                p {
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
            <div class="error-container">
                <h2>401 Unauthorized</h2>
                <p>Incorrect password. You are not authorized to access this page.</p>
                <a href="/">Go back to login</a>
            </div>
        </body>
    </html>
    ''', 401

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5032)

