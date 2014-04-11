import pygame
from pygame.locals import *
from camara_editor import Camara
from menu_editor import Menu
from raton_editor import Raton
from chat_editor import Chat
#from caja_texto import CajaTexto
from mundo_editor import Mundo
from ayuda_editor import Ayuda


class Editor(object):

    def __init__(self, nombre="Editor", resolucion=(800, 600)):

        self.nombre = nombre
        self.resolucion = resolucion
        self.pantalla = pygame.display.set_mode(self.resolucion)
        self.cont_tiempo = 0

        nombre_mundo = "test"
        self.menuayuda = Ayuda(self.resolucion)
        self.mundo = Mundo(nombre_mundo)
        self.raton = Raton("puntero.png")
        self.camara = Camara(self.mundo, self.raton, self.resolucion)
        self.menu = Menu(self.resolucion, self.raton, self.mundo)
        self.chat = Chat(self.resolucion, self.mundo.tiles_suelos1[31][31], self.mundo.capa,
                      self.mundo.modo_entidad, self.camara.pincel.borrar,
                       self.mundo.aut_save)
        self.cambio = False

    def iniciar(self):

        pygame.init()
        self.cambio = False
        pygame.display.set_caption(self.nombre)
        self.salir = False
        self.reloj = pygame.time.Clock()

        while self.menu.salir != 1:

            self.reloj.tick(35)

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

                if self.menu.boton_salir.click(self.raton):
                    self.menu.salir = True

            self.raton.update()
            if not self.mundo.modo_entidad:
                if self.mundo.capa == 1:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_suelos
                elif self.mundo.capa == 3:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_paredes
                elif self.mundo.capa == 4:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_tejados
            else:
                self.tile_activo = self.menu.marco_tileset.tile_seleccionado_enemigos
            self.tile_activo_paredes = self.menu.marco_tileset.tile_seleccionado_paredes
            self.camara.update(self.tile_activo)
            self.pantalla.blit(self.camara.render(), (0, 0))
            self.menu.update()
            self.dibuja(self.menu)

            #self.camara.pincel.update()
            self.chat.update(self.tile_activo, self.mundo.capa,
                 self.camara.mostrar_capa3, self.camara.mostrar_capa4,
                  self.mundo.modo_entidad, self.camara.pincel.borrar, self.mundo.aut_save)
            self.chat.imprime()
            self.dibuja(self.chat)
            if not self.camara.focused():
                self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))

            if self.mundo.aut_save:
                self.cont_tiempo = self.cont_tiempo + 1
                if self.cont_tiempo == 10000:
                    self.mundo.grabar("temporal")
                    self.cont_tiempo = 0
            pygame.display.update()

    def dibuja(self, ente):

        self.pantalla.blit(ente.surface, (ente.rect.x, ente.rect.y))

