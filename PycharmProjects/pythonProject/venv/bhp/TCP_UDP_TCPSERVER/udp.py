import socket

target_host = '127.0.0.1'
target_port = 9997
#sendto and recvfrom are used for UDP based sockets
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#this line isn't in the book, but it's mandatory for UDP socket to work as intended.
client.bind((target_host, target_port))
# WE DON'T NEED TO CONNECT IN UDP BECAUSE IT IS CONNECTIONLESS, UNLIKE TCP
client.sendto(b"AAABBBCCC", (target_host, target_port))
#since my message contains 9 chars, recvfrom should get 9 as minimum parameter.
data, addr = client.recvfrom(9)
print('\n RESPONSE \n'+data.decode())
print('addr=')
print(addr)
print('data=')
print(data)
client.close()