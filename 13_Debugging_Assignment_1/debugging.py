# Paul Wade
# DA_1

# PW: Added correct line spacing throughout to comply with PIP 8
# PW: Fixed line wraps in included comments to comply with PIP 8

# This program reads an unspecified number of integers, determines how many positive
# and negative values have been read, and computes the total and average of the input values
# (not counting zeros). The program ends when a zero is inputted.

# The average should be formatted as a fixed-point number with 2 decimal places.

# Prompt user to enter an integer
number = int(input("Enter an integer, the input ends if a zero is entered: "))      # PW: Fixed missing close param

count_positive = 0
count_negative = 0
count = 0
total = 0         # PW: Fixed Initialization of total to zero


# While loop to read and count numbers
while number != 0:

	if number > 0:
		count_positive += 1
	else:                              # PW: changed 'elif' to 'else' to simplify code since no 0 can get this far
		count_negative += 1            # PW: changed value to increment from 2 to 1

	total += number

	count += 1

	# Prompt user to enter another integer                                               # PW: Fixed indention
	number = int(input("Enter an integer, the input ends if a zero is entered: "))       # PW: Fixed indention


# Display output
if count == 0:                                            # PW: Added in missing colon
	print("No numbers were entered except zero")
else:
	print(f"The number of positives is {count_positive}")
	print(f"The number of negative is {count_negative}")
	print(f"The total is {total}")                         # PW: Removed whitespace between quote and paren per Pep 8
	print(f"The average is {(total / count):.2f}")         # PW: added in '.2f' formatter to match sample output
