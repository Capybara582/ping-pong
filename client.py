import socket
class Connection():
    host='127.0.0.1'
    port=18083
    def __init__(self):
        self.s=socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
    def send_data(self,data):
        self.s.sendall(str(data).encode())
    def recieve_data(self):
        self.data = self.s.recv(1024)
        return self.data 
    def close_connection(self):
        self.s.close()