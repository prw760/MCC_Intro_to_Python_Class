# Paul Wade
# DA 2


try:

	x = int(input("Please enter a number: "))

except ValueError:

	print("You did not enter a number.")


try:

	y = int(input("Please enter your name: "))

except ValueError:

	pass    # If it threw an exception when we tried to convert it to an int, that's a good thing, so do nothing

else:       # else, it must be an integer

	print("You did not enter a string for your name.")
