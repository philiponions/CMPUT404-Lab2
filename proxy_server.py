import socket
import os

HOST = "127.0.0.1"
PORT = 8001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("www.google.com", 80))
s.bind((HOST, PORT))
s.listen()

def handle_client(conn):
    while True:        
        data = conn.recv(1024)        
        if not data:               
            break
        
        client.send(data)
        response = client.recv(4096)        
        conn.sendall(response)


def main():    
    while True:
        conn, addr = s.accept()
        # Create a new copy of itself for every client that arrives
        # so each client gets its own private copy of the server to interact with
        pid = os.fork()
        if pid == 0:
            handle_client(conn)           
            break # Close
            
main()