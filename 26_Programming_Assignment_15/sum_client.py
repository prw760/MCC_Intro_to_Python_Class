# Paul Wade
# PA 15
import socket


def client_program():

	host = socket.gethostname()
	port = 9877

	client_socket = socket.socket()
	client_socket.connect((host, port))

	data = client_socket.recv(1024).decode()

	print('Received from server: ' + data)

	client_socket.close()  # close the connection


if __name__ == '__main__':
	client_program()
