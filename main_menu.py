import pygame as pygame
from kirby_game import*
import os
pygame.init()
WIDTH,HEIGHT=700,850
MUSIC = pygame.mixer.Sound("Assets/Sound/Music.mp3")
MUSIC.set_volume(0.65)
BLACK=(0,0,0)
start_img = pygame.transform.scale(pygame.image.load("Assets/start_btn.png"),(WIDTH/3,HEIGHT/6))
exit_img = pygame.transform.scale(pygame.image.load("Assets/exit_btn.png"),(WIDTH/3,HEIGHT/6))
restartt_img=pygame.image.load(os.path.join("Assets",'restart_btn.png'))
restart_img=pygame.transform.scale(restartt_img,(WIDTH/3,HEIGHT/6))



BACKGROUND= pygame.transform.scale(pygame.image.load("Assets/background_main_menu.png"),(WIDTH,HEIGHT))

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





start_button = Button(WIDTH // 2 - 300, HEIGHT // 2,6, start_img)
exit_button = Button(WIDTH // 2 + 60, HEIGHT // 2,6, exit_img)
restart_button=Button(WIDTH // 2 - 300, HEIGHT // 2,6,restart_img)

#return state of boolean variables run,main_menu,restart_menu,pause_menu and draw the buttons#
def state(run,main_menu,restart_menu,pause_menu):
    if exit_button.draw():
        run=False
        
    if main_menu==True:
        if start_button.draw():
            main_menu=False
            restart_menu=False
            pause_menu=False
            MUSIC.play()
            
    if restart_menu==True:
        if  start_button.draw():
            main_menu=False
            restart_menu=False
            pause_menu=False
            
    if pause_menu==True:
        if restart_button.draw():
            pause_menu=False
            main_menu=False
            restart_menu=False
            MUSIC.play()
            


    return run,main_menu,restart_menu,pause_menu

def draw_main_menu():
    
    
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND,(0,0))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
