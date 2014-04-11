import pygame
from pygame.locals import *
from boton_editor import Boton
from marco_tileset import MarcoTileset


class Menu(pygame.sprite.Sprite):

    def __init__(self, pantalla_tam, raton, mundo):

        super(Menu, self).__init__()
        self.raton = raton
        #self.mundo = mundo
        self.surface = pygame.image.load("menu.png")
        self.surface = pygame.transform.scale(self.surface,
            (pantalla_tam[0] / 2, pantalla_tam[1])).convert()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(pantalla_tam[0] / 2, 0)

        self.boton_nuevo = Boton(200, 75, 0, 600, "Nuevo mapa", "boton.png")
        self.boton_nuevo.centrarx(self.rect, 600)
        self.boton_salir = Boton(200, 75, 0, 800, "Salir", "boton.png")
        self.boton_salir.centrarx(self.rect, 800)
        self.boton_salir.bind(self.fsalir())
        self.salir = 0
        self.marco_tileset = MarcoTileset(mundo, self.raton)
        self.offsetx = 0
        self.offsety = 10
        self.marco_tileset.centrarx(self.rect, self.offsety)

        self.coordx = 0
        self.coordy = 0
        #print self.boton_nuevo.rect.x
        #print self.boton_nuevo.rect.y

    def update(self):

        self.boton_nuevo.imprime()
        self.boton_salir.imprime()
        self.surface.blit(self.boton_nuevo.surface,
                        (self.boton_nuevo.rect.x, self.boton_nuevo.rect.y))
        self.surface.blit(self.boton_salir.surface,
                        (self.boton_salir.rect.x, self.boton_salir.rect.y))
        self.marco_tileset.update()
        self.surface.blit(self.marco_tileset.surface, (self.marco_tileset.rect.x,
                         self.marco_tileset.rect.y))
        if self.focused():
            self.set_coord()
            if self.marco_tileset.focused(self.coordx, self.coordy,
                                        self.offsetx, self.offsety):
                lista = self.get_tile_coord()
                self.marco_tileset.get_tileselec(lista)
        #pygame.draw.rect(self.surface, (255, 0, 0), self.boton_nuevo.rect)

    def fsalir(self):

        self.salir = 1

    def focused(self):

        if self.rect.colliderect(self.raton.puntero):
            return True

    def set_coord(self):

        self.coordx = pygame.mouse.get_pos()[0] - self.rect.x
        self.coordy = pygame.mouse.get_pos()[1] - self.rect.y

    def get_tile_coord(self):

        coord = []
        x = self.coordx - self.marco_tileset.rect.x
        coord.append(x)
        y = self.coordy - self.offsety
        coord.append(y)
        return coord



