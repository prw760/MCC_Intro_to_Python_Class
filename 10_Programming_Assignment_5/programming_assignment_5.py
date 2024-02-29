# Paul Wade
# PA 5

# Obtain loan balance, payment, and interest rate values from the user
current_balance = round(float(input("Enter the loan balance: ")), 2)
payment = round(float(input("Enter the loan payment: ")), 2)
rate = float(input("Enter the interest rate: "))

# init the payment counter
payment_counter = 0


# Calculate number of payments required for a loan-payoff
while current_balance > 0:

	# keep track of how many payments have been made so far
	payment_counter += 1

	interest = current_balance * rate

	# Debugging Code
	# print("\nPayment", payment_counter, "balance = ", current_balance, ", interest = ", interest)

	current_balance += interest
	current_balance = round(current_balance, 2)

	# Debugging Code
	# print("Payment", payment_counter, "current balance with interest: ", current_balance)

	current_balance -= payment
	current_balance = round(current_balance, 2)

	# Debugging Code
	# print("After ", payment, "Payment", payment_counter, " applied: ", current_balance)


print("The number of payments required is:", payment_counter)
