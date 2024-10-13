import pygame
import os

#Constantes utilisées pour l'affichage
#Taille du sprite Kirby, indépendant de la taille du rectangle pygame utilisé pour représenter Kirbys
WIDTHKIRBY=80
HEIGHTKIRBY=80
#Paramètres de rafraîchissement
FPS=60
STATICFRAME=5
#=============================#

def enemy_size(enemy):
    """Donne la taille des sprites des ennemis de façon proportionnellle à la taille de Kirby
    
    Arguments : enemy (classe Enemy)
    
    Renvoie : tuple contenant la taille du sprite, relative à celle de Kirby
    
    """
    if enemy.type=='WaddleDee':
        if enemy.state=='dmg':
            #taille du sprite d'origine 24*44
            return (int(24/32*WIDTHKIRBY), int(44/32*HEIGHTKIRBY))
        else:
            #taille du sprite d'origine 29*44
            return (int(29/32*WIDTHKIRBY), int(44/32*HEIGHTKIRBY))
    if enemy.type=='BeanBon':
        if enemy.state=='angry' or enemy.state=='dmg':
            #taille du sprite d'origine 24*28
            return (int(24/32*WIDTHKIRBY), int(28/32*HEIGHTKIRBY))
        else :
            #taille du sprite d'origine 24*34
            return (int(24/32*WIDTHKIRBY), int(34/32*HEIGHTKIRBY))
    if enemy.type =='Coconut':
        #taille du sprite d'origine 32*16
        return (int(32/32*WIDTHKIRBY), int(16/32*HEIGHTKIRBY))
    if enemy.type=='LittleWoods':
        #taille du sprite d'origine 32*61
        return (int(32/32*WIDTHKIRBY), int(61/32*HEIGHTKIRBY))
    if enemy.type=='WhispyWoods':
        #taille du sprite d'origine 256*140
        return (int(256/32*WIDTHKIRBY), int(140/32*HEIGHTKIRBY))

#Import images, placées dans des listes s'il y a une animation, les listes sont référencées dans des dictionnaires pour les ennemis

#Kirby
KIRBY_IDLE=[]
KIRBY_LEFT=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Kirby', 'left.png')),(WIDTHKIRBY, HEIGHTKIRBY))
KIRBY_RIGHT=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Kirby', 'right.png')),(WIDTHKIRBY, HEIGHTKIRBY))
KIRBY_DMG=[]
for i in range(1,5):
    filename=str(i)+".png"
    KIRBY_IDLE.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Kirby', filename)),(WIDTHKIRBY, HEIGHTKIRBY)))
for i in range(1,11):
    IMAGESIZE=(int(72/32*WIDTHKIRBY), int(80/32*HEIGHTKIRBY))
    filename="dmg_"+str(i)+".png"
    KIRBY_DMG.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Kirby', filename)),IMAGESIZE))

