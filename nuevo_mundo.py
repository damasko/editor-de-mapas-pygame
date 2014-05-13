import pygame
from caja_texto import CajaTexto
from boton_editor import Boton
from layout import GridLayout


#Clase para el menu de creacion de nuevo mundo
class NuevoMundo(pygame.sprite.Sprite):

    def __init__(self, tamx, tamy, posx, posy, raton):

        super(NuevoMundo, self).__init__()

        self.surface = pygame.image.load("mundonuevo.png")
        self.surface = pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(posx, posy)

        # fuente provisional
        self.fuente = pygame.font.SysFont('Arial', 14)
        self.offset = 20
        self.nombre = "Nombre"
        self.caja_nombre = CajaTexto(self.rect.width / 2,
                    self.rect.height / 12, 10, 50)
        self.ancho = "Ancho"
        self.caja_ancho = CajaTexto(self.rect.width / 2,
                    self.rect.height / 12, 10, 150)
        self.alto = "Alto"
        self.caja_alto = CajaTexto(self.rect.width / 2,
                    self.rect.height / 12, 10, 250)

        #self.layout = GridLayout(self.rect.width/2, self.rect.height/6,
                    #self.rect.x, self.rect.y, 1, 1)
        #self.layout.add(self.caja_nombre)
        #self.layout.add(self.caja_ancho)
        #self.layout.add(self.caja_alto)

        self.boton_aceptar = Boton(self.rect.width/4, self.rect.height/9,
                10, self.rect.height - self.rect.height/9 - 10, "aceptar")

        self.boton_cancelar = Boton(self.rect.width/4, self.rect.height/9, self.rect.width - self.rect.width/4 - 10, self.rect.height - self.rect.height/9 - 10, "cancelar")
        self.activo = False
        self.raton = raton

        # dios mio crear la clase layout que dolor de cabeza
        # pd: que dolor de cabeza la clase layout!

    def focused(self):

        if self.raton.puntero.colliderect(self):
            return True

    def update(self):

        if self.activo:
            #self.surface.fill((0, 0, 0))

            self.surface.blit(self.fuente.render(self.nombre, True,
                            (255, 255, 255)), (self.caja_nombre.rect.x,
                                self.caja_nombre.rect.y - 30))
            self.surface.blit(self.fuente.render(self.ancho, True,
                            (255, 255, 255)), (self.caja_ancho.rect.x,
                                self.caja_ancho.rect.y - 30))

            self.surface.blit(self.fuente.render(self.alto, True,
                            (255, 255, 255)), (self.caja_alto.rect.x,
                                self.caja_alto.rect.y - 30))

            self.surface.blit(self.caja_nombre.surface,
                            (self.caja_nombre.rect.x, self.caja_nombre.rect.y))
            self.surface.blit(self.caja_ancho.surface,
                            (self.caja_ancho.rect.x, self.caja_ancho.rect.y))

            self.surface.blit(self.caja_alto.surface,
                            (self.caja_alto.rect.x, self.caja_alto.rect.y))

            self.boton_aceptar.imprime()
            self.boton_cancelar.imprime()

            self.surface.blit(self.boton_aceptar.surface,
                            (self.boton_aceptar.rect.x, self.boton_aceptar.rect.y))
            self.surface.blit(self.boton_cancelar.surface,
                            (self.boton_cancelar.rect.x, self.boton_cancelar.rect.y))

            self.boton_aceptar.click(self.raton.puntero.x, self.raton.puntero.y)
            self.boton_cancelar.click(self.raton.puntero.x, self.raton.puntero.y)

            self.caja_nombre.update(self.raton.puntero.x, self.raton.puntero.y)
            self.caja_alto.update(self.raton.puntero.x, self.raton.puntero.y)
            self.caja_ancho.update(self.raton.puntero.x, self.raton.puntero.y)
            if self.focused():
                self.surface.blit(self.raton.surface, (self.raton.puntero.x, self.raton.puntero.y))

            if self.boton_aceptar.variable == 1:
                self.activo = False
            if self.boton_cancelar.variable == 1:
                self.activo = False

        #print self.caja_nombre.rect.y



