import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 1080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send("touch down 30 60\ntouch up 30 60")
data = s.recv(BUFFER_SIZE)
s.close()

print("Received: ", data)
