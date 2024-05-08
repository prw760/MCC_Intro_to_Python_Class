# Paul Wade
# PA 15
import socket
import random


def sum_3_random_numbers():

	random_1 = abs(random.randint(-100, 100))
	random_2 = abs(random.randint(-100, 100))
	random_3 = abs(random.randint(-100, 100))

	total = random_1 + random_2 + random_3

	return_string = (str(random_1) + " + " + str(random_2) + " + " + str(random_3) + " = " + str(total))

	return return_string


def server_program():

	host = socket.gethostname()
	port = 9876

	server_socket = socket.socket()

	server_socket.bind((host, port))

	while True:

		server_socket.listen(2)

		while True:

			print("Waiting for connection...")

			conn, address = server_socket.accept()

			print("...connected from: " + str(address))

			data = sum_3_random_numbers()

			conn.send(data.encode())
			print("Response sent to client")

			conn.close()
			print("Client connection closed")


if __name__ == '__main__':
	server_program()
