from socket import *
serverName = 'www.huabuxiu.cn'
serverPort = 12000
clientSocket =socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print(clientSocket.recv(1024))
clientSocket.close()
