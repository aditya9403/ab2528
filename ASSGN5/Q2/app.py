
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
    app.run(debug=True, port=5011)
