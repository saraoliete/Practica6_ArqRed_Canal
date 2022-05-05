from socket import *
from random import *


canalSocket= socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
canal_adress = ('192.168.56.1', 40010)
server_socket_address = ('192.168.56.1', 50010)
client_socket_address = ('192.168.56.1', 50001)

print('starting up on {} port {}'.format(*canal_adress))

canalSocket.bind(canal_adress)


while True:
# Wait for a message
    print('\ncanal on')
    
    mensaje_rx, recv_address= canalSocket.recvfrom(2048)
    
    port = recv_address[1]
    
        
    if mensaje_rx:
        new_msg = mensaje_rx.decode()
        #msg_ruido = ruido(new_msg)   
        
        if port == 50010:
            canalSocket.sendto(new_msg.encode(),client_socket_address)
        elif port == 50001:
            canalSocket.sendto(new_msg.encode(),server_socket_address)
        
        print(recv_address)
        print(new_msg)

