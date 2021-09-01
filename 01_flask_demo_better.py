from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'this is my home page! <button>CLick me</button>'


@app.route('/newpage')
def hello2():
    return 'this is my other page! <button onclick="abc">CLick me</button><script>function abc(){alert("clicked")}</script>'

@app.route('/sum/<x>')
def hello3(x):
    y = int(x)
    
    return str(y+1)


app.run()
