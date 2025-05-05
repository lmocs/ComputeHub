from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets

from forms import SplitBillForm, CompoundInterestForm, InternshipPayForm
from calculator import calculateSplitBill, calculateCompoundInterest, calculateInternshipPay

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'sketchy'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/split-bill', methods=['GET', 'POST'])
def splitBill():
    name = 'Split Bill'
    form = SplitBillForm()
    data = {
        'subtotal': form.subtotal.data,
        'tip': form.tip.data,
        'people': form.people.data,
        'message': '',
        'total': None,
        'cost_per_person': None,
    }

    if form.validate_on_submit():
        try:
            data['total'], data['cost_per_person'] = calculateSplitBill(data)
            data['message'] = 'Success'
        except Exception as e:
            data['message'] = f'Error calculating the total per person: {e}'
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
    app.run(debug=True)
