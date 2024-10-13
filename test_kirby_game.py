from kirby_game import *
from pygame import *



def test_handle_keys():

    kirby1=Kirby(WIDTH/2,HEIGHT/2)
    kirby2=Kirby(WIDTH/2,HEIGHT/2)
    kirby1.deplacement=[]
    kirby2.deplacement=[]

    keys_pressed_1={}
    keys_pressed_1[pygame.K_UP]=True
    keys_pressed_1[pygame.K_DOWN]=False
    keys_pressed_1[pygame.K_LEFT]=False
    keys_pressed_1[pygame.K_RIGHT]=False
    handle_keys(keys_pressed_1,kirby1,0)

    keys_pressed_2={}
    keys_pressed_2[pygame.K_UP]=False
    keys_pressed_2[pygame.K_DOWN]=False
    keys_pressed_2[pygame.K_LEFT]=True
    keys_pressed_2[pygame.K_RIGHT]=True
    handle_keys(keys_pressed_2,kirby2,0)

    assert kirby1.deplacement==[("U",0)]
    assert kirby2.deplacement==[("L",0),("R",0)]

test_handle_keys()



def test_handle_enemies():
    enemy1=Enemy(0,0,"WaddleDee")
    enemy1.r.y=0
    enemy1.vel=0
    enemy2=Enemy(10,0,"WaddleDee")
    enemy2.vel=10
    s3=0
    enemies=[enemy1,enemy2]
    coconuts=[]
    handle_enemies(enemies,coconuts,s3)

    assert (enemy1.r.y==0) and (enemy2.r.y==10)

test_handle_enemies()



def test_handle_enemies():
    enemy1=Enemy(0,0,"BeanBon")
    enemy1.reload=5+RELOAD_COCONUT
    enemies=[enemy1]
    coconuts=[]
    s3=0
    handle_enemies(enemies,coconuts,s3)
    assert enemies[0].frame ==0 and enemies[0].state=='angry'

test_handle_enemies()




def test_handle_coconuts():
    coconuts=[]
    coconut_1=Coconut(10,10)
    coconut_1.r.x=0
    coconut_1.r.y=0
    coconut_1.vx=0
    coconut_1.vy=10
    coconut_1.a=0
    coconuts.append(coconut_1)
    handle_coconuts(coconuts)
    assert (coconuts[0].r.x==0) and (coconuts[0].r.y==10) and (coconuts[0].vy==10)

test_handle_coconuts()






def test_handle_bullets():

    bullet_1=Bullet(0,HEIGHT,0)
    bullet_2=Bullet(WIDTH/2,HEIGHT/2,0)
    bullet_3=Bullet(WIDTH/2,-10,0)
    bullets=[bullet_1,bullet_2,bullet_3]
    bullets_2=[bullet_1,bullet_2]
    kirby_1=Kirby(0,0)
    kirby_1.reload=2
    kirbies=[kirby_1]
    handle_bullets(bullets,kirbies)
    assert bullets == bullets_2

test_handle_bullets()


def test_handle_position():
    kirbies=[]
    kirby_1=Kirby(0,0)
    kirby_1.deplacement=[]
    kirbies.append(kirby_1)
    t1=handle_position(kirby_1,kirbies)
    kirby_2=Kirby(10,10)
    kirby_2.deplacement=[("U",0)]
    kirbies.append(kirby_2)
    t2=handle_position(kirby_2,kirbies)

    
    assert (t1==None) and (t2==None)

test_handle_position()
