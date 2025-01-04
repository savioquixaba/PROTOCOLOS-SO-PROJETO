### Projeto: Comunicação Cliente-Servidor via CMD
Este projeto foi desenvolvido na disciplina de Protocolos de Rede e consiste na criação de um servidor e cliente para comunicação via linha de comando (CMD). Ambos os sistemas foram implementados do zero e utilizam Python e sockets para realizar a troca de mensagens entre cliente e servidor, utilizando um protocolo de comunicação simples.

### Objetivo
O objetivo deste projeto é criar um servidor e um cliente que possam se comunicar de forma bidirecional utilizando sockets e um protocolo customizado para troca de mensagens. O cliente envia mensagens para o servidor, que as processa e responde de volta ao cliente, tudo por meio da linha de comando (CMD).

### Tecnologias Utilizadas
Python: Linguagem de programação utilizada para a implementação do servidor e do cliente.
Sockets: Utilizados para a comunicação de rede entre cliente e servidor.
Protocolos de Rede: Implementação de um protocolo customizado para comunicação entre o cliente e o servidor.

### Funcionalidades
O projeto permite que o cliente e o servidor se comuniquem com as seguintes funcionalidades:

Envio de Mensagens: O cliente pode enviar mensagens para o servidor, que processa e responde de volta.
Comandos Personalizados: O cliente pode enviar comandos específicos definidos no protocolo implementado, e o servidor responde com o resultado ou um código de erro.
Conexão e Desconexão: O cliente pode conectar-se ao servidor e desconectar-se de forma controlada.
Resposta do Servidor: O servidor responde ao cliente com a mensagem solicitada ou com uma mensagem de erro, conforme o caso.

### Exemplos de Uso
Conectar ao Servidor: O cliente se conecta automaticamente ao servidor ao ser executado.
Enviar Mensagens: O cliente pode enviar mensagens, como comandos definidos no protocolo, e o servidor responderá.
Desconectar: O cliente pode enviar um comando para encerrar a comunicação com o servidor.
