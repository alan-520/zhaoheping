from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

@app.route('/test')
def test():
    return 'this is '

if __name__ == '__main__':
    app.run()