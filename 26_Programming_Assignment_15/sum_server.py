# Paul Wade
# PA 15
import socket
import random


# generate 3 random numbers, sum them, and return the sum as a string
def sum_3_random_numbers():

	random_1 = abs(random.randint(-100, 100))
	random_2 = abs(random.randint(-100, 100))
	random_3 = abs(random.randint(-100, 100))

	total = random_1 + random_2 + random_3  # sum the 3 random numbers

	# create a string with the 3 random numbers, the sum, and an equals sign
	return_string = (str(random_1) + " + " + str(random_2) + " + " + str(random_3) + " = " + str(total))

	return return_string   # return the string


# create a server that sends the sum of 3 random numbers to a client
def server_program():

	host = socket.gethostname()     # get the hostname
	port = 9876                     # initiate port no above 1024

	server_socket = socket.socket()     # get instance

	server_socket.bind((host, port))    # bind host address and port t