from wtforms import FloatField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from flask_wtf import FlaskForm

class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')

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
