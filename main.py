from pygame import *
from client import Connection
font.init()
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
            self.rect.y-=15
            data['y']-=15
        if keys[K_DOWN] and self.rect.y<565:
            self.rect.y+=15
            data['y']+=15
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
main_menu=transform.scale(image.load('sources/92984159339df76cd563ee8f8b44c368.jpg'),(1280,720))
background=transform.scale(image.load('sources/0b113edf6db30d09a5dff8cca6bfc813.png'),(1280,720))
main_font=font.SysFont('Arial',70)
ball=Ball(605, 325)
play_online=main_font.render('Играть онлайн',1,(0,0,0))
play_solo=main_font.render('Играть против ИИ', 1, (0,0,0))
settings=main_font.render('Настройки',1,(0, 0,0))
exitt=main_font.render('Выйти из игры',1,(0,0,0))
play_online_rect=play_online.get_rect()
play_online_rect.x=80
play_online_rect.y=150

play_solo_rect=play_solo.get_rect()
play_solo_rect.x=650
play_solo_rect.y=150

settings_rect=settings.get_rect()
settings_rect.x=150
settings_rect.y=450

exitt_rect=exitt.get_rect()
exitt_rect.x=700
exitt_rect.y=450

reciever = Reciever()
igrovoi_cikl=True
clock=time.Clock()
display.set_caption('Игра в пинг-понг онлайн')
main_menu_flag=True
is_connected=False
while igrovoi_cikl:
    if main_menu_flag:
        window.blit(main_menu,(0,0))
        window.blit(play_online,(80,150))
        window.blit(play_solo,(650,150))
        window.blit(settings,(150,450))
        window.blit(exitt,(700,450))
    else:

        if not is_connected:
            connection=Connection()
            ismain=connection.recieve_data()
            if ismain.decode()=='1':
                rocketka_number_one=Player(38,285)
                rocketka_number_two=Player(1210,285)
            elif ismain.decode()=='0':
                rocketka_number_one=Player(1210,285)
                rocketka_number_two=Player(38,285)
        window.blit(background,(0,0))
        rocketka_number_one.reset()
        rocketka_number_two.reset()
        rocketka_number_one.move()
        ball.reset()
        ball_x,ball_y,player_y=reciever.get_move()
        rocketka_number_two.get_move(player_y)
        ball.get_move(ball_x,ball_y)
    for i in event.get():
        if i.type==MOUSEBUTTONDOWN:
            mouse_x,mouse_y=i.pos
            if exitt_rect.collidepoint (mouse_x,mouse_y):
                igrovoi_cikl=False
            if play_online_rect.collidepoint (mouse_x,mouse_y):
                main_menu_flag=False
        if i.type==QUIT:
            igrovoi_cikl = False
            
            connection.close_connection()
    clock.tick(60)
    display.update()