from socket import *  
from database import *
import json

# Configurando o Servidor local e a porta a ser utilizada
serverName = 'localhost'
serverPort = 3000

# Criando a conexão do tcpserver.py
serverSocket = socket(AF_INET, SOCK_STREAM)
# Atribuindo a porta ao Socket criado
serverSocket.bind((serverName, serverPort))   

# Usando o método listen() para criar uma fila de conexões (tcpclient.py), aceitando até 10 cliente na fila
serverSocket.listen(10)
print('The server is ready to receive')

# Usando loop para que o tcpserver.py fique estudando
while True:

	connectionSocket, addr = serverSocket.accept() 

	# Permite receber a mensagem do Cliente (tcpclient.py) em bytes        
	mensagem = connectionSocket.recv(1024) 

	#envio tbm deve ser em bytes
	mensagem = mensagem.upper()
	connectionSocket.send(mensagem)

	connectionSocket.close()