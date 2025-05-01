from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets

from forms import TipForm, CompoundInterestForm, InternshipPayForm
from calculator import calculateCompoundInterest, calculateInternshipPay, calculateTip

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'sketchy'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tip', methods=['GET', 'POST'])
def tip():
    name = 'Tip'
    form = TipForm()
    data = {
        'subtotal': form.subtotal.data,
        'tip': form.tip.data,
        'message': '',
        'total': None,
    }

    if form.validate_on_submit():
        try:
            data['tip'], data['total'] = calculateTip(data)
            data['message'] = 'Success'
        except Exception as e:
            data['message'] = f'Error calculating tip: {e}'
    else:
        data['message'] = 'Please fill in all fields correctly.'

    return render_template('index.html', name=name, form=form, data=data)

@app.route('/compound-interest', methods=['GET', 'POST'])
def compoundInterest():
    name = 'Compound Interest'
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

    return render_template('index.html', name=name, form=form, data=data)

@app.route('/internship-pay', methods=['GET', 'POST'])
def internshipPay():
    name = 'Internship Pay'
    form = InternshipPayForm()
    data = {
        'hourly_rate': form.hourly_rate.data,
        'hours': form.hours.data,
        'weeks': form.weeks.data,
        'message': '',
        'total': None,
    }

    if form.validate_on_submit():
        try:
            data['total'] = calculateInternshipPay(data)
            data['message'] = 'Success'
        except Exception as e:
            data['message'] = f'Error calculating internship pay: {e}'
    else:
        data['message'] = 'Please fill in all fields correctly.'

    return render_template('index.html', name=name, form=form, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
