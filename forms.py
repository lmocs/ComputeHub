from wtforms import FloatField, IntegerField, RadioField, SubmitField
from wtforms.validators import InputRequired, NumberRange

from flask_wtf import FlaskForm


class SplitBillForm(FlaskForm):
    subtotal = FloatField('Enter the subtotal: ', validators=[InputRequired(), NumberRange(min=0)])
    tip = RadioField(
        'Choose a tip percentage: ',
        choices=[
            (0, '0%'),
            (10, '10%'),
            (12, '12%'),
            (15, '15%'),
            (18, '18%'),
            (20, '20%'),
            (25, '25%'),
            (30, '30%'),
        ]
    )
    people = IntegerField('Enter the number of people: ', validators=[InputRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')

class CompoundInterestForm(FlaskForm):
    principal = FloatField('Enter principal: ', validators=[InputRequired(), NumberRange(min=0)])
    annual_rate = FloatField('Enter estimated annual rate: ', validators=[InputRequired(), NumberRange(min=0)])
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
    time = FloatField('Enter time (in years): ', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')

class InternshipPayForm(FlaskForm):
    hourly_rate = FloatField('Enter hourly rate: ', validators=[InputRequired(), NumberRange(min=0)])
    hours = FloatField('Enter hours worked in a week: ', validators=[InputRequired(), NumberRange(min=0)], default=40)
    weeks = FloatField('Enter number of weeks working: ', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')
