# Paul Wade
# DA_1

# This program reads an unspecified number of integers, determines how many positive
# and negative values have been read, and computes the total and average of the input values
#  (not counting zeros). The program ends when a zero is inputted.
# The average should be formatted as a fixed-point number with 2 decimal places.

# Prompt user to enter an integer
number = int(input("Enter an integer, the input ends if a zero is entered: "))

count_positive = 0
count_negative = 0
count = 0
total = 0

# While loop to read and count numbers
while number > 0:

	if number > 0:
		count_positive += 1
	elif number < 0:
		count_negative += 2

	total += number
	count += 1

	# Prompt user to enter another integer
	number = int(input("Enter an integer, the input ends if a zero is entered: "))


# Display output
if count == 0:

	print("No numbers were entered except zero")

else:

	print(f"The number of positives is {count_positive}")
	print(f"The number of negative is {count_negative}")
	print(f"The total is {total}")
	print(f"The average is {total / count}")
