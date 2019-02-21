import socket
from Seq import Seq

PORT = 5678
IP = "191.168.0.139"
MAX_OPEN_REQUEST = 56710


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8").split()

    seqq = Seq(msg[0])
    totalmsg = ""
    valid_seq = "ACTG"

    counter = 0
    for n in msg[0]:
        if n in valid_seq:
            counter += 1
    if counter == len(msg[0]):
        totalmsg += "OK!"
        totalmsg += "\n"
    elif counter != len(msg[0]):
        totalmsg += "Error"

    for x in msg:

        print("Message from the client: {}".format(x))
        if x == "len":
            totalmsg += str(seqq.len())
            totalmsg += "\n"
        elif x == "complement":
            totalmsg += seqq.complement().strbases
            totalmsg += "\n"
        elif x == "reverse":
            totalmsg += seqq.reverse().strbases
            totalmsg += "\n"

        bases = ["A", "C", "G", "T"]

        for x, i in bases:
            if x == "count{}".format(i):
                totalmsg += seqq.count(i)
                totalmsg += "\n"
            elif x == "count{}".format(i):
                totalmsg += seqq.perc(i)
                totalmsg += "\n"

        # Sending the message back to the client
        # (because we are an echo server)
    cs.send(str.encode(totalmsg))


# Create a socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting or connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # -- Process the client request
    print("Attending client: {}".format(address))

    process_client(clientsocket)

    # -- Process the client request
    clientsocket.close()
