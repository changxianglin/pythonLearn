from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route("/input/<zhang>")
def input(zhang):
    return '<h1>Bad Request</h1>', 400

if __name__ == '__main__':
    app.run(debug=True)
