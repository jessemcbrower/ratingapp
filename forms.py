
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, NumberRange, ValidationError

class RatingRequest(FlaskForm):
	CustomerID = IntegerField('CustomerID', validators=[InputRequired()], default=1)
	DwellingCoverage = IntegerField('DwellingCoverage', validators=[InputRequired(), NumberRange(min=0, max=350000, message='Coverage must be between $0 and $350,000')])
	HomeAge =  IntegerField('HomeAge', validators=[InputRequired(), NumberRange(min=0, message='Home age cannot be less than 0')])
	RoofType =  SelectField('RoofType', choices=[('Asphault Shingles', 'Asphault Shingles'), ('Tin', 'Tin'), ('Wood', 'Wood')], validators=[InputRequired()])
	NumberOfUnits =  SelectField('NumberOfUnits', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
	PartnerDiscount =  SelectField('PartnerDiscount', choices=[('Y', 'Y'), ('N', 'N')], validators=[InputRequired()])
	Calculate = SubmitField('Calculate')
	NewQuote = SubmitField('New Quote')