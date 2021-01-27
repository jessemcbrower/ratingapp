from flask import Flask, request, render_template, redirect
from forms import RatingRequest
import numpy as np

application = Flask(__name__)
application.config['SECRET_KEY'] = 'dev'

try:
	customerid
except NameError:
	customerid = 1

@application.route('/', methods=['POST', 'GET'])
def getinfo():

	global customerid

	if request.method == 'GET':
		form = RatingRequest()
		return render_template('index.html', form=form, customerid=customerid)
	elif request.method == 'POST':
		form = RatingRequest()
		data = {

		'id': customerid,
		'coverage': request.form.get('DwellingCoverage'),
		'age': int(request.form.get('HomeAge')),
		'roof': request.form.get('RoofType'),
		'units': request.form.get('NumberOfUnits'),
		'discount': request.form.get('PartnerDiscount')

		}

		dwelling = round(dwellingrate(data), 3)
		age = homeage(data)
		units = unitsrate(data)
		roof = roofrate(data)
		discount = round(discountrate(data), 2)
		rate = findrate(data)

	return render_template('premium.html', form=form, rate=rate, dwelling=dwelling, age=age, units=units, customerid=customerid, roof=roof, discount=discount)

def roofrate(data):
	if data['roof'] == 'asphault':
		roof = 1.00
	elif data['roof'] == 'tin':
		roof = 1.70
	elif data['roof'] == 'wood':
		roof = 2.00
	return roof

def homeage(data):
	if  0 <= data['age'] <= 10:
		age = 1.00
	elif 11 <= data['age'] <= 35:
		age = 1.50
	elif 36 <= data['age'] <= 100:
		age = 1.80
	elif data['age'] > 100:
		age = 1.95
	return age

def unitsrate(data):
	if data['units'] == '1':
		units = 1.00
	elif data['units'] == '2':
		units = 0.80
	elif data['units'] == '3':
		units = 0.80
	elif data['units'] == '4':
		units = 0.80
	return units

def dwellingrate(data):
	x = [100000, 150000, 200000, 250000, 300000, 350000]
	y = [0.971, 1.104, 1.314, 1.471, 1.579, 1.761]
	dwelling = np.interp( data['coverage'], x, y)
	return dwelling

def quoterate(data):
	age = homeage(data)
	roof = roofrate(data)
	units = unitsrate(data)
	dwelling = dwellingrate(data)
	quote = 350 * dwelling * age * roof * units
	return quote

def discountrate(data):
	if data['discount'] == 'Y':
		discount = quoterate(data) * 0.05
	elif data['discount'] == 'N':
		discount = 0
	return discount

def findrate(data):
	rate = round(quoterate(data) - discountrate(data), 2)
	return rate

@application.route('/premium', methods=['GET'])
def showrate():
	if request.method == 'GET':
		return render_template('premium.html')

@application.route('/reset', methods=['GET'])
def resetform():
	global customerid
	form = RatingRequest()
	if request.method == 'GET':
		customerid += 1
		return redirect('/')