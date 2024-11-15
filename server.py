import socket
host='127.0.0.1'
port=18083
ball_cords={"x":605,'y':325}
ball_speed=2
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    connection1,address1=s.accept()
    print('Соединение:', address1)
    connection2,address2=s.accept()
    print('Соединение:', address2)
    while True:
        ball_cords['x']+=ball_speed
        ball_cords['y']+=ball_speed
        data1=connection1.recv(1024)
        data2=connection2.recv(1024)
        if not data1 and not data2:
            break
        connection1.sendall(data2+f':x{ball_cords["x"]},y{ball_cords["y"]}'.encode())
        print(data1+f':x{ball_cords["x"]},y{ball_cords["y"]}'.encode())
        connection2.sendall(data1+f':x{ball_cords["x"]},y{ball_cords["y"]}'.encode())