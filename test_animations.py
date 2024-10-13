from animations import *
from kirby_game import *





def test_enemy_size():
    enemy_1=Enemy(0,0,"WaddleDee")
    enemy_2=Enemy(0,0,"Coconut")
    enemy_1.state='dmg'
    (x1,y1)=enemy_size(enemy_1)
    (x2,y2)=enemy_size(enemy_2)
    assert (x1,y1)==(int(24/32*WIDTHKIRBY),int(44/32*HEIGHTKIRBY))
    assert (x2,y2)==(int(32/32*WIDTHKIRBY), int(16/32*HEIGHTKIRBY))

test_enemy_size()



def test_get_kirby_position_for_drawing():
    kirby=Kirby(0,0)
    kirby.r.x=0
    kirby.r.y=0
    kirby.r.width=int(72/32*WIDTHKIRBY)
    kirby.r.height=int(80/32*HEIGHTKIRBY)
    kirby.state='dmg'
    (X,Y)= get_kirby_position_for_drawing(kirby)
    assert (X,Y) == (0,0)

test_get_kirby_position_for_drawing()



def test_get_enemy_position_for_drawing():
    enemy=Enemy(0,0,"WaddleDee")
    enemy.state='dmg'
    enemy.r.width,enemy.r.height=int(72/32*WIDTHKIRBY), int(80/32*HEIGHTKIRBY)
    X,Y=get_enemy_position_for_drawing(enemy)
    assert (X,Y)==(60,45)


test_get_enemy_position_for_drawing()




def test_play_kirby_idle():
    kirby=Kirby(0,0)
    kirby.frame=0
    kirby.staticframe=STATICFRAME
    play_kirby_idle(kirby)

    assert (kirby.staticframe==0) and (kirby.photo==KIRBY_IDLE[1])

test_play_kirby_idle()



def test_play_enemy():
    enemy=Enemy(0,0,"BeanBon")
    enemy.frame=0
    enemy.state='idle'
    enemy.staticframe=STATICFRAME
    play_enemy(enemy)

    assert (enemy.staticframe==0)

test_play_enemy()



def test_play_dead():
    dead_entities=[DeadEntity([(int(32/32*WIDTHKIRBY), int(61/32*HEIGHTKIRBY)),(0,0), 'kirby'])]
    dead_entities[0].frame=len(KIRBY_DMG)
    play_dead(dead_entities)

    assert dead_entities==[]

test_play_dead()    



def test_kirby_animation():
    kirby1=Kirby(0,0)
    kirby1.state='left'
    kirby2=Kirby(10,10)
    kirby2.state='right'
    kirby_animation(kirby1)
    kirby_animation(kirby2)
    assert (kirby1.photo==KIRBY_LEFT) and (kirby2.photo==KIRBY_RIGHT)

test_kirby_animation()


def test_get_bullet_position_for_drawing():
    bullet=Bullet(0,0,0)
    bullet.r.width,bullet.r.height=int(16/32*WIDTHKIRBY), HEIGHTKIRBY
    X,Y=get_bullet_position_for_drawing(bullet)
    assert (X,Y)==(0,0)

test_get_bullet_position_for_drawing()


def test_get_trappedkirby_position_for_drawing():
    kirby=Kirby(0,0)
    kirby.r.width,kirby.r.height=int(33/32*WIDTHKIRBY), int(36/32*HEIGHTKIRBY)
    X,Y=get_trappedkirby_position_for_drawing(kirby)
    assert (X,Y)==(0,0)

test_get_trappedkirby_position_for_drawing()

def test_enemy_animation():
    enemy=Enemy(0,0,"BeanBon")
    enemy.frame=0
    enemy.state='idle'
    enemy.staticframe=STATICFRAME
    enemy_animation(enemy)
    assert (enemy.staticframe==0)

test_enemy_animation()

def test_dead_animation():
    dead_entities=[DeadEntity([(int(32/32*WIDTHKIRBY), int(61/32*HEIGHTKIRBY)),(0,0), 'kirby'])]
    dead_entities[0].frame=len(KIRBY_DMG)
    dead_animation(dead_entities)

    assert dead_entities==[]

test_dead_animation()


def test_play_trappedkirby():
    kirby=Kirby(450,700)
    kirby.frame=0
    kirby.staticframe=STATICFRAME
    play_trappedkirby(kirby)

    assert kirby.frame==1
test_play_trappedkirby()


def test_play_powerup():
    powerup=Powerup(0,0)
    powerup.staticframe=STATICFRAME
    powerup.frame=0
    play_powerup(powerup)
    assert powerup.frame==1
test_play_powerup()


def test_trappedkirby_animation():
    kirby=Kirby(350,350)
    kirby.frame=0
    kirby.staticframe=STATICFRAME
    trappedkirby_animation(kirby)

    assert kirby.frame==1
test_play_trappedkirby()


def test_powerup_animation():
    powerup=Powerup(0,0)
    powerup.staticframe=STATICFRAME
    powerup.frame=0
    powerup_animation(powerup)
    assert powerup.frame==1
test_powerup_animation()


def test_play_bullet():
    bullet1=Bullet(WIDTH/2,HEIGHT/2,0)
    bullet2=Bullet(0,0,0)
    bullet1.frame=4
    bullet2.staticframe=STATICFRAME
    bullet2.frame=1
    play_bullet(bullet1)
    play_bullet(bullet2)
    assert bullet1.frame==0 and bullet2.frame==2
test_play_bullet()

def test_bullet_animation():
    bullet1=Bullet(WIDTH/4,HEIGHT/20,0)
    bullet2=Bullet(10,20,0)
    bullet1.frame=4
    bullet2.staticframe=STATICFRAME
    bullet2.frame=2
    bullet_animation(bullet1)
    bullet_animation(bullet2)
    assert bullet1.frame==0 and bullet2.frame==3
test_bullet_animation()
