import pygame
from pygame.locals import *
from camara_editor import Camara
from menu_editor import Menu
from raton_editor import Raton
from chat_editor import Chat
from mundo_editor import Mundo
from ayuda_editor import Ayuda
#from eventhandler import EventHandler


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
        self.menu.update()
        #self.eventos = EventHandler(self)
        self.dibuja(self.menu)
        self.cambio = False
        self.fullscreen = False
        self.primera_menu = True
        self.primera_camara = True

    def iniciar(self):

        pygame.init()
        self.cambio = False
        pygame.display.set_caption(self.nombre)
        self.salir = False
        self.reloj = pygame.time.Clock()

        while self.menu.salir != 1:

            self.reloj.tick(40)
            #self.eventos.update()
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

            if self.menu.menu_nmundo.activo:

                self.menu_activo()

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

            self.menu.update()
            # por lo que veo reduciendo el blit se reduce muchisimo el uso de cpu
            # asi que uso el metodo focused para que haga el blit sobre la parte
            # activa, ademas uso una variable para que el raton desaparezca si no
            # esta focuseada, es decir, sin esto el raton queda dibujado de la anterior
            # vez, aunque hay que estar constantemente reasignando la variable,
            # el beneficio es mucho mayor. (el menu no se actualiza correctamente por las
            # teclas)

            #if self.menu.focused():
                #self.dibuja(self.menu)
                #self.primera_menu = True

            #else:
                #if self.primera_menu:
                    #self.dibuja(self.menu)
                    #self.primera_menu = False

            #self.camara.pincel.update()
            self.dibuja(self.menu)
            self.muestra_chat()
            self.dibuja(self.chat)
            if not self.camara.focused():
                self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))
                if self.primera_camara:
                    self.pantalla.blit(self.camara.render(), (0, 0))
                    self.primera_camara = False
            else:

                self.camara.update(self.tile_activo)
                self.pantalla.blit(self.camara.render(), (0, 0))

                self.primera_camara = True

            if self.mundo.aut_save:
                self.cont_tiempo = self.cont_tiempo + 1
                if self.cont_tiempo == 10000:
                    self.mundo.grabar("temporal")
                    self.cont_tiempo = 0
            #pygame.display.flip()
            pygame.display.update()

    def dibuja(self, ente):

        self.pantalla.blit(ente.surface, (ente.rect.x, ente.rect.y))

    def muestra_chat(self):

        self.chat.update(self.tile_activo, self.mundo.capa,
                 self.camara.mostrar_capa3, self.camara.mostrar_capa4,
                 self.mundo.modo_entidad, self.camara.pincel.borrar, self.mundo.aut_save)
        self.chat.imprime()

    def menu_activo(self):

        while self.menu.menu_nmundo.activo:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.menu.menu_nmundo.activo = False
            self.reloj.tick(35)
            self.pantalla.fill((0, 0, 0))
            self.raton.update()
            #self.menu.update()
            self.menu.menu_nmundo.update()

            self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))
            #self.dibuja(self.menu)
            #self.dibuja(self.camara)
            self.dibuja(self.menu.menu_nmundo)
            pygame.display.update(self.menu.menu_nmundo.rect)
            pygame.display.update()