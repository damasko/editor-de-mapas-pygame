import pygame


class Raton(pygame.sprite.Sprite):

    def __init__(self, imagen=None):

        super(Raton, self).__init__()

        if not imagen:
            self.surface = pygame.surface.Surface((6,6)).convert()
        else:
            self.surface = pygame.image.load(imagen).convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (16, 32))
        self.surface.set_colorkey((255, 0, 255))

        self.rect = self.surface.get_rect()
        self.puntero = pygame.rect.Rect(0,0,2,5)
        pygame.mouse.set_visible(False)

    def update(self):

        coord = pygame.mouse.get_pos()
        self.puntero.x = coord[0]
        self.puntero.y = coord[1]

    def estado(self):

        return pygame.mouse.get_pressed()

