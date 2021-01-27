
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange

class RatingRequest(FlaskForm):
	DwellingCoverage = IntegerField('DwellingCoverage', validators=[InputRequired(), NumberRange(min=0, max=350000, message='Must be less than $350,000')])
	HomeAge =  IntegerField('HomeAge', validators=[InputRequired(), NumberRange(min=0, max=None)])
	RoofType =  SelectField('RoofType', choices=[('asphault', 'Asphault Shingles'), ('tin', 'Tin'), ('wood', 'Wood')], validators=[InputRequired()])
	NumberOfUnits =  SelectField('NumberOfUnits', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], validators=[InputRequired()])
	PartnerDiscount =  SelectField('PartnerDiscount', choices=[('Y', 'Y'), ('N', 'N')], validators=[InputRequired()])