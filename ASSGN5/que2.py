from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route that accepts input via URL
@app.route('/')
def home():
    return "Welcome to the Flask app!"

# Define a route that accepts a name as input from the URL
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."

# Define a route that accepts two numbers and returns their sum
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}."

# Define a route that accepts input via query parameters
@app.route('/square')
def square():
    return '''
    Use the URL in this format to calculate a square:
    /square/<number>
    '''

@app.route('/square/<int:number>')
def square_number(number):
    result = number ** 2
    return f"The square of {number} is {result}."

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5013)

