import pygame
from caja_texto import CajaTexto
from boton_editor import Boton
#from layout import GridLayout


#Clase para el menu de creacion de nuevo mundo
class NuevoMundo(pygame.sprite.Sprite):

    def __init__(self, tamx, tamy, posx, posy, raton, mundo):

        super(NuevoMundo, self).__init__()
        self.mundo = mundo
        self.surface = pygame.image.load("res/mundonuevo.png").convert()
        self.surface = pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(posx, posy)

        # fuente provisional
        self.fuente = pygame.font.SysFont('Arial', 14)
        self.offset = 20
        self.nombre = "Nombre"
        self.caja_nombre = CajaTexto(self.rect.width / 2 - self.offset, 50, self.rect.x + 10, self.rect.y + 10)

        self.ancho = "Ancho"
        self.caja_ancho = CajaTexto(self.rect.width / 2,
                    self.rect.height / 12, self.rect.x - self.rect.x / 2,
                    self.caja_nombre.rect.bottomleft[1])
        self.alto = "Alto"
        self.caja_alto = CajaTexto(self.rect.width / 2,
                    self.rect.height / 12, self.rect.x - self.rect.x / 2,
                    self.caja_ancho.rect.bottomleft[1])

        self.boton_aceptar = Boton(self.rect.width/4, self.rect.height/9,
                10, self.rect.height - self.rect.height/9 - 10, "aceptar")

        self.boton_cancelar = Boton(self.rect.width/4, self.rect.height/9, self.rect.width - self.rect.width/4 - 10, self.rect.height - self.rect.height/9 - 10, "cancelar")
        self.activo = False
        self.raton = raton
        self.eventos = []
        # dios mio crear la clase layout que dolor de cabeza
        # pd: que dolor de cabeza da la clase layout!

    def focused(self):

        if self.raton.puntero.colliderect(self):
            return True

    def update(self, eventos):

        self.boton_aceptar.imprime()
        self.boton_cancelar.imprime()
        self.boton_aceptar.click(self.raton.puntero.x, self.raton.puntero.y)
        self.boton_cancelar.click(self.raton.puntero.x, self.raton.puntero.y)

        self.caja_nombre.update(self.raton.puntero.x, self.raton.puntero.y, eventos)
        #self.caja_alto.update(self.raton.puntero.x, self.raton.puntero.y, eventos)
        #self.caja_ancho.update(self.raton.puntero.x, self.raton.puntero.y, eventos)

        if self.boton_aceptar.variable == 1:

            self.boton_aceptar.variable = 0
            self.activo = False
            if self.comprueba_box():

                self.mundo = self.mundo.nuevo_mundo(str(self.caja_nombre.texto),
                        int(self.caja_alto.texto), int(self.caja_ancho.texto))

            self.clear_box()

        if self.boton_cancelar.variable == 1:

            self.boton_cancelar.variable = 0
            self.activo = False
            self.clear_box()

    def render(self):

        self.surface.blit(self.caja_nombre.surface,
                        (self.caja_nombre.rect.x, self.caja_nombre.rect.y))
        #self.surface.blit(self.caja_ancho.surface,
                        #(self.caja_ancho.rect.x, self.caja_ancho.rect.y))

        #self.surface.blit(self.caja_alto.surface,
                        #(self.caja_alto.rect.x, self.caja_alto.rect.y))

        self.surface.blit(self.boton_aceptar.surface,
                        (self.boton_aceptar.rect.x, self.boton_aceptar.rect.y))
        self.surface.blit(self.boton_cancelar.surface,
                        (self.boton_cancelar.rect.x, self.boton_cancelar.rect.y))

        self.surface.blit(self.fuente.render(self.nombre, True,
                        (255, 255, 255)), (self.caja_nombre.rect.x,
                            self.caja_nombre.rect.y - 30))
        self.surface.blit(self.fuente.render(self.ancho, True,
                        (255, 255, 255)), (self.caja_ancho.rect.x,
                            self.caja_ancho.rect.y - 30))

        self.surface.blit(self.fuente.render(self.alto, True,
                        (255, 255, 255)), (self.caja_alto.rect.x,
                            self.caja_alto.rect.y - 30))


    def clear_box(self):

        self.caja_nombre.clear()
        self.caja_alto.clear()
        self.caja_ancho.clear()

    def comprueba_box(self):

        dato_valido1 = False
        dato_valido2 = False
        if self.caja_nombre.texto == "":
            self.caja_nombre.texto = "default"
        if self.caja_ancho.texto == "":
            self.caja_ancho.texto = "25"
        if self.caja_alto.texto == "":
            self.caja_alto = "25"

        if int(self.caja_ancho.texto) >= 25:
            dato_valido1 = True
        if int(self.caja_alto.texto) >= 25:
            dato_valido2 = True

        if dato_valido1 and dato_valido2:
            return True

        return False