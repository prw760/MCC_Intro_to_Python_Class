# Paul Wade
# PA 4


# ***** Function Definitions Section *****

def calculate_city_tax(amount):
	"""Calculate, print, and return the city tax amount based on sales_amount parameter"""
	city_tax_calc = round((amount * 0.06125), 2)
	print(f"The city tax amount is ${city_tax_calc:.2f}")
	return city_tax_calc


def calculate_county_tax(amount):
	"""Calculate, print, and return the county tax amount based on sales_amount parameter"""
	county_tax_calc = round((amount * 0.0475), 2)
	print(f"The county tax amount is ${county_tax_calc:.2f}")
	return county_tax_calc


def calculate_state_tax(amount):
	"""Calculate, print, and return the state tax amount based on sales_amount parameter"""
	state_tax_calc = round((amount * 0.01625), 2)
	print(f"The state tax amount is ${state_tax_calc:.2f}")
	return state_tax_calc


# ***** Start of Main Program *****

sales_amount = round(float(input("Enter the sales amount: ")), 2)


# calculate/print city, county, state taxes,
# and use those values to calculate/print total tax too

print(f"The total tax amount is ${
						calculate_city_tax(sales_amount) + 
						calculate_county_tax(sales_amount) + 
						calculate_state_tax(sales_amount)
						:.2f}")
