import socket           
 
s = socket.socket()          
host = '0.0.0.0'
port = 8101                
s.bind((host, port))        
str1='我是蓝业厚，你以连接成功！'
str1=str1.encode()
s.listen(5)                 
while True:
    c,addr = s.accept()     
    print ('连接地址：', addr)
    c.send(str1)
    print('收到：',c.recv(1024).decode())
    c.close()               
