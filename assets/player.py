import pygame

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

class Player(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super(Player, self).__init__()

        self.surf = pygame.image.load("../boy.png").convert()
        self.surf.set_colorkey(COLOR)



        self.rect = self.image.get_rect()
