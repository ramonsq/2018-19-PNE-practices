import socket

# SERVER IP, PORT

PORT = 7009
IP = "212.128.253.108"

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    msg = input("> ")
    if msg == "":
        msg = "asdf"


    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print(response)

    s.close()
