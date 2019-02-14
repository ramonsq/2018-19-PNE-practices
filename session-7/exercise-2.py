# Programming our first client

import socket

#Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

PORT = 8083
IP = "212.128.253.64"

file = input("Type a message:")

# Connect to the server
s.connect((IP, PORT))

s.send(str.encode(file))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER")
print(msg)

s.close()

print("The end")