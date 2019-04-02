import socket

# SERVER IP, PORT

PORT = 7005
IP = "212.128.253.79"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

msg = "ACTGATCAT\nlen\ncomplement"
if msg == "":
    msg = "asdf"


# Send the request message to the server
s.send(str.encode(msg))

# Receive the servers response
response = s.recv(2048).decode()

# Print the server's response
print(response)

s.close()
