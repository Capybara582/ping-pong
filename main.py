from pygame import *
from client import Connection
from random import randint
font.init()
data={'x':38,'y':285}
points={'point1':0,'point2':0}
class Player ():
    def __init__(self, x, y):
        self.y=y
        self.x=x
        self.image=transform.scale(image.load('sources/U+25AF.svg.png'),(30, 150))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed_y=15
        self.speed_ii_y=7
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

    def ofline_move(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=15
           
        if keys[K_DOWN] and self.rect.y<565:
            self.rect.y+=15
            
    def ii(self,y):
        # хватит захватывать мир, пожалуйста
        # хватит
        # ХВАААААТИИИТ
        if self.rect.y<=570 and self.rect.y>=0:
            if self.rect.y<y:
                self.rect.y+=self.speed_ii_y
            if self.rect.y>y:
                self.rect.y-=self.speed_ii_y
            if randint(1,900)==1:
                print('1')
                
                self.speed_ii_y=0
            if current_time%350==0:
                self.speed_ii_y=7
                

            if randint(1,500)==1:
                print('2')
                
                self.speed_ii_y=2
            


            if randint(1,400)==1:
                print('3')
                
                self.speed_ii_y*=-1
            


        if self.rect.y>570:
            self.rect.y=570
        if self.rect.y<0:
            self.rect.y=0

           


    def get_move(self,y):
        self.rect.y=y
class Ball ():
    def __init__(self, x, y):
        self.y=y
        self.x=x
        self.speed_x=7
        self.speed_y=7
        self.image=transform.scale(image.load('sources/istockphoto.png'),(70, 70))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def get_move(self,x,y):
        self.rect.x=x
        self.rect.y=y

    def move_offline(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.y<0 or self.rect.y>650:
            self.speed_y*=-1
class Reciever():
    def get_move(self):
        new_data=connection.recieve_data()
        new_data=new_data.decode()
        new_data=new_data.split(':')
        ball_x=int(new_data[1].split(',')[0][1:])
        ball_y=int(new_data[1].split(',')[1][1:])
        player_y=int(new_data[0][2:])
        point1=int(new_data[2][1:].split(',')[0])
        point2=int(new_data[2][1:].split(',')[1])
        return ball_x,ball_y,player_y,point1,point2
        
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
current_time=0
reciever = Reciever()
igrovoi_cikl=True
clock=time.Clock()
display.set_caption('Игра в пинг-понг онлайн')
main_menu_flag=True
online_game=False
ofline_game=False
is_connected=False
is_end_game=False
rocketka_number_one=Player(1210,285)
rocketka_number_two=Player(38,285)
back_main_menu=main_font.render('Главное меню',1,(66, 114, 245))
play_a_game=main_font.render('Играть еще раз',1,(66, 114, 245))
back_main_menu_rect=back_main_menu.get_rect()
play_a_game_rect=play_a_game.get_rect()

while igrovoi_cikl:

    if main_menu_flag:
        window.blit(main_menu,(0,0))
        window.blit(play_online,(80,150))
        window.blit(play_solo,(650,150))
        window.blit(settings,(150,450))
        window.blit(exitt,(700,450))
    elif online_game:

        if not is_connected:
            connection=Connection()
            ismain=connection.recieve_data()
            if ismain.decode()=='1':
                rocketka_number_one=Player(38,285)
                rocketka_number_two=Player(1210,285)
            elif ismain.decode()=='0':
                rocketka_number_one=Player(1210,285)
                rocketka_number_two=Player(38,285)
            is_connected=True
        window.blit(background,(0,0))
        rocketka_number_one.reset()
        rocketka_number_two.reset()
        rocketka_number_one.move()
        ball.reset()
        ball_x,ball_y,player_y,point1,point2=reciever.get_move()
        rocketka_number_two.get_move(player_y)
        points=main_font.render(f'{point1}:{point2}',1,(0,0,0))
        window.blit(points,(590,10))
        ball.get_move(ball_x,ball_y)
    
    
    
    elif ofline_game:
        current_time+=1
        window.blit(background,(0,0))
        rocketka_number_one.reset()
        rocketka_number_two.reset()
        points_text=main_font.render(f'{points["point1"]}:{points["point2"]}',1,(0,0,0))
        window.blit(points_text,(590,10))
        rocketka_number_two.ofline_move()
        rocketka_number_one.ii(ball.rect.y)
        ball.move_offline()
        ball.reset()
        if ball.rect.colliderect(rocketka_number_one.rect) or ball.rect.colliderect(rocketka_number_two.rect):
            ball.speed_x*=-1
            
        if ball.rect.x>1280:
            points['point1']+=1
            ball.rect.x=605
            ball.rect.y=325
            ball.speed_x*=-1 if randint(0,1)==1 else 1
            ball.speed_y*=-1 if randint(0,1)==1 else 1

        if ball.rect.x<-70:
            points['point2']+=1
            ball.rect.x=605
            ball.rect.y=325
            ball.speed_x*=-1 if randint(0,1)==1 else 1
            ball.speed_y*=-1 if randint(0,1)==1 else 1

        if points['point1']==3 or points['point2']==3:
            if points['point1']>points['point2']:
                exit_game_text='Вы выиграли'
            else:
                exit_game_text='Выиграл ИИ'
            exit_game=main_font.render(exit_game_text,1,(66, 114, 245))
            is_end_game=True
            ofline_game=False
            
    elif is_end_game:
        window.blit(background,(0,0))
        window.blit(exit_game,(450,500))
        window.blit(play_a_game,(150,150))
        window.blit(back_main_menu,(150,300))
        play_a_game_rect.x=150
        play_a_game_rect.y=150
        back_main_menu_rect.x=150
        back_main_menu_rect.y=300

    for i in event.get():
        if main_menu_flag:
            if i.type==MOUSEBUTTONDOWN:
                mouse_x,mouse_y=i.pos
                if exitt_rect.collidepoint (mouse_x,mouse_y):
                    igrovoi_cikl=False

                if play_online_rect.collidepoint (mouse_x,mouse_y):
                    main_menu_flag=False
                    online_game=True

                if play_solo_rect.collidepoint (mouse_x,mouse_y):
                    main_menu_flag=False
                    ofline_game=True
        if is_end_game:  
            if i.type==MOUSEBUTTONDOWN:
                mouse_x,mouse_y=i.pos
                if play_a_game_rect.collidepoint(mouse_x,mouse_y):
                    is_end_game=False
                    ofline_game=True
                 
                if back_main_menu_rect.collidepoint(mouse_x,mouse_y):
                    is_end_game=False
                    ofline_game=False
                    main_menu_flag=True
            points['point1']=0
            points['point2']=0
            rocketka_number_one.rect.y=285
            rocketka_number_two.rect.y=285            
            ball.rect.x=605
            ball.rect.y=325
        if i.type==QUIT:
            igrovoi_cikl = False
            
            connection.close_connection()
     
    clock.tick(60)
    display.update()