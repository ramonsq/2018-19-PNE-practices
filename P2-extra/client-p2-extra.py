from typing import Any, Union

from Seq import Seq

# Programming our first client

import socket

#Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

PORT = 8080
IP = "192.168.1.138"

s0 = input("My sequence:")


# Connect to the server
s.connect((IP, PORT))

s.send(str.encode(str(s0)))

msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER")
print(msg)

s.close()

print("The end")