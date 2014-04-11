import pygame


class CajaTexto(pygame.sprite.Sprite):

    def __init__(self, tamx, tamy):
        super(CajaTexto, self).__init__()
        pygame.font.init()
        self.texto = ""
        self.surface = pygame.surface.Surface((tamx, tamy))

    def update(self):
        self.surface.blit(self.fuente.render(self.texto_entidad, True,
                            (255, 255, 255)), (self.offset + 200, self.offset + 200))

