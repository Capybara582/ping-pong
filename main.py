from pygame import *
from client import Connection
data={'x':38,'y':285}
class Player ():
    def __init__(self, x, y):
        self.y=y
        self.x=x
        self.image=transform.scale(image.load('sources/U+25AF.svg.png'),(30, 150))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=8
            data['y']-=8
        if keys[K_DOWN] and self.rect.y<565:
            self.rect.y+=8
            data['y']+=8
        connection.send_data('ry'+str(data['y']))
    def get_move(self,y):
        self.rect.y=y
class Ball ():
    def __init__(self, x, y):
        self.y=y
        self.x=x
        self.image=transform.scale(image.load('sources/istockphoto.png'),(70, 70))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def get_move(self,x,y):
        self.rect.x=x
        self.rect.y=y
class Reciever():
    def get_move(self):
        new_data=connection.recieve_data()
        new_data=new_data.decode()
        new_data=new_data.split(':')
        ball_x=int(new_data[1].split(',')[0][1:])
        ball_y=int(new_data[1].split(',')[1][1:])
        player_y=int(new_data[0][2:])
        return ball_x,ball_y,player_y
window=display.set_mode((1280,720))
background=transform.scale(image.load('sources/0b113edf6db30d09a5dff8cca6bfc813.png'),(1280,720))
ball=Ball(605, 325)
reciever = Reciever()
igrovoi_cikl=True
clock=time.Clock()
display.set_caption('Игра в пинг-понг онлайн')
connection=Connection()
ismain=connection.recieve_data()
if ismain.decode()=='1':
    rocketka_number_one=Player(38,285)
    rocketka_number_two=Player(1210,285)
elif ismain.decode()=='0':
    rocketka_number_one=Player(1210,285)
    rocketka_number_two=Player(38,285)
while igrovoi_cikl:
    window.blit(background,(0,0))
    rocketka_number_one.reset()
    rocketka_number_two.reset()
    rocketka_number_one.move()
    ball.reset()
    ball_x,ball_y,player_y=reciever.get_move()
    rocketka_number_two.get_move(player_y)
    ball.get_move(ball_x,ball_y)
    for i in event.get():
        if i.type==QUIT:
            igrovoi_cikl = False
            connection.close_connection()
    clock.tick(60)
    display.update()