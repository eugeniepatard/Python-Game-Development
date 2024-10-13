import pygame
import os 
from main_menu import *
from animations import *
from main_menu import *
from random import *
from copy import deepcopy
from math import *

pygame.init()
class Kirby:
    def __init__(self,x,y):
        self.r=pygame.Rect(x,y,WIDTH_KIRBY,HEIGHT_KIRBY)
        self.frame=0
        self.state="idle"
        self.photo= None
        self.staticframe=0
        self.reload=0
        self.deplacement=[]
        self.summon_position=x,y
        self.destination=None
        self.t=9
        self.summoned=False

BULLETS_DAMAGE=[30,40,50,55,57,59,60,65,70]
BULLETS_VEL=[20,21,22,23,24,25,26,27,29]
ONE_HIT= pygame.USEREVENT +1

COLOR_FONT = (5, 5, 40)
VEL_BG = 2
LOSER_FONT = pygame.font.SysFont('OCR A Extended',80)

class Bullet:
    def __init__(self,x,y,level):
        self.r=pygame.Rect(x,y,WIDTH_BULLET,HEIGHT_BULLET)
        self.damage=BULLETS_DAMAGE[level]
        self.vel=BULLETS_VEL[level]
        self.frame=0
        self.state=0
        self.photo= None
        self.staticframe=0
        self.level=level


