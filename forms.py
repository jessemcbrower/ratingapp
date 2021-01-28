
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, NumberRange, ValidationError

class RatingRequest(FlaskForm):
	DwellingCoverage = IntegerField('DwellingCoverage', validators=[InputRequired(), NumberRange(min=0, message='Must enter a value greater than zero')])
	HomeAge =  IntegerField('HomeAge', validators=[InputRequired(), NumberRange(min=0, message='Must enter a value greater than zero')])
	RoofType =  SelectField('RoofType', choices=[('asphault', 'Asphault Shingles'), ('tin', 'Tin'), ('wood', 'Wood')], validators=[InputRequired()])
	NumberOfUnits =  SelectField('NumberOfUnits', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
	PartnerDiscount =  SelectField('PartnerDiscount', choices=[('Y', 'Y'), ('N', 'N')], validators=[InputRequired()])
	Calculate = SubmitField('Calculate')
	NewQuote = SubmitField('New Quote')