from flask import Flask

from flask import request
app = Flask(__name__)

@app.route('/')
def hello():

    return '<h1>Hello, feature1!</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h2>Hello, {name}! Wiiiiiiiiiiii</h2>'

@app.route('/sumar')
def sumar():
    param1 = int(request.args.get('param1', 0))
    param2 = int(request.args.get('param2', 0))
    result = param1 + param2
    return f'{param1} + {param2} = {result}'

@app.route('/multiplicar')
def multiplicar():
    param1 = int(request.args.get('param1', 0))
    param2 = int(request.args.get('param2', 0))
    result = param1 * param2
    return f'{param1} * {param2} = {result}'

if __name__ == '__main__':
    app.run(debug=True)