#Waddle Dee
WADDLEDEE=[]
WADDLEDEE_DMG=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','WaddleDee', 'dmg.png')),(int(24/32*WIDTHKIRBY), int(44/32*HEIGHTKIRBY)))
for i in range(1,9):
    IMAGESIZE=(int(29/32*WIDTHKIRBY), int(44/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    WADDLEDEE.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','WaddleDee', filename)),IMAGESIZE))
 
#Explosion    
EXPLOSION=[]
for i in range (1,9):
    IMAGESIZE=(int(64/32*WIDTHKIRBY), int(64/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    EXPLOSION.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','Dwead', filename)),IMAGESIZE))

#BeanBon
BEANBON=[]
BEANBON_DMG=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','BeanBon', 'dmg.png')),(int(24/32*WIDTHKIRBY), int(28/32*HEIGHTKIRBY)))
BEANBON_ANGRY=[]
for i in range (1,6):
    IMAGESIZE=(int(24/32*WIDTHKIRBY), int(34/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    BEANBON.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','BeanBon', filename)),IMAGESIZE))
for i in range (1,3):
    IMAGESIZE=(int(24/32*WIDTHKIRBY), int(28/32*HEIGHTKIRBY))
    filename="angry_"+str(i)+".png"
    BEANBON_ANGRY.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','BeanBon', filename)),IMAGESIZE))

#Coconut
COCONUT=[]
for i in range (1,7):
    IMAGESIZE=(int(32/32*WIDTHKIRBY), int(16/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    COCONUT.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','Coconut', filename)),IMAGESIZE))
    
#LittleWoods
LITTLEWOODS=[]
LITTLEWOODS_DMG=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','LittleWoods', 'dmg.png')),(int(32/32*WIDTHKIRBY), int(61/32*HEIGHTKIRBY)))
for i in range (1,7):
    IMAGESIZE=(int(32/32*WIDTHKIRBY), int(61/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    LITTLEWOODS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','LittleWoods', filename)),IMAGESIZE))

#WhispyWoods
WHISPYWOODS=[]
WHISPYWOODS_DMG=pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','WhispyWoods', 'dmg.png')),(int(256/32*WIDTHKIRBY), int(140/32*HEIGHTKIRBY)))
for i in range (1,15):
    IMAGESIZE=(int(256/32*WIDTHKIRBY), int(140/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    WHISPYWOODS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Enemies','WhispyWoods', filename)),IMAGESIZE))

#PowerUp
POWERUP=[]
for i in range(1,8):
    #Taille du sprite 20*18
    IMAGESIZE=(int(20/32*WIDTHKIRBY), int(18/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    POWERUP.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bonus','PowerUp', filename)),IMAGESIZE))
    
#TrappedKirby
TRAPPEDKIRBY=[]
for i in range(1,8):
    #Taille du sprite 33*36
    IMAGESIZE=(int(33/32*WIDTHKIRBY), int(36/32*HEIGHTKIRBY))
    filename=str(i)+".png"
    TRAPPEDKIRBY.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bonus','TrappedKirby', filename)),IMAGESIZE))
    
#Bullets
RED_BULLETS=[]
GREEN_BULLETS=[]
YELLOW_BULLETS=[]

for i in range (1,5):
    #Taille du sprite 16*32
    IMAGESIZE=(int(16/32*WIDTHKIRBY), HEIGHTKIRBY)
    filename=str(i)+".png"
    RED_BULLETS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bullets','Red', filename)),IMAGESIZE))
    GREEN_BULLETS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bullets','Green', filename)),IMAGESIZE))
    YELLOW_BULLETS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Bullets','Yellow', filename)),IMAGESIZE))
      
    
#Fonctions permettant d'obtenir les positions pour dessiner les sprites
def get_kirby_position_for_drawing(kirby):
    """Cette fonction permet d'obtenir les coordonées pour dessiner le Kirby au centre du rectangle
    
    Arguments : kirby (classe Kirby)
    
    Renvoie : tuple contenant les coordonées du coin haut gauche pour dessiner les sprites au centre du rectangle pygame
    
    """
    rect_size=(kirby.r.width, kirby.r.height)
    if kirby.state=='dmg':
        #Taille du sprite : int(72/32*WIDTHKIRBY) * int(80/32*HEIGHTKIRBY)
        sprite_size=(int(72/32*WIDTHKIRBY), int(80/32*HEIGHTKIRBY))
    else :
        #Taille du sprite : WIDTHKIRBY*HEIGHTKIRBY
        sprite_size=(WIDTHKIRBY, HEIGHTKIRBY)
    X=kirby.r.x-(sprite_size[0]-rect_size[0])/2
    Y=kirby.r.y-(sprite_size[1]-rect_size[1])/2
    return (int(X),int(Y))

def get_enemy_position_for_drawing(enemy):
    """Cette fonction permet d'obtenir les coordonées pour dessiner l'ennemi au centre du rectangle pygame
    
    Arguments : enemy (classe Enemy)
    
    Renvoie : tuple contenant les coordonées du coin haut gauche pour dessiner les sprites au centre du rectangle pygame
    
    """
    rect_size=(enemy.r.width, enemy.r.height)
    sprite_size=enemy_size(enemy)
    X=enemy.r.x-(sprite_size[0]-rect_size[0])/2
    Y=enemy.r.y-(sprite_size[1]-rect_size[1])/2
    return (int(X),int(Y))

def get_bullet_position_for_drawing(bullet):
    """Cette fonction permet d'obtenir les coordonées pour dessiner les bullets
    
    Arguments : bullet (classe Bullet)
    
    Renvoie : tuple contenant les coordonées du coin haut gauche pour dessiner les sprites centrés horizontalement seulement avec le rectangle pygame
    
    """
    rect_size=(bullet.r.width, bullet.r.height)
    sprite_size=(int(16/32*WIDTHKIRBY), HEIGHTKIRBY)
    X=bullet.r.x-(sprite_size[0]-rect_size[0])/2
    Y=bullet.r.y-(sprite_size[1]-rect_size[1])*2/7
    return (int(X),int(Y))

def get_powerup_position_for_drawing(powerup):
    """Cette fonction permet d'obtenir les coordonées pour dessiner le powerup au centre du rectangle pygame
    
    Arguments : powerup (classe Powerup)
    
    Renvoie : tuple contenant les coordonées du coin haut gauche pour dessiner les sprites au centre du rectangle pygame
    
    """
    rect_size=(powerup.r.width, powerup.r.height)
    sprite_size=(int(20/32*WIDTHKIRBY), int(18/32*HEIGHTKIRBY))
    X=powerup.r.x-(sprite_size[0]-rect_size[0])/2
    Y=powerup.r.y-(sprite_size[1]-rect_size[1])/2
    return (int(X),int(Y))

def get_trappedkirby_position_for_drawing(trappedkirby):
    """Cette fonction permet d'obtenir les coordonées pour dessiner la cage au centre du rectangle pygame
    
    Arguments : trappedkirby (classe Cage)
    
    Renvoie : tuple contenant les coordonées du coin haut gauche pour dessiner les sprites au centre du rectangle pygame
    
    """
    rect_size=(trappedkirby.r.width, trappedkirby.r.height)
    sprite_size=(int(33/32*WIDTHKIRBY), int(36/32*HEIGHTKIRBY))
    X=trappedkirby.r.x-(sprite_size[0]-rect_size[0])/2
    Y=trappedkirby.r.y-(sprite_size[1]-rect_size[1])/2
    return (int(X),int(Y))


#Dictionnaires contenant les listes de sprites
#DMG : 1 seul sprite (pas dans une liste !)
Enemy_DMG={"WaddleDee" : WADDLEDEE_DMG, "BeanBon" : BEANBON_DMG, "LittleWoods" : LITTLEWOODS_DMG, "WhispyWoods": WHISPYWOODS_DMG}
Enemy_IDLE={"WaddleDee" : WADDLEDEE, "BeanBon" : BEANBON, "Coconut" : COCONUT, "LittleWoods" : LITTLEWOODS, "WhispyWoods": WHISPYWOODS}
Enemy_ANGRY={"BeanBon" : BEANBON_ANGRY}

#=============================#

#Fonctions d'animation
def play_kirby_idle(kirby):
    """Cette fonction change le sprite de kirby en idle toutes les STATICFRAME frames
    
    Arguments : kirby (classe Kirby)
    
    Renvoie : None
    
    Agit par effet de bord sur l'objet kirby en mettant à jour l'attribut photo
    
    """
    kirby.staticframe+=1
    if kirby.staticframe>=STATICFRAME:
        kirby.staticframe=0
        kirby.frame+=1
    if kirby.frame>=len(KIRBY_IDLE):
        kirby.frame=0
    kirby.photo=KIRBY_IDLE[kirby.frame]

        
def play_enemy(enemy):
    """Cette fonction change la photo de l'ennemi selon son état
    
    Arguments : enemy (classe Enemy)
    
    Renvoie : None
    
    Agit par effet de bord sur l'objet enemy en mettant à jour l'attribut photo
    
    """
    enemy.staticframe+=1
    
    if enemy.state=='dmg':
        if enemy.staticframe>=STATICFRAME:
            enemy.staticframe=0
            enemy.frame+=1
        if enemy.frame>=2:
            enemy.frame=0
            enemy.state='idle'
        enemy.photo=Enemy_DMG[enemy.type]
    
    elif enemy.state=='idle':
        if enemy.staticframe>=STATICFRAME:
            enemy.staticframe=0
            enemy.frame+=1
        if enemy.frame>=len(Enemy_IDLE[enemy.type]):
            enemy.frame=0 
        enemy.photo=Enemy_IDLE[enemy.type][enemy.frame]
    
    elif enemy.state=='angry':
        if enemy.staticframe>=STATICFRAME:
            enemy.staticframe=0
            enemy.frame+=1
        if enemy.frame>=len(Enemy_ANGRY[enemy.type]):
            enemy.frame=0
            enemy.state='idle'
        enemy.photo=Enemy_ANGRY[enemy.type][enemy.frame]


def play_dead(dead_entities):
    """Cette fonction change la photo de l'ennemi selon son entité dead pour l'animation
    
    Arguments : dead_entities (liste d'éléments de la classe DeadEntities)
    
    Renvoie : None
    
    Agit par effet de bord sur les objets de dead_entities en mettant à jour l'attribut photo
    
    """
    for dead_entity in dead_entities :
        if dead_entity.type == "kirby":
            animation_length=len(KIRBY_DMG)-1
        else:
            animation_length=len(EXPLOSION)-1
        
        dead_entity.staticframe+=1
        if dead_entity.staticframe>=STATICFRAME:
            dead_entity.staticframe=0
            dead_entity.frame+=1
        if dead_entity.frame>=animation_length:
            dead_entity.frame=animation_length
            dead_entities.remove(dead_entity)
            
        if dead_entity.type == "kirby":
            dead_entity.photo=KIRBY_DMG[dead_entity.frame]
        else:
            dead_entity.photo=EXPLOSION[dead_entity.frame]

def play_bullet(bullet):
    """Cette fonction change la photo d'un bullet pour l'animation selon leur niveau
    
    Arguments : bullet (classe Bullet)
    
    Renvoie : None
    
    Agit par effet de bord sur l'objet enemy en mettant à jour l'attribut photo
    
    """
    bullet.staticframe+=1
    if bullet.staticframe>=STATICFRAME:
        bullet.staticframe=0
        bullet.frame+=1
    if bullet.frame>=4:
        bullet.frame=0
        
    if bullet.level==0:    
        bullet.photo=GREEN_BULLETS[bullet.frame]
    if bullet.level==1:    
        bullet.photo=YELLOW_BULLETS[bullet.frame]
    if bullet.level>=2:    
        bullet.photo=RED_BULLETS[bullet.frame]
    
def play_powerup(powerup):
    """Cette fonction change le sprite du powerup toutes les STATICFRAME frames
    
    Arguments : powerup (classe Powerup)
    
    Renvoie : None
    
    Agit par effet de bord sur l'objet powerup en mettant à jour l'attribut photo
    
    """
    powerup.staticframe+=1
    if powerup.staticframe>=STATICFRAME:
        powerup.staticframe=0
        powerup.frame+=1
    if powerup.frame>=len(POWERUP):
        powerup.frame=0
    powerup.photo=POWERUP[powerup.frame]
    
def play_trappedkirby(trappedkirby):
    """Cette fonction change le sprite de la cage toutes les STATICFRAME frames
    
    Arguments : trappedkirby (classe Cage)
    
    Renvoie : None
    
    Agit par effet de bord sur l'objet trappedkirby en mettant à jour l'attribut photo
    
    """
    trappedkirby.staticframe+=1
    if trappedkirby.staticframe>=STATICFRAME:
        trappedkirby.staticframe=0
        trappedkirby.frame+=1
    if trappedkirby.frame>=len(TRAPPEDKIRBY):
        trappedkirby.frame=0
    trappedkirby.photo=TRAPPEDKIRBY[trappedkirby.frame]



#=============================#

#Fonctions à appeler pour animer

def enemy_animation(enemy):
    """Cette fonction met à jour la photo pour faire une animation d'UN ennemi
    
    Arguments : enemy (classe Enemy)
    
    Renvoie : None
    
    A appeler pour chaque ennemi
    Utilise les fonctions play_enemy et play_enemy_explosion
    
    """
    play_enemy(enemy)


def kirby_animation(kirby):
    """Cette fonction met à jour la photo pour faire une animation de Kirby
    
    
    Arguments : kirby (classe Kirby)
    
    Renvoie : None
    
    A appeler pour chaque Kirby
    Utilise les fonctions play_kirby_idle et play_kirby_dmg
    
    """
    if kirby.state=='idle':
        play_kirby_idle(kirby)
    elif kirby.state=='left':
        kirby.photo=KIRBY_LEFT
    elif kirby.state=='right':
        kirby.photo=KIRBY_RIGHT


def dead_animation(dead_entities):
    """Cette fonction met à jour la photo pour faire une animation d'explosion
    
    
    Arguments : enemy dead_entities (liste d'éléments de la classe DeadEntities)
    
    Renvoie : None
    
    Utilise la fonction play_dead
    
    """
    play_dead(dead_entities)
    
def bullet_animation(bullet):
    """Cette fonction met à jour la photo pour faire une animation d'un bullet
    
    
    Arguments : bullet (classe Bullet)
    
    Renvoie : None
    
    A appeler pour chaque bullet
    Utilise la fonction play_bullet
    
    """
    play_bullet(bullet)
    
def powerup_animation(powerup):
    """Cette fonction met à jour la photo pour faire une animation d'un powerup
    
    
    Arguments : powerup (classe Powerup)
    
    Renvoie : None
    
    A appeler pour chaque powerup
    Utilise la fonction play_powerup
    
    """
    play_powerup(powerup)
    
def trappedkirby_animation(trappedkirby):
    """Cette fonction met à jour la photo pour faire une animation d'un trappedkirby
    
    
    Arguments : trappedkirby (classe Cage)
    
    Renvoie : None
    
    A appeler pour chaque trappedkirby
    Utilise la fonction play_trappedkirby
    
    """
    play_trappedkirby(trappedkirby)

#=============================#


#Environnement de test

WIDTH=450
HEIGHT=900

#TESTBACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join('cm_gr20','Assets', 'Background', 'Background.png')),(WIDTH, HEIGHT))

def draw_kirby(i):
    """Fonction de test pour vérifier l'animation"""
    WIN.blit(KIRBY_IDLE[i], (100, 750)) 
    

def draw_kirby_dmg(k):
    """Fonction de test pour vérifier l'animation"""
    WIN.blit(KIRBY_DMG[k], (250, 700)) 
    
def draw_enemy(l):
    WIN.blit(WADDLEDEE[l], (150, 300))
    
def draw_window(i,k,l):
    """Fonction de test"""
    #WIN.blit(TESTBACKGROUND, (0,0))
    draw_kirby(i)
    draw_kirby_dmg(k)
    draw_enemy(l)
    pygame.display.update()

def main():
    """Environnement de test"""
    global WIN
    WIN=pygame.display.set_mode((WIDTH, HEIGHT))
    clock=pygame.time.Clock()
    run=True
    i=0
    j=0
    k=0
    l=0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        draw_window(i,k,l)
        j+=1
        if j>=STATICFRAME:
            i+=1
            k+=1
            l+=1
            j=0

        if i>=4:
            i=0
        if k>=10:
            k=9
        if l>=8:
            l=0
    pygame.quit()
    
if __name__ == '__main__':
    main()
    
#=============================#