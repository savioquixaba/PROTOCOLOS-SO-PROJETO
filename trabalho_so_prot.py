import socket
import threading

def envia_mensagem(sock,client,msg):
	sock.sendto(msg,client)


def recebe_mensagem(sock):
	msg,cliente = sock.recvfrom(1024)
	print(msg.decode())
	if msg[0:5].decode().upper() ==  '\GET ':
		print("FUNFOU")
		sock_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_file.bind((sock_file.gethostbyname(gethostname()), 8000)) 
		sock_file.listen(100)
		while True:
			con, addr = server.accept() 
			nome_arq = " ".join(msg[6:])
			print('Arquivo solicitado:', nome_arq)
			try:
				status_arq = os.stat(nome_arq)
				con.send(str.encode('+OK {}\n'.format(status_arq.st_size)))
				arq = open(nome_arq, "rb")
				while True:
					dados = arq.read(TAM_MSG)
					if not dados:
						break
					con.send(dados)
			except Exception as e:
				con.send(str.encode('-ERR {}\n'.format(e)))
		arq.close()
		conn.close()
HOST = socket.gethostbyname(socket.gethostname())  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
#global yourname = input("Digite seu nome -> ")
udp.bind(orig)

print(f' {HOST} Servidor no ar...')
clientess = []
#threading.Thread(target=recebe_mensagem).start()
#threading.Thread(target=envia_mensagem).start() 
while True:
     msg,cliente = udp.recvfrom(1024)
     if not cliente in clientess:
     	clientess.append(cliente)
     	print(f"{cliente} adicionado!!")
     print(msg.decode())
     for x in clientess:
     	threading.Thread(target=envia_mensagem,args=(udp,x,msg)).start()
    
      # quantidade de bytes que espera receber
    
    #print( msg.decode()) # decode = de bytes para string
    #a = input("-> ")
    #udp.sendto(a.encode(),cliente)
udp.close()


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

