import socket
host='127.0.0.1'
port=18083
ball_cords={"x":605,'y':325}
ball_speed_x=2
ball_speed_y=2
with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    connection1,address1=s.accept()
    connection1.sendall(1)
    print('Соединение:', address1)
    connection2,address2=s.accept()
    connection1.sendall(0)
    print('Соединение:', address2)
    while True: 
        data1=connection1.recv(1024)
        data2=connection2.recv(1024)
        rocket_y_one=int(data1.decode()[2:])
        rocket_y_two=int(data2.decode()[2:])
        ball_cords['x']+=ball_speed_x
        ball_cords['y']+=ball_speed_y
        if ball_cords['y']<0 or ball_cords['y']>650:
            ball_speed_y*=-1
        
        if ball_cords['x']<=68 and ball_cords['x']>38:
            if ball_cords['y'] in range(rocket_y_one,rocket_y_one+150) or ball_cords['y']+70 in range(rocket_y_one,rocket_y_one+150):
                ball_speed_x*=-1
        
        if ball_cords['x']>=1140 and ball_cords['x']<1170:
            if ball_cords['y'] in range(rocket_y_two,rocket_y_two+150) or ball_cords['y']+70 in range(rocket_y_two,rocket_y_two+150):
                ball_speed_x*=-1
        
        if not data1 and not data2:
            break
        connection1.sendall(data2+f':x{ball_cords["x"]},y{ball_cords["y"]}'.encode())
        connection2.sendall(data1+f':x{ball_cords["x"]},y{ball_cords["y"]}'.encode())