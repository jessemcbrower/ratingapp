from flask import Flask, request, render_template, redirect
from forms import RatingRequest
from models import Quote

application = Flask(__name__)
application.config['SECRET_KEY'] = 'dev'

@application.template_filter()
def currencyFormat(value):
    value = float(value)
    return "${:,.2f}".format(value)

@application.template_filter()
def numberRounder(value):
    value = float(value)
    return round(value, 2)

@application.route('/', methods=['POST', 'GET'])
def get_info():

	form = RatingRequest()

	if form.validate_on_submit():

		customerid = request.form.get('CustomerID')
		coverage = request.form.get('DwellingCoverage')
		age = request.form.get('HomeAge')
		roof = request.form.get('RoofType')
		units = request.form.get('NumberOfUnits')
		discount = request.form.get('PartnerDiscount')

		quote = Quote(customerid, coverage, age, roof, units, discount)
		quote.calculate_premium()

		return render_template('premium.html',
			form=form,
			quote=quote)

	return render_template('index.html',
		form=form)

@application.route('/premium', methods=['POST'])
def find_premium():

	data = request.get_json()
	customerid = data['CustomerID']
	coverage = data['DwellingCoverage']
	age = data['HomeAge']
	roof = data['RoofType']
	units = data['NumberOfUnits']
	discount = data['PartnerDiscount']	
	quote = Quote(customerid, coverage, age, roof, units, discount)
	quote.calculate_premium()
	return 'Your quoted premium: $' + str(round(quote.Premium, 2))

@application.route('/reset', methods=['GET'])
def reset_form():

	# global customerid
	# form = RatingRequest()

	if request.method == 'GET':
		# customerid += 1
		return redirect('/')