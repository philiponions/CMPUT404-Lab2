import socket
import os

HOST = "127.0.0.1"
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()

def handle_client(conn):    
    while True:        
        data = conn.recv(1024)        
        if not data:                           
            break
             
        conn.sendall(data)        


def main():    
    while True:
        conn, addr = s.accept()
        # Create a new copy of itself for every client that arrives
        # so each client gets its own private copy of the server to interact with
        pid = os.fork()
        if pid == 0:
            handle_client(conn)       
            print("Finished")       
            break # Close
            
main()