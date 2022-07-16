import pygame
from random import randint

import time

pygame.init()

class Core:
    def __init__(self):
        self.window_width = 500
        self.window_heigth = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_heigth))
        pygame.display.set_caption("Kare Yakala")
        self.clock = pygame.time.Clock()

        self.enemy = pygame.image.load("img/enemy.png")
        self.background = pygame.image.load("img/background.png")

        self.player = pygame.image.load("img/player.png")
        self.player_X = 250
        self.player_Y = 600

        self.spam_normal1 = False
        self.spam_normal2 = True
        self.normal_animation_speed = 4
        self.normal1_animation_counter = 0
        self.normal2_animation_counter = 0

        self.normal_free = [pygame.image.load("img/normal-cell/normal-free/normal-free-1.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-2.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-3.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-4.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-5.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-6.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-7.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-8.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-9.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-10.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-11.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-12.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-13.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-14.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-15.png"),
                            pygame.image.load("img/normal-cell/normal-free/normal-free-16.png")]

        self.normal_spam_animation_counter = 0
        self.normal_spam = [pygame.image.load("img/normal-cell/normal-spam/normal-spam-1.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-2.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-3.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-4.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-5.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-6.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-7.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-8.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-9.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-10.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-11.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-12.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-13.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-14.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-15.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-16.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-17.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-18.png"),
                            pygame.image.load("img/normal-cell/normal-spam/normal-spam-19.png")]

        self.spam_tumor1 = False
        self.spam_tumor2 = True
        self.tumor_animation_speed = 4
        self.tumor1_animation_counter = 0
        self.tumor2_animation_counter = 0
        self.tumor_spam_animation_counter = 0

        self.tumor_free = [pygame.image.load("img/tumor-cell/tumor-free/tumor-free-1.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-2.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-3.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-4.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-5.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-6.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-7.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-8.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-9.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-10.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-11.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-12.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-13.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-14.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-15.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-16.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-17.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-18.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-19.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-20.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-21.png"),
                           pygame.image.load("img/tumor-cell/tumor-free/tumor-free-22.png")]

        self.tumor_spam = [pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-1.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-2.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-3.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-4.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-5.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-6.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-7.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-8.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-9.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-10.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-11.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-12.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-13.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-14.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-15.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-16.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-17.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-18.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-19.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-20.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-21.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-22.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-23.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-24.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-25.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-26.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-27.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-28.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-29.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-30.png"),
                           pygame.image.load("img/tumor-cell/tumor-spam/tumor-spam-31.png")]

        self.protein = pygame.image.load("img/protein/protein2.png")
        self.neoantijen = pygame.image.load("img/protein/neoantijen2.png")
        self.protein_liste = [] # [[x1,y1], [x2,y2], ..., [x5,y5]]
        self.neoantijen_liste = [] # [[x1,y1], [x2,y2], ..., [x5,y5]]
        
    def normal_spam_free_animation(self, coo1, coo2):
        
        
        if self.spam_normal1:
            if self.normal1_animation_counter == int(len(self.normal_spam)/2) * self.normal_animation_speed:
                self.protein_liste.append([coo1 + 35,coo2 + 35])
            
            if self.normal1_animation_counter == len(self.normal_spam) * self.normal_animation_speed:
                self.normal1_animation_counter = 0
                self.spam_normal1 = False
                
                
            self.window.blit(self.normal_spam[int(self.normal1_animation_counter // self.normal_animation_speed)],(coo1, coo2))

        elif self.normal_spam_animation_counter == 0 and len(self.protein_liste) < 5:
            if self.normal1_animation_counter == len(self.normal_free) * self.normal_animation_speed:
                self.normal1_animation_counter = 0
                self.spam_normal1 = True

            self.window.blit(self.normal_free[int(self.normal1_animation_counter // self.normal_animation_speed)],(coo1, coo2))
        else:
            if self.normal1_animation_counter == len(self.normal_free) * self.normal_animation_speed:
                self.normal1_animation_counter = 0
                
            self.window.blit(self.normal_free[int(self.normal1_animation_counter // self.normal_animation_speed)],(coo1, coo2))

        self.normal1_animation_counter += 1

        if self.spam_normal2:
            if self.normal2_animation_counter == int(len(self.normal_spam)/2) * self.normal_animation_speed:
                self.protein_liste.append([coo1 + 285,coo2 + 35])
                
            if self.normal2_animation_counter == len(self.normal_spam) * self.normal_animation_speed:
                self.normal2_animation_counter = 0
                self.spam_normal2 = False
                
            self.window.blit(self.normal_spam[int(self.normal2_animation_counter // self.normal_animation_speed)],(coo1 + 250, coo2))

        elif self.normal_spam_animation_counter == 0 and len(self.protein_liste) < 5:
            if self.normal2_animation_counter == len(self.normal_free) * self.normal_animation_speed:
                self.normal2_animation_counter = 0
                self.spam_normal2 = True

            self.window.blit(self.normal_free[int(self.normal2_animation_counter // self.normal_animation_speed)],(coo1+ 250, coo2))
        else:
            if self.normal2_animation_counter == len(self.normal_free) * self.normal_animation_speed:
                  self.normal2_animation_counter = 0
                  
            self.window.blit(self.normal_free[int(self.normal2_animation_counter // self.normal_animation_speed)],(coo1+ 250, coo2))

        self.normal2_animation_counter += 1

        if self.spam_tumor1:
            if self.tumor1_animation_counter == int(len(self.tumor_spam)/2) * self.tumor_animation_speed:
                self.neoantijen_liste.append([coo1 + 165,coo2 + 30])
                
            if self.tumor1_animation_counter == len(self.tumor_spam) * self.tumor_animation_speed:
                self.tumor1_animation_counter = 0
                self.spam_tumor1 = False
                
            self.window.blit(self.tumor_spam[int(self.tumor1_animation_counter // self.tumor_animation_speed)],(coo1 + 140, coo2))

        elif self.tumor_spam_animation_counter == 0 and len(self.neoantijen_liste) < 5:
            if self.tumor1_animation_counter == len(self.tumor_free) * self.tumor_animation_speed:
                self.tumor1_animation_counter = 0
                self.spam_tumor1 = True

            self.window.blit(self.tumor_free[int(self.tumor1_animation_counter // self.tumor_animation_speed)],(coo1 + 140, coo2))
        else:
            if self.tumor1_animation_counter == len(self.tumor_free) * self.tumor_animation_speed:
                self.tumor1_animation_counter = 0
                
            self.window.blit(self.tumor_free[int(self.tumor1_animation_counter // self.tumor_animation_speed)],(coo1 + 140, coo2))
        
        self.tumor1_animation_counter += 1

        if self.spam_tumor2:
            if self.tumor2_animation_counter == int(len(self.tumor_spam)/2) * self.tumor_animation_speed:
                self.neoantijen_liste.append([coo1 + 415,coo2 + 30])
                
            if self.tumor2_animation_counter == len(self.tumor_spam) * self.tumor_animation_speed:
                self.tumor2_animation_counter = 0
                self.spam_tumor2 = False
                
            self.window.blit(self.tumor_spam[int(self.tumor2_animation_counter // self.tumor_animation_speed)],(coo1 + 390, coo2))

        elif self.tumor_spam_animation_counter == 0 and len(self.neoantijen_liste) < 5:
            if self.tumor2_animation_counter == len(self.tumor_free) * self.tumor_animation_speed:
                self.tumor2_animation_counter = 0
                self.spam_tumor2 = True

            self.window.blit(self.tumor_free[int(self.tumor2_animation_counter // self.tumor_animation_speed)],(coo1 + 390, coo2))
        else:
            if self.tumor2_animation_counter == len(self.tumor_free) * self.tumor_animation_speed:
                  self.tumor2_animation_counter = 0
                  
            self.window.blit(self.tumor_free[int(self.tumor2_animation_counter // self.tumor_animation_speed)],(coo1 + 390, coo2))
            
        self.tumor2_animation_counter += 1
        
    def draw(self):


        self.window.blit(self.background, (0,0))

        sayac = 0
        
        for i in self.protein_liste:
            self.window.blit(self.protein, (i[0], i[1]))
            if i[1] > 720:
                self.protein_liste.pop(sayac)
            self.protein_liste[sayac][1] += 3
            sayac += 1
        
        sayac = 0
        for i in self.neoantijen_liste:
            self.window.blit(self.neoantijen, (i[0], i[1]))
            if i[1] > 720:
                self.neoantijen_liste.pop(sayac)
            self.neoantijen_liste[sayac][1] += 3
            sayac += 1
            
        self.normal_spam_free_animation(coo1 = 0, coo2 = 0)

        self.window.blit(self.player, (self.player_X, self.player_Y))

        self.clock.tick(60)

        pygame.display.update()

    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        self.key = pygame.key.get_pressed()

        if self.key[pygame.K_ESCAPE]:
            return 0

        # silinecek
        if self.key[pygame.K_d]:
            self.player_X += 10
        elif self.key[pygame.K_a]:
            self.player_X -= 10

        self.draw()

game = Core()

while True:
    game_status = game.game_loop()
    if game_status is not None:
        break

pygame.quit()