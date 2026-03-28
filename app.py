from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Babystore App</h1><p>Build: week6-v1</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)