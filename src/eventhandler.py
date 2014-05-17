import pygame
from pygame.locals import *


class EventHandler(object):

    def __init__(self, motor):

        self.motor = motor

    def update(self):

        self.lista = pygame.event.get()

        for event in self.lista:
            if event.type == QUIT:
                self.motor.menu.salir = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.dict['button'] == 4):
                    if self.motor.camara.pincel.tam < 3:
                        self.motor.camara.pincel.tam = self.motor.camara.pincel.tam + 1
                if (event.dict['button'] == 5):
                    if self.motor.camara.pincel.tam > 1:
                        self.motor.camara.pincel.tam = self.motor.camara.pincel.tam - 1

            if event.type == pygame.KEYDOWN:

                if event.key == K_F11:
                    if not self.motor.fullscreen:
                        self.motor.pantalla = pygame.display.set_mode(self.motor.resolucion,
                                 DOUBLEBUF | FULLSCREEN)
                        self.motor.fullscreen = True
                    else:
                        self.motor.pantalla = pygame.display.set_mode(self.motor.resolucion,
                             DOUBLEBUF)
                        self.motor.fullscreen = False

                if event.key == K_F1:
                    self.motor.menuayuda.run = True
                    while self.motor.menuayuda.run:
                        self.motor.menuayuda.ejecutar()
                        self.motor.dibuja(self.motor.menuayuda)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == K_F1:
                                    self.motor.menuayuda.run = False
                        pygame.display.update()

                if event.key == K_s:
                    self.motor.mundo.grabar(self.motor.mundo.nombre)

                #k_plus y k_minus parecen no funcionar, a lo mejor es algo de teclado europeo
                if event.key == K_PLUS:
                    if self.camara.pincel.tam < 3:
                        self.camara.pincel.tam = self.motor.camara.pincel.tam + 1

                if event.key == K_MINUS:
                    if self.motor.camara.pincel.tam > 1:
                        self.motor.camara.pincel.tam = self.motor.camara.pincel.tam - 1

                if event.key == K_e:
                    if not self.motor.mundo.modo_entidad:
                        self.motor.menu.marco_tileset.default = True
                    else:
                        if self.motor.camara.pincel.borrar:
                            self.motor.camara.pincel.borrar = False
                        else:
                            self.motor.camara.pincel.borrar = True

                if event.key == K_a:
                    if self.motor.mundo.aut_save:
                        self.motor.mundo.aut_save = False
                    else:
                        self.motor.mundo.aut_save = True

                if event.key == K_1:
                    self.motor.menu.marco_tileset.capa = 1
                    self.motor.mundo.capa = 1

                if event.key == K_3:
                    self.motor.menu.marco_tileset.capa = 3
                    self.motor.mundo.capa = 3

                if event.key == K_4:
                    self.motor.menu.marco_tileset.capa = 4
                    self.motor.mundo.capa = 4

                if event.key == K_LCTRL:
                    if not self.motor.menu.marco_tileset.modo_entidad:
                        self.motor.menu.marco_tileset.modo_entidad = True
                        self.motor.mundo.modo_entidad = True
                    else:
                        self.motor.menu.marco_tileset.modo_entidad = False
                        self.motor.mundo.modo_entidad = False

                if event.key == K_SPACE:
                    if self.motor.mundo.capa == 3:
                        if self.motor.camara.mostrar_capa3:
                            self.motor.camara.mostrar_capa3 = False
                        else:
                            self.motor.camara.mostrar_capa3 = True
                if event.key == K_LALT:
                    if self.motor.mundo.capa == 4:
                        if self.motor.camara.mostrar_capa4:
                            self.motor.camara.mostrar_capa4 = False
                        else:
                            self.motor.camara.mostrar_capa4 = True
            if pygame.key.get_pressed()[K_l] and pygame.key.get_pressed()[K_x]:

                self.motor.camara.tile_base(self.motor.tile_activo)
