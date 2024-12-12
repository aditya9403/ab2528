'''from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

# Dummy user data
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f'<h1>Welcome back, {username}!</h1><a href="/logout">Logout</a>'
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('username', username)
        return resp
    return 'Invalid credentials! <a href="/">Try again</a>'

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)  # Expire the cookie
    return resp

if __name__ == '__main__':
    app.run(debug=True)'


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            file.save('templates/' + file.filename)  # Adjust 'uploads' directory as needed
            return render_template('success.html', filename=file.filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)'

 

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def customer_details():
    if request.method == 'POST':
        cust_name = request.form['cust_name']
        email = request.form['email']
        mob_no = request.form['mob_no']
        address = request.form['address']
        pincode = request.form['pincode']
        customer_details = {
            'cust_name': cust_name,
            'email': email,
            'mob_no': mob_no,
            'address': address,
            'pincode': pincode
        }
        return render_template('customer_details.html', customer_details=customer_details)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) '''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('routing.html')

@app.route('/calculate', methods=['GET'])
def calculate():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = "Invalid operation"

    return f"The result of {operation}ing {num1} and {num2} is: {result}"

if __name__ == '__main__':
    app.run(debug=True)
