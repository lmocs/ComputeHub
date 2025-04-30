from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets

from forms import TipForm, CompoundInterestForm
from calculator import calculateCompoundInterest, calculateTip

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

@app.route('/t', methods=['GET', 'POST'])
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

@app.route('/c', methods=['GET', 'POST'])
def compoundInterest():
    form = CompoundInterestForm()
    data = {
        'principal': form.principal.data,
        'annual_rate': form.annual_rate.data,
        'compound_rate': form.compound_rate.data,
        'time': form.time.data,
        'message': '',
        'total': None,
    }

    if form.validate_on_submit():
        try:
            data['total'] = calculateCompoundInterest(data)
            data['message'] = 'Success'
        except Exception as e:
            data['message'] = f'Error calculating compound interest: {e}'
    else:
        data['message'] = 'Please fill in all fields correctly.'

    return render_template('index.html', form=form, data=data)

@app.route('/internship', methods=['GET', 'POST'])
def internshipPay():
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
