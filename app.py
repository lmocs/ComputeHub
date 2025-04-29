from flask import Flask, render_template
from calculator import calculateTip

app = Flask(__name__)

@app.route('/')
def home():
    return f'<h1>Home</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template(
        'home.html',
        name=name,
        calculator='tip'
    )

# NOTE: If the template uses many vars, pass a dict instead
# Use {{ dictionary[''] }}
# calculator.calculateTip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