ENEMY_DIMENSION={"BeanBon" : (50,50),
                "Coconut" : (40,40),
                "LittleWoods" : (50,80),
                "WaddleDee" : (50,80),
                "Powerup" : (40,40),
                "Cage" : (50,50),
                "WhispyWoods" : (WIDTH-100, (HEIGHT//2)-200)}

ENEMY_VEL=     {"BeanBon" : 3 ,
                "Coconut" : 6,
                "LittleWoods" : 2,
                "WaddleDee" : 4,
                "Powerup" : 3,
                "Cage" : 3,
                "WhispyWoods" : 2}



ENEMY_COLORS=  {"BeanBon" : (0,255,0) ,
                "Coconut" : (0,0,255),
                "LittleWoods" : (0,255,255),
                "WaddleDee" : (255,100,100),
                "Powerup" : (0,255,0),
                "Cage" : (0,255,255)  ,
                "WhispyWoods" : (0,255,255)}

ENEMY_HEALTH=   {"BeanBon" : 50 ,
                "Coconut" : 30,
                "LittleWoods" : 40,
                "WaddleDee" : 70,
                "Powerup" : 0,
                "Cage" : 100,
                "WhispyWoods" : 1000000}

RELOAD_COCONUT=200


class Enemy:
    def __init__(self,x,y,type):
        self.w,self.h=ENEMY_DIMENSION[type]
        self.vel=ENEMY_VEL[type]
        self.color=(0,0,255)
        self.health=ENEMY_HEALTH[type]
        self.r=pygame.Rect(x,y,self.w,self.h)
        self.frame=0
        self.state='idle'
        self.type=type
        self.photo= None
        self.staticframe=0
        self.reload=100

class DeadEntity:
    def __init__(self, dead_entity):
        self.r=pygame.Rect(dead_entity[1][0],dead_entity[1][1],dead_entity[0][0],dead_entity[0][1])
        self.frame=0
        self.state='dmg'
        self.type=dead_entity[2]
        self.photo= None
        self.staticframe=0

class Coconut:
    def __init__(self,x,y):
        self.w,self.h=ENEMY_DIMENSION["Coconut"]
        self.vel=ENEMY_VEL["Coconut"]
        self.color=ENEMY_COLORS["Coconut"]
        self.health=ENEMY_HEALTH["Coconut"]
        self.r=pygame.Rect(x,y,self.w,self.h)
        self.frame=0
        self.state='idle'
        self.type=type
        self.photo= None
        self.staticframe=0
        self.type='Coconut'

        self.vx=-1
        self.sens=1
        self.a=0.1
        self.vy=-2


class Powerup:
    def __init__(self,x0,y):
        self.x=x0
        self.vy=2
        self.r=pygame.Rect(x0,y,ENEMY_DIMENSION["Powerup"][0],ENEMY_DIMENSION["Powerup"][1])
        self.frame=0
        self.state="idle"
        self.photo=None
        self.staticframe=0
    
        self.omega=0.01*2*pi
        self.t=0
        self.amplitude=30
        self.x0=x0

class Cage:
    def __init__(self,x0,y):
        self.x=x0
        self.vy=2
        self.r=pygame.Rect(x0,y,ENEMY_DIMENSION["Cage"][0],ENEMY_DIMENSION["Cage"][1])
        self.frame=0
        self.state="idle"
        self.photo=None
        self.staticframe=0
        self.health=ENEMY_HEALTH["Cage"]
        self.omega=0.01*2*pi
        self.t=0
        self.amplitude=30
        self.x0=x0

class Button():
        def __init__(self, x, y,elevation, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.clicked = False
            self.original_y_pos= y
            self.elevation =elevation
            self.dynamic_elevation=elevation

        def draw(self):
            action = False
            self.rect.y=self.original_y_pos-self.dynamic_elevation

            #get mouse position
            pos = pygame.mouse.get_pos()

            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                self.dynamic_elevation=0
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    action = True
                    self.clicked = True
            else:
                self.dynamic_elevation=self.elevation

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False


            #draw button
            WIN.blit(self.image, self.rect)

            return action


WIDTH, HEIGHT = 700, 850
##frame,type,x
LEVEL1=[(60,"BeanBon",400),(120,"Coconut","r"),(130,"Cage","r"),(135,"BeanBon","r"),(140,"BeanBon","r"),(220,"WaddleDee","r"),(260,"Powerup","r"),(270,"Cage","r"),(300,"LittleWoods","r"),
        (350,"WaddleDee","r"),(360,"WaddleDee","r"),(370,"WaddleDee","r"),(560,"BeanBon",80),(561,"Cage","r"),(562,"BeanBon",180),(564,"BeanBon",220),
        (750,"WaddleDee","r"),(800,"Cage","r"),(850,"WaddleDee","r"),(860,"BeanBon","r"),(865,"BeanBon","r"),(950,"WaddleDee","r"),(980,"LittleWoods","r"),
        (1010,"WaddleDee","r"),(1020,"Cage",WIDTH//2),(1050,"Cage","r"),(1100,"BeanBon","r"),(1101,"BeanBon","r"),(1102,"BeanBon","r"),(1120,"Powerup","r"),
        (1140,"WaddleDee","r"),(1145,"BeanBon","r"),(1150,"Cage","r"),(1162,"BeanBon",WIDTH//2+40),(1200,"LittleWoods",300),
        (1231,"LittleWoods",WIDTH-100),(1280,"LittleWoods",100),(1298,"LittleWoods",150),(1299,"BeanBon",WIDTH//2),
        (1301,"Coconut","r"),(1302,"Coconut","r"),(1410,"WhispyWoods",WIDTH//2-ENEMY_DIMENSION["WhispyWoods"][0]//2),
        (1411,"BeanBon",WIDTH//2+110),(1498,"WaddleDee","r"),(1499,"BeanBon",WIDTH//2+100),
        (1502,"Coconut",100),(1530,"Coconut","r"),(1590,"Coconut","r"),(1600,"Coconut","r"),
        (1650,"Coconut",WIDTH-50),(1710,"Coconut","r"),(1800,"Coconut","r"),(1890,"Coconut","r"),
        (1950,"Coconut",WIDTH//2),(2000,"Coconut",WIDTH//2+10),(2100,"Coconut","r"),(2200,"Coconut","r"),
        (2100,"Coconut","r"),(2200,"Coconut",WIDTH//2+20),(2300,"Coconut",WIDTH//2),(2400,"Coconut",WIDTH//2+10),
        (2450,"Coconut",WIDTH//2+10),(2500,"Coconut",WIDTH//2+10),(2600,"Coconut",WIDTH//2+10),
        (2650,"Coconut",WIDTH//2+10),(2700,"Coconut",WIDTH//2+10),(2750,"Coconut",WIDTH//2+10),
        (2800,"Coconut",WIDTH//2+10),(-1,0)]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

EXPLOSION = pygame.mixer.Sound("Assets/Sound/explosion.mp3")
EXPLOSION.set_volume(1)
POWERUP = pygame.mixer.Sound("Assets/Sound/power_up.mp3")
EXTRA_KIRBY = pygame.mixer.Sound("Assets/Sound/power_up.mp3")
NEW_COCONUT = pygame.mixer.Sound("Assets/Sound/new_coconut.mp3")

WHITE = (255,255,255)
RED=(255,0,0)
WIDTH_KIRBY,HEIGHT_KIRBY=40,40
VEL=10
BULLET_VEL=20
WIDTH_BULLET=8
HEIGHT_BULLET=10
RELOAD_TIME=13
BACKGROUND_IMAGE = pygame.image.load(os.path.join('Assets','Background',"bg_level_1.png"))
#RELOAD_TIME=10
#BACKGROUND_IMAGE = pygame.image.load("bg_level_1.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH,HEIGHT))
BACKGROUND_BOSS_IMAGE = pygame.image.load(os.path.join('Assets','Background','bg_boss_final.png'))
BACKGROUND_BOSS = pygame.transform.scale(BACKGROUND_BOSS_IMAGE, (WIDTH,HEIGHT))

WINNER_IMAGE = pygame.image.load(os.path.join('Assets',"Win_Screen.png"))
GAME_OVER_IMAGE = pygame.image.load(os.path.join('Assets',"Game_over.png"))
WINNER=pygame.transform.scale(WINNER_IMAGE,(WIDTH,HEIGHT))
GAME_OVER=pygame.transform.scale(GAME_OVER_IMAGE,(WIDTH,HEIGHT))

pausee_img=pygame.image.load(os.path.join('Assets','pause_btn.png'))
pause_img=pygame.transform.scale(pausee_img,(WIDTH/7,HEIGHT/20))



etat_deplacement=True
FPS = 60
HIT_FONT=pygame.font.SysFont('OCR A Extended', 40)


def handle_level(level,frame,enemies,powerups,cages):
    if level[0][0]==frame:
        if level[0][2]=="r":
            f,type,x=level.pop(0)
            x=randint(0,WIDTH-ENEMY_DIMENSION[type][0])
        else:
            f,type,x=level.pop(0)
        if type=="Powerup":
            powerups.append(Powerup(x,0))
        elif type=="Cage":
            cages.append(Cage(x,0))
        else:
            enemies.append(Enemy(x,-ENEMY_DIMENSION[type][1],type))

def handle_enemies(enemies,coconuts,s3):
    '''gère les ennemis et les fait avancer sur l'écran. Pour les ennemis spéciales, 
    cette fonction les fait attaquer'''
    if s3!=0:
        for enemy in enemies:
            enemy.r.y+=enemy.vel
            if enemy.type=="BeanBon":
                enemy.reload=(enemy.reload-1)%RELOAD_COCONUT
                if enemy.reload==4:
                    enemy.frame=0
                    enemy.staticframe=0
                    enemy.state='angry'
                if enemy.reload==0:
                    coconuts.append(Coconut(enemy.r.x+ENEMY_DIMENSION["BeanBon"][0]//2-ENEMY_DIMENSION["Coconut"][0]//2,enemy.r.y-ENEMY_DIMENSION["Coconut"][1]))
                    NEW_COCONUT.play()
    else:
        for enemy in enemies:
            if enemy.type == "WaddleDee" or enemy.type == "Coconut":
                enemy.r.y+=enemy.vel
            if enemy.type == "BeanBon":
                enemy.reload=(enemy.reload-1)%RELOAD_COCONUT
                if enemy.reload==4:
                    enemy.frame=0
                    enemy.staticframe=0
                    enemy.state='angry'
                if enemy.reload==0:
                    coconuts.append(Coconut(enemy.r.x+ENEMY_DIMENSION["BeanBon"][0]//2-ENEMY_DIMENSION["Coconut"][0]//2,enemy.r.y-ENEMY_DIMENSION["Coconut"][1]))

                
                


def handle_coconuts(coconuts):
    for coconut in coconuts:
        coconut.r.x+=coconut.vx
        coconut.r.y+=coconut.vy
        coconut.vy+=coconut.a
    

def draw_window(s1,s2,s3,kirbies,bullets,enemies, hits, dead_entities,coconuts,powerups,cages):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND_BOSS,(0,s3))
    WIN.blit(BACKGROUND,(0,s1))
    WIN.blit(BACKGROUND, (0,s2))
        

   # pygame.draw.rect(WIN,RED,kirby.r)
    for enemy in enemies:
        x,y=get_enemy_position_for_drawing(enemy)
        if y >= HEIGHT:
            enemies.remove(enemy)
        elif y<0 and s3==0:
            enemies.remove(enemy)
        else:    
            WIN.blit(enemy.photo,get_enemy_position_for_drawing(enemy))
        
    for kirby in kirbies:
        #pygame.draw.rect(WIN,RED,kirby.r)
        WIN.blit(kirby.photo,get_kirby_position_for_drawing(kirby))
    for coconut in coconuts:
        WIN.blit(coconut.photo,get_enemy_position_for_drawing(coconut))
        #pygame.draw.rect(WIN,ENEMY_COLORS["Coconut"],coconut.r)
    for bullet in bullets:
        #pygame.draw.rect(WIN,RED,bullet.r)
        WIN.blit(bullet.photo,get_bullet_position_for_drawing(bullet))
    for powerup in powerups:
        #pygame.draw.rect(WIN,ENEMY_COLORS["Powerup"],powerup.r)
        WIN.blit(powerup.photo,get_powerup_position_for_drawing(powerup))
    for cage in cages:
        #pygame.draw.rect(WIN,ENEMY_COLORS["Cage"],cage.r)
        WIN.blit(cage.photo,get_trappedkirby_position_for_drawing(cage))
    
    hits_text= HIT_FONT.render("Hits: "+ str(hits),1,(255,255,255))
    WIN.blit(hits_text,(WIDTH - hits_text.get_width() - 10,10))
    
    for dead_entity in dead_entities :
        POS=(dead_entity.r.x, dead_entity.r.y) #position du coin haut gauche de l'ennemi
        size=(dead_entity.r.width, dead_entity.r.height)
        explosionsize=(WIDTHKIRBY*2, HEIGHTKIRBY*2)
        explosionpos=(int(POS[0]-(explosionsize[0]-size[0])/2),int(POS[1]-(explosionsize[1]-size[1])/2))
    
        if dead_entity.type == "kirby" and dead_entity.photo!= None:
            WIN.blit(dead_entity.photo, explosionpos)
            
        elif dead_entity.type == "Coconut" or dead_entity.type=="trappedKirby":
            if dead_entity.photo is not None:
                WIN.blit(dead_entity.photo, explosionpos)

        else :
            if dead_entity.photo is not None:
                WIN.blit(dead_entity.photo, explosionpos)
            if dead_entity.frame<=2:
                dmgpos=get_enemy_position_for_drawing(dead_entity)
                WIN.blit(Enemy_DMG[dead_entity.type], dmgpos)
                
    
    pygame.display.update()



def draw_win(hits):
    WIN.fill(BLACK)
    WIN.blit(WINNER,(0,0))
    winner_text= HIT_FONT.render("Score: "+ str(hits),1,(255,215,0))
    WIN.blit(winner_text,(WIDTH/2.5,HEIGHT/2+30))
    pygame.display.update()
    pygame.time.delay(2000) 

def draw_lost():
    WIN.fill(BLACK)
    WIN.blit(GAME_OVER,(0,0))
    pygame.display.update()
    pygame.time.delay(2000)
    
def handle_keys(keys_pressed,kirby,i):
    if keys_pressed[pygame.K_UP]:
        kirby.deplacement.append(("U",i))
    if keys_pressed[pygame.K_DOWN]:
        kirby.deplacement.append(("D",i))
    if keys_pressed[pygame.K_LEFT]:
        kirby.deplacement.append(("L",i))
    if keys_pressed[pygame.K_RIGHT]:
        kirby.deplacement.append(("R",i))

def handle_keys_kirbies(keys_pressed,kirbies):
    for i in range(len(kirbies)):
        handle_keys(keys_pressed,kirbies[i],10*i)

def handle_bullets(bullets,kirbies):
    global bullet_level
    for bullet in bullets:
        bullet.r.y-=bullet.vel
        if bullet.r.y<0:
            bullets.remove(bullet)
    for kirby in kirbies:
        kirby.reload =(kirby.reload+1) % RELOAD_TIME
        if kirby.reload==0:
            bullets.append(Bullet(kirby.r.x+WIDTH_KIRBY//2-WIDTH_BULLET//2,kirby.r.y+HEIGHT_BULLET,bullet_level))

def handle_collision(bullets,enemies,kirbies,coconuts,dead_entities,powerups,cages):
    global bullet_level
    for enemy in enemies:

        for bullet in bullets:
            if enemy.r.colliderect(bullet.r):
                bullets.remove(bullet)
                enemy.health-=bullet.damage
                enemy.static_state=0
                enemy.frame=0
                enemy.state='dmg'
                if enemy.health<=0 and enemy in enemies:
                    dead_entity=[(enemy.r.width, enemy.r.height),(enemy.r.x, enemy.r.y), enemy.type]
                    dead_entities.append(DeadEntity(dead_entity))
                    enemies.remove(enemy)
                    EXPLOSION.play()
                    pygame.event.post(pygame.event.Event(ONE_HIT))


        for kirby in kirbies:
            if not kirby.summoned:
                if enemy.r.colliderect(kirby.r) and kirby in kirbies and enemy in enemies:
                    dead_entity=[(kirby.r.width, kirby.r.height),(kirby.r.x, kirby.r.y), "kirby"]
                    dead_entities.append(DeadEntity(dead_entity))
                    kirbies.remove(kirby)
                    enemies.remove(enemy)



    for coconut in coconuts:

        for bullet in bullets:
            if coconut.r.colliderect(bullet.r):
                bullets.remove(bullet)
                coconut.health-=bullet.damage
                if coconut.health<=0 and coconut in coconuts:
                    dead_entity=[(coconut.r.width, coconut.r.height),(coconut.r.x, coconut.r.y), coconut.type]
                    dead_entities.append(DeadEntity(dead_entity))
                    coconuts.remove(coconut)
                    EXPLOSION.play()

        for kirby in kirbies:
            if not kirby.summoned:
                if coconut.r.colliderect(kirby.r) and coconut in coconuts:
                    dead_entity=[(kirby.r.width, kirby.r.height),(kirby.r.x, kirby.r.y), "kirby"]
                    dead_entities.append(DeadEntity(dead_entity))
                    kirbies.remove(kirby)
                    coconuts.remove(coconut)
        
    for powerup in powerups:
        for kirby in kirbies:
            if not kirby.summoned:
                #print(powerup.x,powerup.y,kirby.x,kirby.y)
                if powerup.r.colliderect(kirby.r) and powerup in powerups:
                    powerups.remove(powerup)
                    bullet_level+=1
                    POWERUP.play()

    for cage in cages:

        for bullet in bullets:
            if cage.r.colliderect(bullet.r):
                bullets.remove(bullet)
                cage.health-=bullet.damage
                if cage.health<=0 and cage in cages:
                    dead_entity=[(cage.r.width, cage.r.height),(cage.r.x, cage.r.y), "trappedKirby"]
                    dead_entities.append(DeadEntity(dead_entity))
                    cages.remove(cage)
                    kirby_ajout=Kirby(cage.r.x,cage.r.y)
                    kirby_ajout.destination=(kirbies[0].r.x,kirbies[0].r.y)
                    kirby_ajout.summoned=True
                    kirbies.append(kirby_ajout)
                    EXPLOSION.play()
                    EXTRA_KIRBY.play()

        for kirby in kirbies:
            if not kirby.summoned:
                if cage.r.colliderect(kirby.r) and cage in cages:
                    dead_entity=[(kirby.r.width, kirby.r.height),(kirby.r.x, kirby.r.y), "kirby"]
                    dead_entities.append(DeadEntity(dead_entity))
                    kirbies.remove(kirby)
                    cages.remove(cage)

                    





def handle_position(kirby,kirbies):
    a=False
    if kirby.deplacement==[]:
        kirby.state="idle"
        return None

  #  if kirby.deplacement[0][1]<0:
   #     alpha=kirby.deplacement[0][1]
    #    for kirby_iter in kirbies:
     #       for i in range(len(kirby_iter.deplacement)):
      #              b,c=kirby_iter.deplacement[i]
       #             kirby_iter.deplacement[i]=b,c-alpha

    if kirby.deplacement[0][0]=="U" and kirby.deplacement[0][1]<=0:
        if kirby.r.y-VEL>=0:
            kirby.r.y-=VEL
        else:
            kirby.r.y=0
        kirby.deplacement.pop(0)
    if kirby.deplacement==[]:
        return None
    if kirby.deplacement[0][0]=="D" and kirby.deplacement[0][1]<=0:
        if kirby.r.y+HEIGHT_KIRBY+VEL<=HEIGHT:
            kirby.r.y+=VEL
        else :
            kirby.r.y=HEIGHT-HEIGHT_KIRBY
        kirby.deplacement.pop(0)
    if kirby.deplacement==[]:
        return None
    if kirby.deplacement[0][0]=="L" and kirby.deplacement[0][1]<=0:
        if kirby.r.x-VEL>=0:
            kirby.r.x-=VEL
        else:
            kirby.r.x=0
        kirby.state="left"
        a=True
        kirby.deplacement.pop(0)
    if kirby.deplacement==[]:
        return None
    if kirby.deplacement[0][0]=="R" and kirby.deplacement[0][1]<=0:
        if kirby.r.x+VEL+WIDTH_KIRBY<=WIDTH:
            kirby.r.x+=VEL
        else:
            kirby.r.x=WIDTH-WIDTH_KIRBY
        kirby.state="right"
        kirby.deplacement.pop(0)
        a=True
    if not a:
        kirby.state="idle"
    for i in range(len(kirby.deplacement)):
        kirby.deplacement[i]=(kirby.deplacement[i][0],kirby.deplacement[i][1]-1)


def kirbies_animation(kirbies):
    for kirby in kirbies:
        kirby_animation(kirby)

def handle_position_kirbies(kirbies):
    for kirby in kirbies:
        handle_position(kirby,kirbies)

def enemies_animation(enemies):
    for enemy in enemies:
        enemy_animation(enemy)


def handle_powerups_and_cages(powerups,cages):
    for powerup in powerups:
        powerup.x=powerup.x0+powerup.amplitude*sin(powerup.omega*powerup.t)
        powerup.t+=1
        powerup.r.x=powerup.x
        powerup.r.y+=powerup.vy

    for cage in cages:
        cage.x=cage.x0+cage.amplitude*sin(cage.omega*cage.t)
        cage.t+=1
        cage.r.x=cage.x
        cage.r.y+=cage.vy

def handle_summoned(kirbies):
    for kirby in kirbies:
        if kirby.summoned:
            #print(kirby.t)
            if kirby.t==-1:
                kirby.summoned=False
                
            else:
            
                kirby.r.x=(kirby.t*kirby.summon_position[0]+(10-kirby.t)*kirby.destination[0])/10
                kirby.r.y=(kirby.t*kirby.summon_position[1]+(10-kirby.t)*kirby.destination[1])/10
                kirby.t-=1

bullet_level=0

pause_button=Button(10,10,6,pause_img)

def main():
    """Cette fonction est la fonction principale qui fait exécuter le jeu, elle fait avancer le backgroung,
    et appelle les autres fonctions pour placer des ennemis, placer des Kirbys et le faire attaquer.
    Elle appelle aussi la fonction draw_window() pour dessiner la fenêtre sur l'écran"""
    
    global bullet_level
    global etat_deplacement
    run = True 
    s1 = 0               #ordonnée du premier backgroud qui apparaît
    s2 = -HEIGHT         #ordonnée du deuxième backgroud qui apparaît identique au 1er background mais ces 
                         #deux background vont tourner en boucle jusqu'à ce qu'on arrive au background du boss
    s3 = -HEIGHT         #ordonnée du background du boss qui arrive que à la fin
    main_menu=True
    restart_menu=False
    pause_menu=False
    hits=0
    cages=[]
    dead_entities=[]
    powerups=[]
    coconuts=[]
    enemies=[]
    clock = pygame.time.Clock()
    kirby=Kirby(WIDTH//2,HEIGHT-100)
    kirbies=[kirby]
    bullets=[]
    level= deepcopy(LEVEL1)
    frame=0




    while run:
        clock.tick(FPS)
        if main_menu == True:
            draw_main_menu()
            run,main_menu,restart_menu,pause_menu=state(run,main_menu,restart_menu,pause_menu)

        elif restart_menu==True:
            s1 = 0
            s2 = -HEIGHT
            s3 = -HEIGHT #ordonnée du fond du boss de fin (qu'on affiche pas tout de suite)
            main_menu=True
            restart_menu=False
            MUSIC.stop()
            hits=0
            cages=[]
            powerups=[]
            dead_entities=[]
            coconuts =[]
            enemies=[]
            clock = pygame.time.Clock()
            kirby=Kirby(WIDTH//2,HEIGHT-100)
            kirbies=[kirby]
            bullets=[]
            level=deepcopy(LEVEL1)
            frame=0
            bullet_level=0

            draw_main_menu()
            run,main_menu,restart_menu,pause_menu=state(run,main_menu,restart_menu,pause_menu)
        elif pause_menu==True:
            draw_main_menu()
            run,main_menu,restart_menu,pause_menu=state(run,main_menu,restart_menu,pause_menu)



        elif main_menu==False and restart_menu==False:
            if pause_menu==False:
                

            # draw_main_menu()
                if frame < 850:
                    if s2 == 0 and s1 > 0:
                        s1 = -HEIGHT
                    if s1 == 0 and s2 > 0:
                        s2 = -HEIGHT
                    
                    s1 += VEL_BG
                    s2 += VEL_BG
                    keys_pressed=pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            run = False
                            pygame.quit()
                        if event.type == pygame.KEYUP:
                            if  keys_pressed[pygame.K_m]:
                                if etat_deplacement==True:
                                    etat_deplacement=False
                                    for kirby in kirbies:
                                        kirby.state="idle"
                                else:
                                    etat_deplacement=True
                            if keys_pressed[pygame.K_n]:
                                kirbies.append(Kirby(kirbies[0].r.x,kirbies[0].r.y))

                        if event.type == ONE_HIT:
                            hits +=1
                            
                else:
                    if s1 > s2:
                        s3 = s2 - HEIGHT
                    if s2 > s1:
                        s3 = s1 - HEIGHT
                        
                    if s3 != 0:
                        s1 += VEL_BG
                        s2 += VEL_BG
                        s3 += VEL_BG
                        
                    keys_pressed=pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            run = False
                            pygame.quit()
                        if event.type == pygame.KEYUP:
                            if  keys_pressed[pygame.K_m]:
                                if etat_deplacement==True:
                                    etat_deplacement=False
                                    for kirby in kirbies:
                                        kirby.state="idle"
                                else:
                                    etat_deplacement=True
                            if keys_pressed[pygame.K_n]:
                                kirbies.append(Kirby(kirbies[0].r.x,kirbies[0].r.y))

                        if event.type == ONE_HIT:
                            hits +=1

                if len(enemies)==0 and s3==0:
                    restart_menu=True
                    main_menu=False
                    draw_win(hits)
                    
        
                if etat_deplacement:
                    handle_keys_kirbies(keys_pressed,kirbies)
                    handle_position_kirbies(kirbies)
                    
                if kirbies == []:
                    restart_menu=True
                    main_menu=False
                    draw_lost()
                
                
            # handle_keys_kirbies(keys_pressed,kirbies)
                for kirby in kirbies:
                    kirby_animation(kirby)
                for enemy in enemies:
                    enemy_animation(enemy)
                for coconut in coconuts:
                    enemy_animation(coconut)
                for bullet in bullets:
                    bullet_animation(bullet)
                for powerup in powerups:
                    powerup_animation(powerup)
                for cage in cages:
                    trappedkirby_animation(cage)
                dead_animation(dead_entities)
                if main_menu==False and restart_menu==False:
                    draw_window(s1,s2,s3,kirbies,bullets,enemies, hits, dead_entities,coconuts,powerups,cages)
                handle_bullets(bullets,kirbies)
                handle_level(level,frame,enemies,powerups,cages)

                
                handle_enemies(enemies,coconuts,s3)

                handle_collision(bullets,enemies,kirbies,coconuts, dead_entities,powerups,cages)
                handle_coconuts(coconuts)
                handle_powerups_and_cages(powerups,cages)
                handle_summoned(kirbies)

                if pause_button.draw():
                    pause_menu=True
                    restart_menu=False
                    main_menu=False
                    MUSIC.stop()
                
                frame+=1
            # handle_position_kirbies(kirbies)

        


        pygame.display.update()

if __name__ == "__main__":
    main()

def test():
    return 0



