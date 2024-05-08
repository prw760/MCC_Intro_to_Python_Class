# Paul Wade
# PA 15
import socket
import random


# generate 3 random numbers, sum them, and return the sum as a string
def sum_random_numbers():

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

	server_socket.bind((host, port))    # bind host address and port together

	while True:

		server_socket.listen(4)         # configure how many client the server can listen simultaneously

		while True:

			print("Waiting for connection...")

			conn, address = server_socket.accept()          # accept new connection

			print("...connected from: " + str(address))

			data = sum_random_numbers()                   # get the sum of 3 random numbers

			conn.send(data.encode())                        # send the sum to the client
			print("Response sent to client")

			conn.close()        					        # close the connection
			print("Client connection closed\n")


if __name__ == '__main__':  # if the script is executed directly
	server_program()           # run the server program
