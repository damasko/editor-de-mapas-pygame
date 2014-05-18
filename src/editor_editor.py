import pygame
from pygame.locals import *
from camara_editor import Camara
from menu_editor import Menu
from raton_editor import Raton
from chat_editor import Chat
from mundo_editor import Mundo
from ayuda_editor import Ayuda
from nuevo_mundo import NuevoMundo
from menu_carga import MenuCarga
from eventhandler import EventHandler


class Editor(object):

    # No te olvides de quitar las rutas hardcodeadas y meterlas
    # en un archivo de configuracion

    def __init__(self, nombre="Editor", resolucion=(800, 600)):

        self.nombre = nombre
        self.resolucion = resolucion
        self.pantalla = pygame.display.set_mode(self.resolucion)
        self.cont_tiempo = 0

        self.menuayuda = Ayuda(self.resolucion)
        self.mundo = Mundo()
        self.raton = Raton("res/puntero.png")
        self.camara = Camara(self.mundo, self.raton, self.resolucion)
        # de momento menu_nmundo se queda aqui ya veremos si es mejor moverlo a
        # menu como estaba antes
        self.menu_nmundo = NuevoMundo(self.resolucion[0] / 2,
                    self.resolucion[1] / 2, 10, 10, self.raton, self.mundo, self.camara)
        self.menu_carga = MenuCarga(self.resolucion, self.raton, self.mundo, self.camara)
        self.menu = Menu(self.resolucion, self.raton, self.mundo,
                            self.menu_nmundo, self.menu_carga)
        self.chat = Chat(self.resolucion, self.mundo.tiles_suelos1[31][31], self.mundo.capa,
                      self.mundo.modo_entidad, self.camara.pincel.borrar,
                       self.mundo.aut_save)

        self.eventhandler = EventHandler(self)

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

            # ticks del reloj
            self.reloj.tick(40)
            # actualizacion eventos de teclado
            self.eventhandler.update()

            # actualizacion del raton (raton + puntero)
            # (puntero es un rect muy pequeno que sigue a raton para darle mas precision)
            self.raton.update()
            # tile seleccionado:
            if not self.mundo.modo_entidad:
                # seleccion de tile del marco del menu
                if self.mundo.capa == 1:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_suelos
                elif self.mundo.capa == 3:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_paredes
                elif self.mundo.capa == 4:
                    self.tile_activo = self.menu.marco_tileset.tile_seleccionado_tejados
            else:
                # seleccion del tile que representa un enemigo
                self.tile_activo = self.menu.marco_tileset.tile_seleccionado_enemigos
            self.tile_activo_paredes = self.menu.marco_tileset.tile_seleccionado_paredes

            self.menu.update()
            #print self.mundo.nombre
            # /* anotacion1
            # /** anotacion2

            ########### dibujar sobre la pantalla el menu, actualizacion de chat y mostrarlo
            self.dibuja(self.menu)
            self.muestra_chat()
            self.dibuja(self.chat)
            ###########

            if not self.camara.focused():    # /**
                self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))
                if self.primera_camara:
                    self.pantalla.blit(self.camara.render(), (0, 0))
                    self.primera_camara = False
            else:

                self.camara.update(self.tile_activo)
                self.pantalla.blit(self.camara.render(), (0, 0))

                self.primera_camara = True

            # menu para crear nuevo mundo
            if self.menu_nmundo.activo:

                self.menu_activo()

            if self.menu_carga.activo:

                self.menu_carga_activo()

            if self.menuayuda.run:

                self.menu_ayuda()

            # contador para guardar con autosave, esta en milisegundos
            if self.mundo.aut_save:
                self.cont_tiempo = self.cont_tiempo + 1
                if self.cont_tiempo == 8000:
                    self.mundo.grabar("temporal")
                    self.cont_tiempo = 0
                    print "Mapa guardado en temporal.txt"
            pygame.display.update()

    def dibuja(self, ente):

        self.pantalla.blit(ente.surface, (ente.rect.x, ente.rect.y))

    def muestra_chat(self):

        self.chat.update(self.tile_activo, self.mundo.capa,
                 self.camara.mostrar_capa3, self.camara.mostrar_capa4,
                 self.mundo.modo_entidad, self.camara.pincel.borrar, self.mundo.aut_save)
        self.chat.imprime()


    def menu_ayuda(self):

        while self.menuayuda.run:
            self.menuayuda.ejecutar()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_F1:
                        self.menuayuda.run = False
            self.dibuja(self.menuayuda)
            pygame.display.update()
        self.pantalla.blit(self.camara.render(), (0, 0))

    def menu_activo(self):

        while self.menu_nmundo.activo:

            # /***
            eventos = pygame.event.get()
            self.pantalla.fill((0, 0, 0))
            self.reloj.tick(35)
            self.raton.update()
            self.menu_nmundo.update(eventos, self.mundo)
            self.menu_nmundo.render()
            self.dibuja(self.menu_nmundo)
            self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))
            self.menu.update()
            pygame.display.update()
        self.pantalla.blit(self.camara.render(), (0, 0))

    def menu_carga_activo(self):

        self.menu_carga.build_menu()
        while self.menu_carga.activo:
            eventos = pygame.event.get()
            self.pantalla.fill((0, 0, 0))
            self.reloj.tick(35)
            self.raton.update()
            self.menu_carga.update(eventos)
            self.dibuja(self.menu_carga)
            self.pantalla.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))
            self.menu.update()
            pygame.display.update()
        self.pantalla.blit(self.camara.render(), (0, 0))

    # /*
    # por lo que veo reduciendo el blit se reduce muchisimo el uso de cpu
    # asi que uso el metodo focused para que haga el blit sobre la parte
    # activa, ademas uso una variable para que el raton desaparezca si no
    # esta focuseada, es decir, sin esto el raton queda dibujado de la anterior
    # vez, aunque hay que estar constantemente reasignando la variable,
    # el beneficio es mucho mayor. (el menu no se actualiza correctamente por las
    # teclas)

    # /**
    # para ahorrar el blit del menu cuando no esta activo, el problema es que que
    # la tecla no actualiza bien el marco de tilesets si este no se encuentra
    # focuseado(logico) revisar. Con la camara, al no tener que actualizarse por teclado
    # como es el caso del marco, funciona bastante bien

    #if self.menu.focused():
                #self.dibuja(self.menu)
                #self.primera_menu = True

            #else:

                #if self.primera_menu:
                    #self.dibuja(self.menu)
                    #self.primera_menu = False


    # /***
    # recuerda que no puedes estar constantemente llamando a pygame.event.get
    # ya que vacia la cola de eventos en cada llamada y devuelve una
    # lista, mejor almacenarlo en este caso, pasarsela a menu_nmundo y
    # que el compruebe los textinput, que requieren ver eventos de teclado
