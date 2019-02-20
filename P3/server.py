import socket
from Seq import Seq

PORT = 45687
IP = "212.128.253.113"
MAX_OPEN_REQUEST = 56710


def process_client(cs):

    # Reading the message from the client
    msg = cs.recv(2048).decode("utf-8").split()

    counter = 0
    seqq = Seq(msg[0])

    totalmsg = ""

    valid_seq = "ACTG"
    for n in msg[0]:
        if n not in valid_seq:
            totalmsg += "Error"
            totalmsg += "\n"

        elif n in valid_seq:
            counter += 1
    if counter == len(msg[0]):
        totalmsg += "OK!"
        totalmsg += "\n"

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
            elif x == "countA":
                totalmsg += seqq.count("A").n_base
                totalmsg += "\n"
            elif x == "countC":
                totalmsg += seqq.count("C")
                totalmsg += "\n"
            elif x == "countG":
                totalmsg += seqq.count("G")
                totalmsg += "\n"
            elif x == "countT":
                totalmsg += seqq.count("T")
                totalmsg += "\n"
            elif x == "percA":
                totalmsg += seqq.perc("A")
                totalmsg += "\n"
            elif x == "percC":
                totalmsg += seqq.perc("C")
                totalmsg += "\n"
            elif x == "percG":
                totalmsg += seqq.perc("G")
                totalmsg += "\n"
            elif x == "percT":
                totalmsg += seqq.perc("T")
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