import pygame
import time
import random
pygame.init()
display_width=800
display_height=600
gray=(119,119,119)
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Car Game")
clock=pygame.time.Clock()
carimg=pygame.image.load("car1.jpg")
back=pygame.image.load("grass.jpg")
yellow=pygame.image.load("ystrip.jpg")
car_width=56
myfont = pygame.font.SysFont("None",100)
render_text = myfont.render("CAR CRASHED",1,(0,0,0))
level_text=myfont.render("Level-",1,(0,0,0))
def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car7.jpg")
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))
def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed = "+str(passed),True,(0,0,0))
    score=font.render("Score = "+str(score),True,(255,0,0))
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))
def background():
    gamedisplay.blit(back,(0,0))
    gamedisplay.blit(back,(697,0))
    gamedisplay.blit(yellow,(385,30))
    gamedisplay.blit(yellow,(385,230))
    gamedisplay.blit(yellow,(385,430))
def car(x,y):
    gamedisplay.blit(carimg,(x,y))
def game_loop():
    x=400
    y=470
    x_change=0
    obs_speed=10
    obs=0
    y_cahnge=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                bumped=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obs_speed+=2
                if event.key==pygame.K_b:
                    obs_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x+=x_change
        gamedisplay.fill(gray)
        background()
        obs_starty-=(obs_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obs_speed
        car(x,y)
        score_system(passed,score)
        if x>695-car_width or x<165-car_width:
            gamedisplay.blit(render_text,(150,200))
            pygame.display.update()
            time.sleep(3)
            game_loop()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,display_width-170)
            obs=random.randrange(0,6)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obs_speed+2
                font_level=pygame.font.SysFont("None",100)
                level_text = font_level.render("LEVEL-"+str(level),True,(0,0,0))
                gamedisplay.blit(level_text,(270,200))
                pygame.display.update()
                time.sleep(3)
        if y <obs_starty+obs_height:
            if x>obs_startx and x<obs_startx + obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                gamedisplay.blit(render_text,(150,200))
                pygame.display.update()
                time.sleep(4)
                game_loop()
            
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
    
