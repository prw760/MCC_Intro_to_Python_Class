# Paul Wade
# PA 15

import socket
import random


# The server program should include a function named sum_random_numbers. The function should generate three random
# integers between -100 and 100, and sum the absolute values of num1, num2, and num3. The function should return the
# following information: num1 + num2 + num3 = sum

def server_program():
	host = socket.gethostname()
	port = 9876

	return sum_random_numbers()


def sum_random_numbers():

	x = abs(random.randint(-100, 100))
	y = abs(random.randint(-100, 100))
	z = abs(random.randint(-100, 100))

	sum = x + y + z

	result_string = str(x) + " + " + str(y) + " + " + str(z) + " = " + str(x + y + x)

	return result_string
