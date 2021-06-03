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
		
			"""
			print("FUNFOU")
			sock_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock_file.bind(('127.0.1.1', 8000)) 
			sock_file.listen(100)
			while True:
				con, addr = sock_file.accept() 
				print(addr)
				print(con)
				time.sleep(10)
				nome_arq = (msg[10:].decode())
				print('Arquivo solicitado:', nome_arq)
				
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
				break
			print("Fechando...")
			arq.close()
			con.close()
			sock_file.close()
			"""
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

#threading.Thread(target=envia_mensagem).start() 
"""
while True:
	msg,cliente = udp.recvfrom(1024)
	if not cliente in clientess:
		clientess.append(cliente)
		print(f"{cliente} adicionado!!")
	print(msg.decode())
	if msg[0:10].decode().upper() ==  '/DOWNLOAD ':
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
			break
		print("Fechando...")
		arq.close()
		con.close()
		sock_file.close()
		
	for x in clientess:
		threading.Thread(target=envia_mensagem,args=(udp,x,msg)).start()
"""    
      # quantidade de bytes que espera receber
    
    #print( msg.decode()) # decode = de bytes para string
    #a = input("-> ")
    #udp.sendto(a.encode(),cliente)
#udp.close()


"""
from threading import Thread,get_ident


class Somador(Thread):

    def __init__(self, inicio, fim):
        Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        self.somatorio = 0

    def run(self):
        for i in range(self.inicio, self.fim + 1):
            self.somatorio += i
            print("Thread- ",get_ident())

s1 = Somador(0, 10)
s2 = Somador(11,20)
s1.start()
s1.join()
s2.start()
s2.join()
print(s1.somatorio)
"""

