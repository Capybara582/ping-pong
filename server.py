import socket
host='127.0.0.1'
port=18083
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    connection1,address1=s.accept()
    connection2,address2=s.accept()
    print('Соединение:', address1)
    print('Соединение:', address2)
    while True:
        data1=connection1.recv(1024)
        data2=connection2.recv(1024)
        if not data1 and not data2:
            break
        connection1.sendall(data2)
        connection2.sendall(data1)