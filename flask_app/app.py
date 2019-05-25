from flask import Flask, jsonify


app = Flask(__name__)


#  http://mysite.com/ - entry point to the website (root directory)
@app.route('/')
def home():
    #  jsonify convert dictionary into a string
    return jsonify({'message': 'Hello, world!'})


if __name__ == '__main__':
    app.run()

