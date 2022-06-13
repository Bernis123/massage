
import socket

server_ip = '127.0.0.1'
port = 9999

client = socket.socket()

client.connect((server_ip,port))
print('---- Server is connect ----')

print("이름을 입력하세요(ex : jang) : ")
msg=input()

client.send(bytes(msg,'utf-8'))
print('---- Message send ----')

msg = client.recv(1024)
print('---- Message received ----')
print(msg)

client.close()
