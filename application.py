from flask import Flask, request, render_template, redirect
from forms import RatingRequest
import numpy as np
import constant
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

		data = json.loads(get_data())

		customerid = (data['id'])
		dwelling = round(get_dwelling_rate(data), 3)
		age = get_home_age_rate(data)
		units = get_units_rate(data)
		roof = get_roof_rate(data)
		discount = round(calculate_discount(data), 2)
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

	data = json.dumps(data)

	return data

def get_roof_rate(data):

	r = data['roof']

	if r == 'Asphault Shingles':
		roof = 1.00
	elif r == 'Tin':
		roof = 1.70
	elif r == 'Wood':
		roof = 2.00

	return roof

def get_home_age_rate(data):

	n = int(data['age'])

	if 0 <= n <= 10:
		age = 1.00
	elif 11 <= n <= 35:
		age = 1.50
	elif 36 <= n <= 100:
		age = 1.80
	elif n > 100:
		age = 1.95

	return age

def get_units_rate(data):

	n = int(data['units'])

	if n == 1:
		units = 1.00
	elif n >= 2 and n <= 4:
		units = 0.80

	return units

def get_dwelling_rate(data):

	n = data['coverage']

	dwelling = np.interp(n, constant.DWELLING_COVERAGE, constant.RATING_FACTOR)

	return dwelling

def calculate_subtotal(data):

	subtotal = 350 * get_dwelling_rate(data) * get_home_age_rate(data) * get_roof_rate(data) * get_units_rate(data)

	return subtotal

def calculate_discount(data):

	d = data['discount']

	discount = calculate_subtotal(data) * 0.05 if d == 'Y' else 0

	return discount

def calculate_premium(data):

	premium = round(calculate_subtotal(data) - calculate_discount(data), 2)

	return premium

@application.route('/reset', methods=['GET'])
def reset_form():

	global customerid
	form = RatingRequest()

	if request.method == 'GET':
		# customerid += 1
		return redirect('/')