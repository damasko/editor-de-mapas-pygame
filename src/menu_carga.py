import pygame
import os
#from caja_texto import CajaTexto
from boton_editor import Boton


class MenuCarga(object):

    def __init__(self, resolucion, raton, mundo, camara):
        self.resolucion = resolucion
        self.raton = raton
        self.mundo = mundo
        self.camara = camara
        self.surface = pygame.surface.Surface(self.resolucion)
        self.rect = self.surface.get_rect()
        self.activo = False
        self.seleccionado = None
        self.array_botones = []
        #self.build_menu()
        self.boton_aceptar = Boton(100, 75, self.rect.centerx - 125,
                                self.rect.height - 100, "aceptar")

        self.boton_cancelar = Boton(100, 75, self.rect.centerx + 125,
                                self.rect.height - 100, "cancelar")
        self.fuente = pygame.font.SysFont('Arial', 28)

    def build_menu(self):

        self.dirlist = os.listdir("mapas/")
        y = 0
        for nombre in self.dirlist:
            boton = Boton(800, 50, self.rect.centerx - 400, y + 50,
                    nombre, "res/boton_1.png", "res/boton_2.png")
            y += 50
            self.array_botones.append(boton)

    def update(self):

        self.surface.fill((0, 0, 0))
        for i in self.array_botones:
            i.click(self.raton.puntero.x, self.raton.puntero.y)
            i.imprime()
            self.surface.blit(i.surface, (i.rect.x, i.rect.y))
            if i.variable == 1:
                self.seleccionado = i.texto
                i.variable = 0
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

        if self.boton_aceptar.variable == 1:
            self.boton_aceptar.variable = 0
            self.activo = False
            # reinstanciamos la camara, ya que si el mapa anterior era mas grande
            # y la camara estaba lejos, al crear el nuevo mapa mas pequeno la camara
            # podria estar en una posicion no valida, dando error de indice
            self.camara.recargar(self.mundo)
            self.mundo.cargar_mapa("mapas/" + self.seleccionado)
