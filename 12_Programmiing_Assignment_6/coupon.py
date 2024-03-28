# Paul Wade
# PA 6

grocery_cost = float(input("Enter the cost of your groceries: "))

# Determine if amount of groceries is eligible for a coupon award
if grocery_cost <= 0:

	print("You entered an invalid cost of groceries.")

else:

	# Determine the amount of award based on the purchase amount

	if grocery_cost < 10.00:
		coupon_percentage = 0
	elif grocery_cost <= 60.00:
		coupon_percentage = 8
	elif grocery_cost <= 150.00:
		coupon_percentage = 10
	elif grocery_cost <= 210.00:
		coupon_percentage = 12
	else:
		coupon_percentage = 14

	print("Your coupon percentage is: " + str(coupon_percentage) + "%.")

	print("You win a discount coupon of: ${}.".format(str(round((grocery_cost * (coupon_percentage/100)), 2))))
