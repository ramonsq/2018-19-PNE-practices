import socket
import termcolor

PORT = 45677
IP = "212.128.253.113"
MAX_OPEN_REQUEST = 5


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    if msg == "EXIT":
        cs.send(str.encode("Server finished"))

        cs.close()
        return False
    print("Message from the client: {}".format(termcolor.cprint(msg, 'green')))
    # Sending the message back to the client
    # (because we are an echo server)
    cs.send(str.encode(msg))

    cs.close()
    return True


# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

active = True
while active:

    print("Waiting or connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request

    if process_client(clientsocket):
        print("Attending client: {}".format(address))
    # -- Process the client request
    else:
        active = False
