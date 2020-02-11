import pygame

class LegalMove:

    def __init__(self, coord):
        self.x = coord[0]
        self.y = coord[1]
        self._image_surf = pygame.image.load("sprites/block-green20x20.png").convert()

    def get(self):
        return (self.x, self.y)

    def draw(self, surface):
        surface.blit(self._image_surf,(self.x,self.y))