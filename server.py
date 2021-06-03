"""
***********SERVIDOR UDP + TCP **************

TRATA AS MENSAGENS RECEBIDAS DO CHAT, FUNCIONA COMO O MEDIADOR DO CHAT.


**********SE RECEBER UMA MENSAGEM COMUM, ELE PRINTA E ENVIA PARA OS CLIENTES DO VETOR******************

**********NO DOWNLOAD ELE ABRE UMA CONEXAO TCP PARA ENVIO DE ARQUIVOS DE TEXTO****************


"""


import socket
import threading
import os
import time
TAM_MSG = 1024





def envia_mensagem(sock,client,msg):
	sock.sendto(msg,client)

def envia_arq(msg):
	print("FUNFOU")
	sock_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock_file.bind(('127.0.1.1', 8000)) 
	sock_file.listen(100)
	while True:
			con, addr = sock_file.accept() 
			print(addr)
			print(con)
			nome_arq = (msg[10:].decode())
			print('Arquivo solicitado:', nome_arq)
			try:		
				status_arq = os.stat(nome_arq)
				#con.send(str.encode('+OK \n'))
				
				arq = open(nome_arq, "rb")
				x = 1
				#while x==1 :
				print("LEITURA")
				dados = arq.read()
				#if not dados:
				#x = 0 
				con.send(dados)
				#break
				
				print("Fechando...")
				arq.close()
				con.close()
				sock_file.close()
				break
			except FileNotFoundError:
				print("Arquivo não encontrado!!")
				msg = "Arquivo não existe!!"
				con.send(msg.encode())
				sock_file.close()
				con.close()
			break

def recebe_mensagem(udp,clientess= []):
	while True:
		msg,cliente = udp.recvfrom(1024)
		if not cliente in clientess:
			clientess.append(cliente)
			print(f"{cliente} adicionado!!")
		
		if msg[0:10].decode().upper() ==  '/DOWNLOAD ':
			envia_arq(msg)
		else:
			print(msg.decode())
			for x in clientess:
				threading.Thread(target=envia_mensagem,args=(udp,x,msg)).start()
	udp.close()	
			
HOST = socket.gethostbyname(socket.gethostname())  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
#global yourname = input("Digite seu nome -> ")
udp.bind(orig)

print(f' {HOST} Servidor no ar...')
clientess = []
a = threading.Thread(target=recebe_mensagem,args=(udp,clientess,))
a.start()

