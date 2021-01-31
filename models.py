import numpy as np
import constants

class Quote:

	def __init__(self, CustomerID, DwellingCoverage, HomeAge, RoofType, NumberOfUnits, PartnerDiscount):
		self.CustomerID = CustomerID
		self.DwellingCoverage = DwellingCoverage
		self.HomeAge = int(HomeAge)
		self.RoofType = RoofType
		self.NumberOfUnits = int(NumberOfUnits)
		self.PartnerDiscount = PartnerDiscount

		self.DwellingRate = self.get_dwelling_rate()
		self.AgeRate = self.get_home_age_rate()
		self.RoofRate = self.get_roof_rate()
		self.UnitsRate = self.get_units_rate()
		self.Subtotal = self.get_subtotal()
		self.Discount = self.get_discount()

	def get_dwelling_rate(self):

		return np.interp(self.DwellingCoverage, constants.DWELLING_COVERAGE, constants.RATING_FACTOR)

	def get_home_age_rate(self):

		if 0 <= self.HomeAge <= 10:
			return 1.00
		elif 11 <= self.HomeAge <= 35:
			return 1.50
		elif 36 <= self.HomeAge <= 100:
			return 1.80
		elif self.HomeAge > 100:
			return 1.95

	def get_roof_rate(self):

		if self.RoofType == 'Asphalt Shingles':
			return 1.00
		elif self.RoofType == 'Tin':
			return 1.70
		elif self.RoofType == 'Wood':
			return 2.00

	def get_units_rate(self):

		if self.NumberOfUnits == 1:
			return 1.00
		elif self.NumberOfUnits >= 2 and self.NumberOfUnits <= 4:
			return 0.80

	def get_subtotal(self):

		return constants.BASE_PREMIUM * self.DwellingRate * self.AgeRate * self.RoofRate * self.UnitsRate
	
	def get_discount(self):

		return self.Subtotal * 0.05 if self.PartnerDiscount == 'Y' else 0

	def calculate_premium(self):

		self.Premium = self.Subtotal - self.Discount