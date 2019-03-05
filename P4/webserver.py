import socket
import termcolor

# Change this IP to yours!!!!!
IP = "127.0.0.1"
PORT = 8081
MAX_OPEN_REQUESTS = 57


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = input("Type here your request:"), cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    filename1 = "index.html"
    with open(filename1, "r") as file:
        content = file.read()
        file.close()
    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content)))

    response_msg = status_line + header + "\r\n" + content

    filename2 = "blue.html"
    with open(filename2, "r") as file:
        content3 = file.read()
        file.close()
    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content3)))

    response_msg1 = status_line + header + "\r\n" + content3

    filename3 = "pink.html"
    with open(filename3, "r") as file:
        content1 = file.read()
        file.close()
    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content1)))

    response_msg2 = status_line + header + "\r\n" + content1

    filename4 = "error.html"
    with open(filename4, "r") as file:
        content2 = file.read()
        file.close()
    status_line = "HTTP/1.1 200 ok\r\n"

    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(content2)))

    response_msg3 = status_line + header + "\r\n" + content2

    for i in msg:

        if i == "/":
            cs.send(str.encode(response_msg))
        elif i == "/blue":
            cs.send(str.encode(response_msg1))
        elif i == "/pink":
            cs.send(str.encode(response_msg2))
        else:
            cs.send(str.encode(response_msg3))

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
