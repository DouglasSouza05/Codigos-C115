from socket import *  
import time 

# Mensagem a ser enviada
mensagem = "conceitos e tecnologias para dispositivos conectados"

# Configurando o Servidor local e a porta a ser utilizada
serverName = 'localhost'
serverPort = 3000

# Criando a conexão do tcpcliente.py
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Usando o método encode() para transformar string em bytes (que será enviada ao Buffer de TX)
clientSocket.send(mensagem.encode())

# Recebendo a resposta do tcpserver.py e decodificando usando o método decode() para tranformar de bytes para string. Recebendo até 1024 bytes por vez
resposta = clientSocket.recv(1024).decode()

# Printando a resposta
print('Resposta do Servidor (tcpserver.py):' , resposta)

# Fechando a conexão
clientSocket.close()