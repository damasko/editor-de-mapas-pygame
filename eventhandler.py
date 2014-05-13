import pygame
from pygame.locals import *


class EventHandler(object):

    def __init__(self, motor):
        self.lista = pygame.event.get()

    def update(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                self.menu.salir = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.dict['button'] == 4):
                    if self.camara.pincel.tam < 3:
                        self.camara.pincel.tam = self.camara.pincel.tam + 1
                if (event.dict['button'] == 5):
                    if self.camara.pincel.tam > 1:
                        self.camara.pincel.tam = self.camara.pincel.tam - 1

            if event.type == pygame.KEYDOWN:

                if event.key == K_F11:
                    if not self.fullscreen:
                        self.pantalla = pygame.display.set_mode(self.resolucion,
                                 DOUBLEBUF | FULLSCREEN)
                        self.fullscreen = True
                    else:
                        self.pantalla = pygame.display.set_mode(self.resolucion,
                             DOUBLEBUF)
                        self.fullscreen = False

                if event.key == K_F1:
                    self.menuayuda.run = True
                    while self.menuayuda.run:
                        self.menuayuda.ejecutar()
                        self.dibuja(self.menuayuda)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_F1:
                                    self.menuayuda.run = False
                        pygame.display.update()

                if event.key == K_s:
                    self.mundo.grabar(self.mundo.nombre)

                if event.key == K_PLUS:
                    if self.camara.pincel.tam < 3:
                        self.camara.pincel.tam = self.camara.pincel.tam + 1

                if event.key == K_MINUS:
                    if self.camara.pincel.tam > 1:
                        self.camara.pincel.tam = self.camara.pincel.tam - 1

                if event.key == K_e:
                    if not self.mundo.modo_entidad:
                        self.menu.marco_tileset.default = True
                    else:
                        if self.camara.pincel.borrar:
                            self.camara.pincel.borrar = False
                        else:
                            self.camara.pincel.borrar = True

                if event.key == K_a:
                    if self.mundo.aut_save:
                        self.mundo.aut_save = False
                    else:
                        self.mundo.aut_save = True

                if event.key == K_1:
                    self.menu.marco_tileset.capa = 1
                    self.mundo.capa = 1

                if event.key == K_3:
                    self.menu.marco_tileset.capa = 3
                    self.mundo.capa = 3

                if event.key == K_4:
                    self.menu.marco_tileset.capa = 4
                    self.mundo.capa = 4

                if event.key == K_LCTRL:
                    if not self.menu.marco_tileset.modo_entidad:
                        self.menu.marco_tileset.modo_entidad = True
                        self.mundo.modo_entidad = True
                    else:
                        self.menu.marco_tileset.modo_entidad = False
                        self.mundo.modo_entidad = False

                if event.key == K_SPACE:
                    if self.mundo.capa == 3:
                        if self.camara.mostrar_capa3:
                            self.camara.mostrar_capa3 = False
                        else:
                            self.camara.mostrar_capa3 = True
                if event.key == K_LALT:
                    if self.mundo.capa == 4:
                        if self.camara.mostrar_capa4:
                            self.camara.mostrar_capa4 = False
                        else:
                            self.camara.mostrar_capa4 = True
            if pygame.key.get_pressed()[K_l] and pygame.key.get_pressed()[K_x]:

                self.camara.tile_base(self.tile_activo)
