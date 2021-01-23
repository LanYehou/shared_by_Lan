import socket
s=socket.socket()
host = '42.193.184.206'
port = 8101
s.connect((host,port))
print (s.recv(1024).decode())
w=input('输入你想发送的消息：\n')
w=w.encode()
s.send(w)
s.close()
