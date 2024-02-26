# EA 3
# Paul Wade

# CHAPTER 6

# 1. Write a function called enrollment that just prints the following: I am enrolled in CIS156.
# No arguments should be passed into the function and the function should not return a value (2 pts.).

def enrollment():
	print("I am enrolled in CIS156.")


# 2. Write a statement to call the enrollment function (1 pt.).

enrollment()


# 3. Write a function named greeting. The function should accept ONE argument, the
# name of the person you are greeting and PRINT the following: Hello <name argument>, how are you doing today?
# The function should not return a value (2 pts.).

def greeting(name):
	print("Hello " + name + ", how are you doing today?")


# 4. Write a statement to call the greeting function passing in an argument of Charlotte (1 pt.).

greeting("Charlotte")


# 5. Write a statement to call the four_args function passing in a value of 16 that will be assigned to parameter a,
# a value of 8.7 that will be assigned to parameter b, a value of -10 that will be assigned to parameter c
# and a value of 12 that will be assigned to parameter d.
# Save the returned answer in a variable named returned_value. Print returned_value (4 pts.).
def four_args(a, b, c, d):  # DO NOT DELETE OR UPDATE THIS FUNCTION
	answer = a + b * c + d  # DO NOT DELETE OR UPDATE THIS FUNCTION
	return answer  # DO NOT DELETE OR UPDATE THIS FUNCTION


returned_value = four_args(16, 8.7, -10, 12)

print(returned_value)