import socket
import threading
import json
import os
from configs import a
import sys
import time
TAM_MSG = 1024
cor = a["estilo"]["cor_fonte"]

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
			#print(dados.decode())
			#if not dados: 
			#	break
			#msg_status = dados.decode()
			#dados = dados[len(msg_status)+1:]
			print("Aperte Enter para receber o arquivo")
			nome_arq = msg_to_send[10:]
			print('Recebendo:', nome_arq)
			arq = open(nome_arq, "wb")
			#tam_arquivo = len(msg_status)
			#tam_arquivo = int(msg_status.split()[1])
			#while True:
			arq.write(dados)
				#tam_arquivo -= 1
				#if tam_arquivo == 0:
				#	break
				#dados = sock.recv(TAM_MSG)
				#if not dados: 
					#break
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
#while True:
	#os.system("clear||cls")
	#for men in vetor:
		#print(men)
b = threading.Thread(target=recvdata, args=(s,vetor,))
b.start()
a = threading.Thread(target=sendata, args=(s,name,))
a.start()
	#msg,recpt = s.recvfrom(1024)
	#if recpt:
	#	vetor.append(msg.decode())
	#b = threading.Thread(target=recvdata, args=(s,vetor,))
