# Paul Wade
# PA 15
import socket
import random


def sum_3_random_numbers():

	random_1 = abs(random.randint(-100, 100))
	random_2 = abs(random.randint(-100, 100))
	random_3 = abs(random.randint(-100, 100))

	sum = random_1 + random_2 + random_3

	return_string = (str(random_1) + " + " + str(random_2) + " + " + str(random_3) + " = " + str(sum)

	return return_string


def server_program():

    host = socket.gethostname()
    port = 9876  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()