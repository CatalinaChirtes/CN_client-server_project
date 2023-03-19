# CLIENT

import socket

print("Do you want to manually give the IP address and port? [y/n]")
answer = input()
if answer == 'y':
    HOST = input("Please provide the server IP address: ")
    PORT = int(input("Please provide the port of the server: "))
elif answer == 'n':
    HOST = socket.gethostname()
    PORT = 8080

ADDR = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # try connecting to the server
    try:
        s.connect(ADDR)
    except:
        s.close()
        print("Cannot connect to the server :(\n")
        exit()

    print("\n------------------ hello :) ------------------")
    print("you can type any message and the server will display it")
    print("typing CLOSE will terminate the connection\n")

    while True:
        # Wait to receive data from the server
        data = s.recv(2048)
        print("Received message: " + data.decode())
        message = bytes(input("\nEnter message: ").encode().strip())

        # If the message is empty, continue to next iteration of the loop
        while not message:
            message = bytes(input().encode().strip())

        # If we send "!close", we will terminate the client side
        if message == b"CLOSE":
            print("\nTerminating client side.")
            s.sendall(message)
            exit()
        else:
            s.sendall(message)
