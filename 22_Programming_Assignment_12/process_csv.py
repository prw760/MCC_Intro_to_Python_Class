# Paul Wade
# PA 12

import csv
from datetime import datetime
import math

ASSIGNMENT_PATH = (
	'/users/paulwade/Documents/GitHub/educational/MCC_Intro_to_Python_Class/22_Programming_Assignment_12/ ')

with open(ASSIGNMENT_PATH + 'CrudeOil_20212022.csv', newline='\n') as csvfile:
	csv_reader = csv.DictReader(csvfile, delimiter=',')
	csv_reader.fieldnames = ['Date', 'Close/Last', 'Volume', 'Open', 'High', 'Low']
	oil_data_list = list(csv_reader)  # fill crude oil price data list

oil_data_list.pop(0)  # delete the first row containing header info

# load up list of keys to be used as search constraint later

month_year_keys = []
number_of_trading_days = 0
total_volume = 0

for oil_data_item in oil_data_list:

	date = datetime.strptime(oil_data_item['Date'], '%m/%d/%Y')
	year = str(date.year)
	month = str(date.month).zfill(2)
	month_name = datetime.strftime(date, '%B')

	key_item = {'key': int(year + month), 'year': int(year), 'month': int(month), 'month_name': month_name}

	if key_item not in month_year_keys:
		month_year_keys.append(key_item)

	number_of_trading_days += 1

	total_volume += int(oil_data_item['Volume'])

highest_price_results = []
lowest_price_results = []

# iterate through each month
for key_item in month_year_keys:

	this_key = key_item['key']
	this_year = key_item['year']
	this_month = str(key_item['month']).zfill(2)
	this_month_name = key_item['month_name']

	this_months_highest_price = float(0.00)
	this_months_lowest_price = float(9999999.99)

	for oil_data_item in oil_data_list:

		date = datetime.strptime(oil_data_item['Date'], '%m/%d/%Y')
		year = int(date.year)
		month = str(date.month).zfill(2)
		closing_price = float(oil_data_item['Close/Last'])

		if month == this_month and year == this_year:

			if closing_price > this_months_highest_price:
				this_months_highest_price = closing_price

			if closing_price < this_months_lowest_price:
				this_months_lowest_price = closing_price

	highest_price_results.append({'key': this_key, 'year': this_year, 'month': this_month,
											'month_name': this_month_name, 'price': this_months_highest_price})

	lowest_price_results.append({'key': this_key, 'year': this_year, 'month': this_month,
											'month_name': this_month_name, 'price': this_months_lowest_price})


print("The highest price per month for crude oil (August 2021 - July 2022):")

for high_price_item in highest_price_results:

	high_price_month_name = high_price_item['month_name']
	high_price_year = str(high_price_item['year'])
	high_price = '${:,.2f}'.format(high_price_item['price'])

	print(high_price_month_name + " " + high_price_year + "'s highest price was: " + high_price)

print("\nThe lowest price per month for crude oil (August 2021 - July 2022):")

for low_price_item in lowest_price_results:

	low_price_month_name = low_price_item['month_name']
	low_price_year = str(low_price_item['year'])
	low_price = '${:,.2f}'.format(low_price_item['price'])

	print(low_price_month_name + " " + low_price_year + "'s highest price was: " + low_price)

print("\nThe number of trading days for the period August 2021 through July 2022:", number_of_trading_days)

print("Total trading volume for the period August 2021 through July 2022:", '{:,}'.format(total_volume))

average_daily_volume = math.floor(total_volume / number_of_trading_days)
#                              ^^^^^^^^^^
# JEFFREY: When I rounded with round(), it gave me 332,021,
# but I wanted to match your results so I used math.floor() here

print("Average daily trading volume for the period August 2021 through July 2022:", '{:,}'.format(average_daily_volume))

# EXTRA CREDIT ANSWER: Russia invaded Ukraine
