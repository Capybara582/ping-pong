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
        connection.send_data(data)
    def get_move(self):
        new_data=connection.recieve_data()
        new_data=new_data.decode()
        new_data=new_data.replace('{','').replace('}','').replace("'", "").split(',')
        x=new_data[0].split(':')[1]
        y=new_data[1].split(':')[1]
        self.rect.x=int(x)
        self.rect.y=int(y)
window=display.set_mode((1280,720))
background=transform.scale(image.load('sources/0b113edf6db30d09a5dff8cca6bfc813.png'),(1280,720))
rocketka_number_one=Player(38,285)
rocketka_number_two=Player(1210,285)
igrovoi_cikl=True
clock=time.Clock()
display.set_caption('Игра в пинг-понг онлайн')
connection=Connection()
while igrovoi_cikl:
    window.blit(background,(0,0))
    rocketka_number_one.reset()
    rocketka_number_two.reset()
    rocketka_number_one.move()
    rocketka_number_two.get_move()
    for i in event.get():
        if i.type==QUIT:
            igrovoi_cikl = False
    clock.tick(60)
    display.update()
