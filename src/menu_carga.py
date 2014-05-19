import pygame
import os
from boton_editor import Boton


class MenuCarga(object):

    def __init__(self, resolucion, raton, mundo, camara):
        self.resolucion = resolucion
        self.raton = raton
        self.mundo = mundo
        self.camara = camara
        self.surface = pygame.surface.Surface(self.resolucion).convert()
        self.ventana = pygame.surface.Surface((800, 2 * self.resolucion[1] / 3)).convert()
        self.rect = self.surface.get_rect()
        self.rect_ventana = self.ventana.get_rect()
        self.rect_ventana.move_ip(self.rect.centerx - 400, 0)
        self.activo = False
        self.seleccionado = None
        self.array_botones = []
        # me da pereza pero hacer flecha arriba/abajo para controlar el scrolling
        # por si no hay raton de rueda
        #self.flecha_arriba = pygame.image.load("res/superflecha.png")

        #self.build_menu()
        self.boton_aceptar = Boton(100, 75, self.rect.centerx - 125,
                                self.rect.height - 100, "aceptar")


        self.boton_cancelar = Boton(100, 75, self.rect.centerx + 125,
                                self.rect.height - 100, "cancelar")
        self.fuente = pygame.font.SysFont('Arial', 28)

    def build_menu(self):
        self.array_botones = []
        self.tamx = 800
        self.tamy = 50
        self.dirlist = os.listdir("mapas/")
        y = 0
        for nombre in self.dirlist:
            boton = Boton(self.tamx, self.tamy, self.rect_ventana.centerx - 400, y, nombre[:-4], "res/boton_1.png", "res/boton_2.png")
            #boton.rect.move(0, 0)
            y += 50

            self.array_botones.append(boton)
        self.surface_partidas = pygame.surface.Surface((self.tamx, y)).convert()
        self.seleccionado = None
        self.scrolly = 0
        # mas tarde para que la surface no se vaya por ahi
        #self.scrolling = False

    def ventana_focused(self):

        if self.raton.puntero.colliderect(self.rect_ventana):
            return True

    def update(self, eventos):

        self.scrolly = 0
        self.surface.fill((0, 0, 0))
        self.surface_partidas.fill((0, 0, 0))
        self.ventana.fill((0, 0, 0))

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.dict['button'] == 5):

                    self.scrolly -= 50

                if (event.dict['button'] == 4):

                    self.scrolly += 50

        for i in self.array_botones:
            i.click(self.raton.puntero.x, self.raton.puntero.y)
            i.imprime()
            i.rect.move_ip(0, self.scrolly)
            self.surface_partidas.blit(i.surface, (0, i.rect.y))
            if self.ventana_focused():
                if i.variable == 1:
                    self.seleccionado = i.texto
                    i.variable = 0
        self.ventana.blit(self.surface_partidas, (0, 0))
        self.surface.blit(self.ventana, (self.rect_ventana.x, 30))
        self.boton_aceptar.click(self.raton.puntero.x, self.raton.puntero.y)
        self.boton_cancelar.click(self.raton.puntero.x, self.raton.puntero.y)
        self.boton_aceptar.imprime()
        self.boton_cancelar.imprime()
        if self.seleccionado:
            self.surface.blit(self.fuente.render("Cargar " + self.seleccionado + "?",
                    True, (255, 0, 0)), (self.boton_aceptar.rect.x - 30,
                    self.boton_aceptar.rect.y - 30))
        self.surface.blit(self.boton_aceptar.surface,
                (self.boton_aceptar.rect.x, self.boton_aceptar.rect.y))
        self.surface.blit(self.boton_cancelar.surface,
                (self.boton_cancelar.rect.x, self.boton_cancelar.rect.y))

        if self.boton_cancelar.variable == 1:
            self.activo = False
            self.boton_cancelar.variable = 0
            self.seleccionado = None

        if self.boton_aceptar.variable == 1:

            self.boton_aceptar.variable = 0
            self.activo = False
            # reinstanciamos la camara, ya que si el mapa anterior era mas grande
            # y la camara estaba lejos, al crear el nuevo mapa mas pequeno la camara
            # podria estar en una posicion no valida, dando error de indice
            if self.seleccionado is not None:

                self.camara.recargar(self.mundo)
                self.mundo.cargar_mapa("mapas/" + self.seleccionado + ".txt")

            else:

                print "ningun mapa seleccionado"

