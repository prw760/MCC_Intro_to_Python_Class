# EA 4
# Paul Wade

# CHAPTER 6

# 1. Write a while loop that adds the variable number to the variable sum_of numbers. Then it should prompt the user
# with text to enter another whole number (int) and add it to sum_of_numbers. The loop should iterate as long as the
# user enters an even whole number. The whole number can be positive or negative.
# Print sum_of_numbers AFTER EXITING the while loop (4 pts.).
sum_of_numbers = 0  # DO NOT DELETE THIS LINE OF CODE, USE THE VARIABLE IN THE WHILE LOOP
number = int(input('Enter a whole number: '))  # DO NOT DELETE OR MODIFY THIS LINE OF CODE
# The while loop should appear after this comment

while True:

	if number % 2 == 0:
		sum_of_numbers += number
	else:
		break

	number = int(input('Enter a whole number: '))

print(sum_of_numbers)


# 2. Write a for in loop to iterate over class_string, printing each letter on a separate line (2 pts.).
class_string = "PythonProgramming"  # DO NOT DELETE OR MODIFY THIS LINE OF CODE

letter_list = list(class_string)

for char in letter_list:
	print(char)


# 3. Write a for in loop that prints the numbers -4 through 10 on the same line with a comma after each number (3 pts.).

print(', '.join(str(x) for x in range(-4, 11)))


# 4. Write a for in loop that prints the following set of numbers: 12 24 36 48 60 on one line with a space after each
# number by specifying the step value in the range. Examples of using the Step value are covered in the link below:
# https://www.w3schools.com/python/ref_func_range.aspLinks (3 pts.).
print()  # DO NOT DELETE THIS LINE OF CODE

print(' '.join(str(x) for x in range(12, 61, 12)))


# 5. Write a nested for in loop similar to the loop found at the end of section 6.4. The outer loop's range should
# be between the numbers 1 through 5 inclusively using x as the variable. The inner loop's range should be
# between the numbers -5 through -1 inclusively using y as the variable.
# Print the values of x and y inside the inner loop on the same line (3 pts.).
print()  # DO NOT DELETE THIS LINE OF CODE

for x in range(1, 6):
	for y in range(-5, 0):
		print(*(str(x), str(y)), end=" ")
	print("", end="\n")