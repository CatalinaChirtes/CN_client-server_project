# SERVER

import socket
import _thread

HOST = socket.gethostname()
PORT = 8080
ADDR = (HOST, PORT)
server = socket.socket()  # create the server socket
connected = True

clients = dict()
client_num = 0


def clientMAX(connection: socket.socket, address):
    connection.send(str.encode("NOT_ALLOWED"))


def connectionHandling(connection: socket.socket, address: socket.AddressFamily, client_num: int):
    connection.send(str.encode(
        "\nUser client connected: (IP: " + address[0] + " | PORT: " + str(address[1]) + ")"))

    while True:
        # wait to get data from the client
        data = connection.recv(2048)

        if data:
            response = data.decode()
        else:
            break

        if response == 'CLOSE':
            print("\nUser" + str(client_num) + " got disconnected:\nIP: " +
                  str(address[0]) + "\nPORT: " + str(address[1]) + "\n")
            connection.close()
            del clients[client_num]
            return
        else:
            connection.send(response.encode())

        print("User" + str(client_num) + ": " + data.decode() +
              " (IP: " + str(address[0]) + " | PORT: " + str(address[1]) + ")")


if __name__ == "__main__":
    # try binding the address on the socket
    try:
        server.bind(ADDR)
    except socket.error as err:
        print(str(err))
        exit()

    # start listening for connections
    print(f"Server listening on: \nIP: {socket.gethostbyname(HOST)} \nPORT: {PORT}")
    server.listen(10)

    while connected:
        conn, address = server.accept()

        if len(clients) < 5:
            client_num = client_num + 1
            clients[client_num] = (conn, address)
            print("\nUser" + str(client_num) + " connected on: \nIP: " + address[0] + "\nPORT: " + str(address[1]) + "\n")
            _thread.start_new_thread(connectionHandling, (conn, address, client_num))
        else:
            print("\nAttempted to connect, but USER MAX LIMIT has been reached.\n")
            _thread.start_new_thread(clientMAX, (conn, address))

    server.close()
