from wtforms import FloatField, RadioField, SubmitField, validators
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm

class TipForm(FlaskForm):
    subtotal = FloatField('Enter the subtotal: ', validators=[DataRequired()])
    tip = RadioField(
        'Choose a tip percentage: ',
        choices=[
            (10, '10%'),
            (15, '15%'),
            (20, '20%'),
            (25, '25%'),
            (30, '30%'),
        ]
    )
    submit = SubmitField('Submit')

class CompoundInterestForm(FlaskForm):
    principal = FloatField('Enter principal: ', validators=[DataRequired()])
    annual_rate = FloatField('Enter estimated annual rate: ', validators=[DataRequired()])
    compound_rate = RadioField(
        'Choose a compound rate: ',
        choices=[
            (1, 'Annually'),
            (2, 'Semi-annually'),
            (4, 'Quarterly'),
            (12, 'Monthly'),
            (365, 'Daily'),
        ]
    )
    time = FloatField('Enter time (in years): ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class InternshipPayForm(FlaskForm):
    hourly_rate = FloatField('Enter hourly rate: ', validators=[DataRequired()])
    hours = FloatField('Enter hours worked in a week: ', validators=[DataRequired()], default=40)
    weeks = FloatField('Enter number of weeks working: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
