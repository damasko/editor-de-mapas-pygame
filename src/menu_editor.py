import pygame
from pygame.locals import *
from boton_editor import Boton
from marco_tileset import MarcoTileset
from nuevo_mundo import NuevoMundo


class Menu(pygame.sprite.Sprite):

    def __init__(self, pantalla_tam, raton, mundo):

        super(Menu, self).__init__()
        self.raton = raton
        #self.mundo = mundo
        self.surface = pygame.image.load("res/menu.png")
        self.surface = pygame.transform.scale(self.surface,
            (pantalla_tam[0] / 2, pantalla_tam[1])).convert()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(pantalla_tam[0] / 2, 0)
        self.mundo = mundo
        self.boton_nuevo = Boton(150, 75, 0, 600, "Nuevo mapa", "res/boton_1.png")
        self.boton_nuevo.centrarx(self.rect)
        self.boton_salir = Boton(150, 75, 0, 800, "Salir", "res/boton_1.png")
        self.boton_salir.centrarx(self.rect)
        self.boton_salir.bind(self.fsalir)
        self.salir = 0
        self.marco_tileset = MarcoTileset(self.mundo)
        self.offsetx = 0
        self.offsety = 10
        self.marco_tileset.centrarx(self.rect, self.offsety)
        self.menu_nmundo = NuevoMundo(self.rect.width - 20,
                self.rect.height/2 - 20, 10, 10, self.raton, self.mundo)
        self.coordx = 0
        self.coordy = 0

    def update(self):

        if self.focused():
            self.set_coord()
            self.boton_nuevo.click(self.coordx, self.coordy)
            self.boton_salir.click(self.coordx, self.coordy)
            if self.marco_tileset.focused(self.coordx, self.coordy,
                                        self.offsetx, self.offsety):
                lista = self.get_tile_coord()
                self.marco_tileset.get_tileselec(lista)

        self.marco_tileset.update()
        self.surface.blit(self.marco_tileset.surface, (self.marco_tileset.rect.x,
                         self.marco_tileset.rect.y))
        self.boton_nuevo.imprime()
        self.boton_salir.imprime()

        self.surface.blit(self.boton_nuevo.surface,
                        (self.boton_nuevo.rect.x, self.boton_nuevo.rect.y))
        self.surface.blit(self.boton_salir.surface,
                        (self.boton_salir.rect.x, self.boton_salir.rect.y))

        if self.boton_salir.variable == 1:

            self.salir = 1

        # lo suyo seria cambiar la variable self.salir directamente
        # pasandosela al boton, pero no la cambia (supongo que la pasa por copia)

        if self.boton_nuevo.variable == 1:
            self.boton_nuevo.variable = 0

            self.menu_nmundo.activo = True

    def fnmundo(self):

        self.boton_nuevo.variable = 1

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



