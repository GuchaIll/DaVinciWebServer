import socket
import random


class HostServer:
    def send_data():
        sock = socket.socket(sock.AF_INET, socket.SOCK_STREAM)
        server_address = ('rasberry pi address ip', 12345) #rasberry pi address ip
        socket.connect(server_address)
        
        while True:
            data = str(random.randint(0, 100)) + "\n"
            sock.sendall(data.encode())
            
 