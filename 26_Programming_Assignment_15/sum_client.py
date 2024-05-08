# Paul Wade
# PA 15
import socket


# connect to the server, receive random-number-summing information, and print it
def client_program():

	host = socket.gethostname()         # as both code is running on same pc
	port = 9876                         # socket server port number

	client_socket = socket.socket() 	# instantiate
	client_socket.connect((host, port)) # connect to the server

	data = client_s