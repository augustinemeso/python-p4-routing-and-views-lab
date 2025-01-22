from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# 1. Index view (route '/')
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print String view (route '/print/<string>')
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # print the string to the console
    return f'<h1>{text}</h1>'  # display the string in the web browser

# 3. Count view (route '/count/<int:number>')
@app.route('/count/<int:number>')
def count(number):
    numbers = "\n".join(str(i) for i in range(1, number + 1))
    return f'<pre>{numbers}</pre>'  # return numbers as separate lines

# 4. Math view (route '/math/<int:num1>/<operation>/<int:num2>')
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div' or operation == '/':
        if num2 == 0:
            return 'Error: Division by zero'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return f'Error: Unknown operation {operation}'

    return f'<h1>Result: {result}</h1>'

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
