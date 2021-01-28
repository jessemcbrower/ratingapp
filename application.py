from flask import Flask, request, render_template, redirect
from forms import RatingRequest
import numpy as np
import constant

application = Flask(__name__)
application.config['SECRET_KEY'] = 'dev'

try:
	customerid
except NameError:
	customerid = 1

@application.route('/', methods=['POST', 'GET'])
def getinfo():

	global customerid
	form = RatingRequest()

	if form.validate_on_submit():

		data = {

		'id': customerid,
		'coverage': request.form.get('DwellingCoverage'),
		'age': int(request.form.get('HomeAge')),
		'roof': request.form.get('RoofType'),
		'units': request.form.get('NumberOfUnits'),
		'discount': request.form.get('PartnerDiscount')

		}

		dwelling = round(dwellingRate(data), 3)
		age = homeAge(data)
		units = unitsRate(data)
		roof = roofRate(data)
		discount = round(discountAmount(data), 2)
		rate = premiumTotal(data)

		return render_template('premium.html',
								form=form, 
								rate=rate,
								dwelling=dwelling,
								age=age,
								units=units,
								customerid=customerid,
								roof=roof,
								discount=discount)

	return render_template('index.html',
								form=form,
								customerid=customerid)

def roofRate(data):
	r = data['roof']
	roof = 1.00 if r == 'asphault' else 1.70 if r == 'tin' else 2.00 if r == 'wood'	else None
	return roof

def homeAge(data):
	n = data['age']
	age = 1.00 if 0 <= n <= 10 else 1.50 if 11 <= n <= 35 else 1.80 if 36 <= n <= 100 else 1.95 if n > 100 else None
	return age

def unitsRate(data):
	n = int(data['units'])
	units = 1.00 if n == 1 else 0.80 if n >= 2 and n <= 4 else None
	return units

def dwellingRate(data):
	n = data['coverage']
	dwelling = np.interp( n, constant.DWELLING_COVERAGE, constant.RATING_FACTOR)
	return dwelling

def premiumSubtotal(data):
	subtotal = 350 * dwellingRate(data) * homeAge(data) * roofRate(data) * unitsRate(data)
	return subtotal

def discountAmount(data):
	d = data['discount']
	discount = premiumSubtotal(data) * 0.05 if d == 'Y' else 0
	return discount

def premiumTotal(data):
	premium = round(premiumSubtotal(data) - discountAmount(data), 2)
	return premium

@application.route('/summary', methods=['GET'])
def rateSummary():
	if request.method == 'GET':
		return render_template('premium.html')

@application.route('/reset', methods=['GET'])
def resetForm():
	global customerid
	form = RatingRequest()
	if request.method == 'GET':
		customerid += 1
		return redirect('/')