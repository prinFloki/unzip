import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    #5 is the max backlog connections
    server.listen(5)
    print(f'[*] Listening on {IP} : {PORT}')

    while True:
        #we receive the client socket on client, and the remote connection details on address
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        #we create a thread that points to handle_client for our client passed in args.
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
#this function handles the client request, it receives then sends back an aknowledgement.
#We can try sending tcp requests to 127.0.0.1 using tcp.py and we should see them here.
def handle_client(socket):
    with socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request}')
        sock.send(b'AKNOWLEDGEMENT')

if __name__ == '__main__':
    main()
