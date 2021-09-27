import socket

target_port = 9998
target_host = '127.0.0.1'
#AF_INET : IPV4 ---- SOCK_STREAM : TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#we need to connect since we're using tcp
client.connect((target_host, target_port))
client.send(b"GET / HTTP/1.1\rSYN\r\n\r\n")
response = client.recv(4096)
print('\n------------- HERE IS THE RESPONSE ---------------\n'+response.decode())
client.close()
