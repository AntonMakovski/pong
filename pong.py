import pygame as pg
import random
import os

from pygame.constants import MOUSEBUTTONDOWN, QUIT

pg.init()


class Player():
    def __init__(self, image, x,y,width,hight,up_button,down_button):
        self.image = pg.transform.scale(pg.image.load(os.path.join('data', image)).convert_alpha(), (width, hight))
        
        self.win_times = 0

        self.x = x
        self.y = y

        self.rect = pg.rect.Rect(x,y,width,hight)

        self.up_button = up_button
        self.down_button = down_button

        self.up = False
        self.down = False

        self.font = pg.font.Font(None, 300)

    def getting(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.up_button:    
                self.up = True
            elif event.key == self.down_button:    
                self.down = True
        elif event.type == pg.KEYUP:
            if event.key == self.up_button:    
                self.up = False
            elif event.key == self.down_button:    
                self.down = False

    def go(self):
        
        if (self.up and self.rect.y>0):
            self.rect.y-=4
        elif (self.down and self.rect.y<400):
            self.rect.y+=4
    
    def blit(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

    def blit_results(self, x):
        mw.blit(self.font.render(str(self.win_times), True , (200,100,100)), (x, 150))
        

class Boll():
    def __init__(self, image, x,y,width,hight):
        self.image = pg.transform.scale(pg.image.load(os.path.join('data',image)).convert_alpha(), (width, hight))

        self.rect = pg.rect.Rect(x,y,width,hight)

        self.up = False
        self.left = False

        self.speed = 2
        self.front_speed = 2

    def colised(self, max_hight, min_hight, player1, player2):
        
        global win_menu
        global game
        
        if self.rect.y <= min_hight:
            self.up = False
            self.front_speed = random.randint(2,3)
            self.speed = random.randint(2,3)
        elif self.rect.y >= max_hight:
            self.up = True
            self.front_speed = random.randint(2,3)
            self.speed = random.randint(2,3)

        if self.rect.colliderect(player1.rect):
            self.left = False  
            self.front_speed = random.randint(2,3)
            self.speed = random.randint(2,3)
        elif self.rect.colliderect(player2.rect):
            self.left = True   
            self.front_speed = random.randint(2,3)
            self.speed = random.randint(2,3)
        if self.rect.x <= 10:
            player2.win_times += 1
            game = False
            win_menu = True 

        elif self.rect.x >= 560:   
            player1.win_times +=1
            game = False
            win_menu = True

    def go(self):
        
        self.colised(450,0,player1,player2)

        if (self.up):
            self.rect.y-=self.speed
        elif not(self.up):
            self.rect.y+=self.speed
        if (self.left):
            self.rect.x-=self.front_speed
        if not(self.left):
            self.rect.x+=self.front_speed
            
    def blit(self):
        mw.blit(self.image,(self.rect.x, self.rect.y))






class Menu():
    def __init__(self, text_ferst_button, text_thecond_button, button_x1,button_x2, button_y1, button_y2, width, hight):
        self.button1 = pg.rect.Rect(button_x1, button_y1, width, hight)
        self.button2 = pg.rect.Rect(button_x2, button_y2, width, hight)

        self.font = pg.font.Font(None, 70)

        self.text_button1 = self.font.render(text_ferst_button, True ,(0,0,0))
        self.text_button2 = self.font.render(text_thecond_button, True ,(0,0,0))

    def getting (self, event):
        global setting_menu
        global start_menu
        global back_was_start_menu
        global game

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button1.collidepoint(pg.mouse.get_pos()):
                start_menu = False
                back_was_start_menu = False
                game = True
            elif self.button2.collidepoint(pg.mouse.get_pos()):
                setting_menu = True
                start_menu = False

    def blit(self):
        pg.draw.rect(mw,(50,50,150),self.button1)
        pg.draw.rect(mw,(50,50,150),self.button2)

        mw.blit(self.text_button1, (self.button1.x, self.button1.y))
        mw.blit(self.text_button2, (self.button2.x, self.button2.y))


class Pause_menu():
    def __init__(self, text_first_button, text_thecond_button, text_thirthd_button, x1, y1, x2, y2, x3, y3, text_x1, text_y1, text_x2, text_y2, text_x3, text_y3, width, hight):
        self.button1 = pg.rect.Rect(x1,y1,width,hight)
        self.button2 = pg.rect.Rect(x2,y2,width,hight)
        self.button3 = pg.rect.Rect(x3,y3,width,hight)

        self.font = pg.font.Font(None, 70)
        
        self.text1 = self.font.render(text_first_button, True,(0,0,0))
        self.text2 = self.font.render(text_thecond_button, True,(0,0,0))
        self.text3 = self.font.render(text_thirthd_button, True,(0,0,0))

        self.text1_x = text_x1
        self.text1_y = text_y1
        self.text2_x = text_x2
        self.text2_y = text_y2
        self.text3_x = text_x3
        self.text3_y = text_y3
    
    def getting(self, event, pause_button):
        global game
        global pause_menu
        global setting_menu

        if (event.type == pg.MOUSEBUTTONDOWN):
            if (pause_button.collidepoint(pg.mouse.get_pos())): 
                game = not(game)
                pause_menu = not(pause_menu)

        if (event.type == pg.KEYDOWN):
            if (event.key == pg.K_ESCAPE): 
                game = not(game)
                pause_menu = not(pause_menu)
        
        
        if (pause_menu):
            if (event.type == pg.MOUSEBUTTONDOWN):
                if (self.button1.collidepoint(pg.mouse.get_pos())):
                    pause_menu = False
                    game = True
                
                elif (self.button2.collidepoint(pg.mouse.get_pos())):
                    pause_menu = False
                    setting_menu = True
                
                elif (self.button3.collidepoint(pg.mouse.get_pos())):
                    quit()               

    def blit(self):
        pg.draw.rect(mw,(50,50,150), self.button1)
        pg.draw.rect(mw,(50,50,150), self.button2)
        pg.draw.rect(mw,(50,50,150), self.button3)

        mw.blit(self.text1,(self.text1_x, self.text1_y))       
        mw.blit(self.text2,(self.text2_x, self.text2_y))
        mw.blit(self.text3,(self.text3_x, self.text3_y))     


class Setting_menu():
    def __init__(self):
        self.main_surface = pg.Surface((550,400))
        self.main_surface.fill((20,20,40))

        self.volume_rect1 = pg.rect.Rect(200, 140, 200, 20)
        self.seting_rect1 = pg.rect.Rect(200, 140, 100, 20)

        self.volume_rect2 = pg.rect.Rect(200, 170, 200, 20)
        self.seting_rect2 = pg.rect.Rect(200, 170, 100, 20)

        self.button_out = pg.rect.Rect(200,250,200,35)

        self.font = pg.font.Font(None, 70)

        self.text1 = self.font.render('music', True, (0,0,0))
        self.text2 = self.font.render('effects', True, (0,0,0))
        self.text3 = self.font.render('exit', True, (0,0,0))

        self.button_down = False

        self.volume_music = 0.5
        self.volume_efects = 0.25



    def getting(self, event, flag):
        global setting_menu
        global start_menu
        global pause_menu

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.button_down = True 
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                self.button_down = False

        if self.button_down:    
            self.cursor_pos_x, self.cursor_pos_y = pg.mouse.get_pos()
        
            self.cursor_pos_x -= 25
            self.cursor_pos_y -= 65

            if self.cursor_pos_x >= 200 and self.cursor_pos_x <= 400:
                    if self.cursor_pos_y >= 140 and self.cursor_pos_y <= 160:
                        self.seting_rect1.width = self.cursor_pos_x-200
                        
                        self.volume_music = self.seting_rect1.width/200

                    elif self.cursor_pos_y >= 170 and self.cursor_pos_y <= 190:
                        self.seting_rect2.width = self.cursor_pos_x-200

                        self.volume_efects = self.seting_rect2.width/200

            if self.button_out.collidepoint(self.cursor_pos_x, self.cursor_pos_y):
                setting_menu = False
                if flag == True:
                    start_menu = True
                else:
                    pause_menu = True

        return self.volume_efects
    
    def blit(self):
        mw.blit(self.main_surface, (25,65))

        pg.draw.rect(self.main_surface, (255,255,255), self.volume_rect1)
        pg.draw.rect(self.main_surface, (255,255,255), self.volume_rect2)

        pg.draw.rect(self.main_surface, (200,100,100), self.seting_rect1)
        pg.draw.rect(self.main_surface, (200,100,100), self.seting_rect2)
        
        pg.draw.rect(self.main_surface, (200,100,100), self.button_out)

        pg.mixer.music.set_volume(self.volume_music)

        self.main_surface.blit(self.text1, (200,90))
        self.main_surface.blit(self.text2, (200, 200))
        self.main_surface.blit(self.text3, (240, 245))


class Win_menu():
    def __init__(self, text_ferst_button, text_thecond_button, button_x1,button_x2, button_y1, button_y2, width, hight):
        self.button1 = pg.rect.Rect(button_x1, button_y1, width, hight)
        self.button2 = pg.rect.Rect(button_x2, button_y2, width, hight)

        self.font = pg.font.Font(None, 70)

        self.text_button1 = self.font.render(text_ferst_button, True ,(0,0,0))
        self.text_button2 = self.font.render(text_thecond_button, True ,(0,0,0))

    def getting (self, event):
        global win_menu
        global game

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.button1.collidepoint(pg.mouse.get_pos()):
                boll.rect.x = 275
                boll.rect.y = 225

                boll.speed = 1
                boll.front_speed = 1

                win_menu = False
                game = True
            elif self.button2.collidepoint(pg.mouse.get_pos()):
                quit()

    def blit(self):
        pg.draw.rect(mw,(50,50,150),self.button1)
        pg.draw.rect(mw,(50,50,150),self.button2)

        mw.blit(self.text_button1, (self.button1.x, self.button1.y))
        mw.blit(self.text_button2, (self.button2.x, self.button2.y))





game = False
win_menu = False
pause_menu = False
start_menu = True
setting_menu = False
back_was_start_menu = True



pause_button = pg.rect.Rect(0,0,50,50)
pause_button_image = pg.transform.scale(pg.image.load(os.path.join('data','pause.png')), (50,50))



mw = pg.display.set_mode((600,500))
mw.fill((200,255, 255))



setting__menu = Setting_menu()
menu = Menu('start', 'settings',200,200,175,275,200,50)
win__menu = Win_menu('continue', 'exit',200,200,175,275,200,50)
pause__menu = Pause_menu('continue', 'settings', 'exit', 200, 150, 200, 225, 200, 300, 200, 150, 200, 225, 250, 300, 200, 50)

player1 = Player('pngwin.png',0,200,50,100,pg.K_w,pg.K_s)
player2 = Player('pngwin.png',550,200,50,100,pg.K_UP,pg.K_DOWN)    

boll = Boll('boll.png', 275,225,50,50)

pg.mixer.music.load(os.path.join('data', 'music.mp3'))
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.5)

clock = pg.time.Clock()

while True:

    pg.draw.rect(mw,(200,255,255),(pg.rect.Rect(0,0,600,500)))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        player1.getting(event) 
        player2.getting(event) 
        
        if (start_menu):    
            menu.getting(event)
        
        if not(start_menu) and not(win_menu) and not(setting_menu):
            pause__menu.getting(event, pause_button)   

        if setting_menu:
            setting__menu.getting(event, back_was_start_menu)  
        
        if win_menu:
            win__menu.getting(event)


    if game:   
        player1.go()
        player2.go()

        player1.blit()
        player2.blit()

        player1.blit_results(100)
        player2.blit_results(400)


        boll.go()

        boll.blit()

        start_menu = False

    elif (start_menu):
        menu.blit()

    if (pause_menu) and not(setting_menu):
        pause__menu.blit()

    if not(start_menu) and not(win_menu):
        mw.blit(pause_button_image,(0,0))

    if setting_menu:
        setting__menu.blit()

    if win_menu:
        win__menu.blit()

    clock.tick(100)
    pg.display.update()