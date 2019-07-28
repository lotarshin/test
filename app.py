from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello,world!"


@app.route("/bye")
def bye():
    return "bye,world"


@app.route("again")
def again():
    return "see you again"


if __name__ == '__main__':
    app.run()