import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))

s.send(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

response = s.recv(4096)

print(response)