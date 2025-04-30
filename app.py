from re import sub
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets

from forms import NameForm, TipForm
from calculator import calculateTip

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

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

@app.route('/form', methods=['GET', 'POST'])
def index():
    form = NameForm()
    form.validate_on_submit()
    return render_template('index.html', form=form, message='error')


@app.route('/tip', methods=['GET', 'POST'])
def tip():
    form = TipForm()
    data = {
        'subtotal': form.subtotal.data,
        'tip': form.tip.data,
        'message': '',
        'total': None,
    }

    if form.validate_on_submit():
        try:
            data['total'] = calculateTip(data['subtotal'], float(data['tip']))
            data['message'] = 'Success'
        except Exception as e:
            data['message'] = f'Error calculating tip: {e}'
    else:
        data['message'] = 'Please fill in all fields correctly.'

    return render_template('index.html', form=form, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
