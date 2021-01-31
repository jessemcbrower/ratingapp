from flask import Flask, request, render_template, redirect, url_for
from forms import RatingRequest
import numpy as np
import constants
import json

application = Flask(__name__)
application.config['SECRET_KEY'] = 'dev'

@application.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)

@application.route('/', methods=['POST', 'GET'])
def get_info():

	form = RatingRequest()

	if form.validate_on_submit():

		# data = json.loads(get_data())
		data = get_data()

		customerid = (data['id'])
		dwelling = round(get_dwelling_rate(data['coverage']), 3)
		age = get_home_age_rate(data['age'])
		units = get_units_rate(data['units'])
		roof = get_roof_rate(data['roof'])
		discount = round(calculate_discount(data['discount']), 2)
		rate = calculate_premium(data)

		return render_template('premium.html',
			form=form,
			data=data, 
			rate=rate,
			dwelling=dwelling,
			age=age,
			units=units,
			customerid=customerid,
			roof=roof,
			discount=discount)

	return render_template('index.html',
		form=form)

def get_data():

	data = {

		'id': request.form.get('CustomerID'),
		'coverage': request.form.get('DwellingCoverage'),
		'age': request.form.get('HomeAge'),
		'roof': request.form.get('RoofType'),
		'units': request.form.get('NumberOfUnits'),
		'discount': request.form.get('PartnerDiscount')

		}

	# data = json.dumps(data)

	return data

def get_roof_rate(roof):

	if roof == 'Asphalt Shingles':
		rate = 1.00
	elif roof == 'Tin':
		rate = 1.70
	elif roof == 'Wood':
		rate = 2.00

	return rate

def get_home_age_rate(age):

	if 0 <= int(age) <= 10:
		rate = 1.00
	elif 11 <= int(age) <= 35:
		rate = 1.50
	elif 36 <= int(age) <= 100:
		rate = 1.80
	elif int(age) > 100:
		rate = 1.95

	return rate

def get_units_rate(units):

	if int(units) == 1:
		rate = 1.00
	elif int(units) >= 2 and int(units) <= 4:
		rate = 0.80

	return rate

def get_dwelling_rate(coverage):

	dwelling = np.interp(coverage, constants.DWELLING_COVERAGE, constants.RATING_FACTOR)

	return dwelling

def calculate_subtotal(data):

	data = get_data()

	subtotal = 350 * get_dwelling_rate(coverage) * get_home_age_rate(age) * get_roof_rate(roof) * get_units_rate(units)

	return subtotal

def calculate_discount(discount):

	data = get_data()
	rate = calculate_subtotal(data) * 0.05 if discount == 'Y' else 0

	return rate

def calculate_premium(data):

	premium = round(calculate_subtotal(data) - calculate_discount(data), 2)

	return premium

@application.route('/calculation', methods=['POST'])
def find_premium():

	data = request.get_json()
	return data

@application.route('/reset', methods=['GET'])
def reset_form():

	# global customerid
	# form = RatingRequest()

	if request.method == 'GET':
		# customerid += 1
		return redirect('/')