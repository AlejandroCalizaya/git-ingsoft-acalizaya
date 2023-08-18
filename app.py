from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    return '<h1>Hello, feature1!</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f'<h2>Hello, {name}! Wiiiiiiiiiiii</h2>'

if __name__ == '__main__':
    app.run(debug=True)
