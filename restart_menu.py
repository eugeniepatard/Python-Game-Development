import pygame as pygame
from kirby_game import *
import os

BLACK=(0,0,0)
restart_img = pygame.image.load(os.path.join('Assets', "restart_btn.png"))
exit_img = pygame.image.load(os.path.join('Assets', 'exit_btn.png'))
BACKGROUND= pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background_main_menu.png')),(WIDTH,HEIGHT))

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

restart_button = Button(WIDTH // 2 - 350, HEIGHT // 2,20, restart_img)
exit_button = Button(WIDTH // 2 + 50, HEIGHT // 2,20, exit_img)

def state_2(run,main_menu,restart_menu):
    if exit_button.draw(WIN):
        run=False
        pygame.quit()
        
    if restart_button.draw(WIN):
        restart_menu =False
        main_menu = False
    return run, restart_menu,main_menu


def draw_restart_menu():
    WIN.fill(BLACK)
    WIN.blit(BACKGROUND,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

