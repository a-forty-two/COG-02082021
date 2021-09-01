from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'this is my home page! <button>CLick me</button>'


app.run()
