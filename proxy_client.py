import socket

HOST = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 8001))

while True:
    user = input("")
    s.send(b"GET / HTTP/1.1\r\nHost:127.0.0.1:8001\r\n\r\n")

    response = s.recv(4096)

    print(response)

