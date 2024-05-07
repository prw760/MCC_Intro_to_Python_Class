# Paul Wade
# PA 15

import socket


# The server program should include a function named sum_random_numbers. The function should generate three random
# integers between -100 and 100, and sum the absolute values of num1, num2, and num3. The function should return the
# following information: num1 + num2 + num3 = sum

def server_program():
	host = socket.gethostname()
	port = 9876
