# Paul Wade
# PA 15

import socket
import random


def server_program():
	host = socket.gethostname()
	port = 9876

	return sum_random_numbers()


def sum_random_numbers():

	x = abs(random.randint(-100, 100))
	y = abs(random.randint(-100, 100))
	z = abs(random.randint(-100, 100))

	total = x + y + z

	result_string = str(x) + " + " + str(y) + " + " + str(z) + " = " + str(total)

	return result_string
