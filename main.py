import pygame
from random import randint
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

        self.normal_spam_time = 20
        self.spam_counter = 0

        self.normal_animation_speed = 4
        self.normal_free_animation_counter = 0
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

    def draw(self):

        self.window.blit(self.background, (0,0))

        self.window.blit(self.player, (self.player_X, self.player_Y))

        if self.normal_free_animation_counter == len(self.normal_free)*self.normal_animation_speed:
            self.normal_free_animation_counter = 0

        self.window.blit(self.normal_free[int(self.normal_free_animation_counter // self.normal_animation_speed)], (0, 0))

        self.normal_free_animation_counter += 1

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