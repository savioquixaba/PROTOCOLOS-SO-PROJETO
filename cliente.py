"""
**********APLICAÇÃO CLIENTE UDP + TCP *************

COMO FUNCIONA: ELE FUNCIONA SE CONECTANDO A UM SERVIDOR Q VAI TRATAR AS MENSAGENS, RECEBENDO SUA MENSAGEM PARA SI PROPRIO APÓS O ENVIO
		E PARA OS OUTROS CLIENTES TAMBÉM. O SERVIDOR APENAS RECEBE AS MESNAGENS NORMAIS E ENVIA PARA TODOS
		
COMO FUNCIONA O /DOWNLOAD: /DOWNLOAD vai abrir uma conexão TCP, q vai enviar o nome do arquivo de texto solicitado que está no servidor. Se o arquivo não existir,
			   O servidor o avisa e fecha a conexão TCP.

RESUMO:
	- MENSAGENS = UDP
	- DOWNLOAD/ENVIO DE ARQS DE TEXTO = TCP

"""
import socket
import threading
import json
import os
from configs import a
import sys
import time
TAM_MSG = 1024
cor = a["estilo"]["cor_fonte"]

"""
def convert_data_to_ints(data, big_endian=True):
    int_count = len(data) // 4  # Assuming uint is 4 bytes long !!!
    fmt = ">" if big_endian else "<"
    fmt += "I" * int_count
    return struct.unpack(fmt, data[:int_count * 4])
"""

def sendata(sock,nome):
	while True:
		msg_to_send = input()
		if msg_to_send[0:10] == "/DOWNLOAD ":
			soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			sock.sendto(msg_to_send.encode(),('127.0.1.1',5000))
			time.sleep(1)
			soc.connect(('127.0.1.1',8000))
			soc.send(str.encode(msg_to_send))
			print("MSG ENVIADA")
			dados = soc.recv(102400000)
			time.sleep(2)
			nome_arq = msg_to_send[10:]
			if dados.decode() =="Arquivo não existe!!":
				soc.close()
			else:	
				arq = open(nome_arq, "wb")
				arq.write(dados)
				arq.close()
				soc.close()

		else:		
			m = cor+f"{nome}// " + msg_to_send +"\033[0;0m"
			sock.sendto(m.encode(),("127.0.1.1",5000)) 
			time.sleep(1.5)				
		

def recvdata(sock,vet):
	
	while True:
		os.system("clear||cls")
		for men in vetor:
			print(men)
		msg, recpt = sock.recvfrom(1024000)
		if recpt:
			#print(f"{msg.decode()}") 
			vet.append(msg.decode())
	

name = input("Digite seu nome -> ")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
vetor = []
welcome_msg = "***************CHAT DOS PROGRAMADORES**********************"
vetor.append(welcome_msg)
b = threading.Thread(target=recvdata, args=(s,vetor,))
b.start()
a = threading.Thread(target=sendata, args=(s,name,))
a.start()
