import pygame
from pygame.locals import *


class CajaTexto(object):

    def __init__(self, tamx, tamy, posx, posy):

        super(CajaTexto, self).__init__()
        pygame.font.init()
        self.texto = ""
        self.surface = pygame.image.load("res/caja.png")
        self.surface = pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        self.background = self.surface.copy()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(posx, posy)
        self.fijado = False
        #fuente provisional
        self.fuente = pygame.font.SysFont('Arial', 14)

        # tposx y tposy indican donde se va a pintar el texto de momento no se usa
        self.tposx = 0
        self.tposy = 0
        self.tamx = tamx
        self.tamy = tamy
        self.centrary()
        self.traza = 0

    def clear(self):

        self.texto = ""

    def centrary(self):

        self.posy = self.rect.centery

    def update(self, raton_coordx, raton_coordy, lista_eventos):

        # no se puede alterar el texto, ya que una vez hecho el blit
        # la otra surface se vuelve parte de la surface destino, por lo
        # que no se puede actualizar el texto. La solucion es tener un
        # background que lo cargue antes, y luego rendear de nuevo el texto O.o
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.fuente.render(self.texto, True, (0, 0, 0)),
                    (15, 15))

        # con focused y fijado conseguimos que al darle click al box este se mantenga
        # activo, si hacemos click fuera de el se desactiva

        if self.focused(raton_coordx, raton_coordy) and pygame.mouse.get_pressed()[0]:

            self.fijado = True

        if self.fijado:

            if pygame.mouse.get_pressed()[0] and not self.focused(raton_coordx, raton_coordy):
                self.fijado = False
            for event in lista_eventos:
                if event.type == pygame.KEYDOWN:

                    # (cogido de eztext)
                    if event.key == K_a: self.texto += 'a'
                    elif event.key == K_b: self.texto += 'b'
                    elif event.key == K_c: self.texto += 'c'
                    elif event.key == K_d: self.texto += 'd'
                    elif event.key == K_e: self.texto += 'e'
                    elif event.key == K_f: self.texto += 'f'
                    elif event.key == K_g: self.texto += 'g'
                    elif event.key == K_h: self.texto += 'h'
                    elif event.key == K_i: self.texto += 'i'
                    elif event.key == K_j: self.texto += 'j'
                    elif event.key == K_k: self.texto += 'k'
                    elif event.key == K_l: self.texto += 'l'
                    elif event.key == K_m: self.texto += 'm'
                    elif event.key == K_n: self.texto += 'n'
                    elif event.key == K_o: self.texto += 'o'
                    elif event.key == K_p: self.texto += 'p'
                    elif event.key == K_q: self.texto += 'q'
                    elif event.key == K_r: self.texto += 'r'
                    elif event.key == K_s: self.texto += 's'
                    elif event.key == K_t: self.texto += 't'
                    elif event.key == K_u: self.texto += 'u'
                    elif event.key == K_v: self.texto += 'v'
                    elif event.key == K_w: self.texto += 'w'
                    elif event.key == K_x: self.texto += 'x'
                    elif event.key == K_y: self.texto += 'y'
                    elif event.key == K_z: self.texto += 'z'
                    elif event.key == K_0: self.texto += '0'
                    elif event.key == K_1: self.texto += '1'
                    elif event.key == K_2: self.texto += '2'
                    elif event.key == K_3: self.texto += '3'
                    elif event.key == K_4: self.texto += '4'
                    elif event.key == K_5: self.texto += '5'
                    elif event.key == K_6: self.texto += '6'
                    elif event.key == K_7: self.texto += '7'
                    elif event.key == K_8: self.texto += '8'
                    elif event.key == K_9: self.texto += '9'
                    elif event.key == K_SPACE: self.texto += ' '
                    elif event.key == K_MINUS: self.texto += '-'
                    elif event.key == K_EQUALS: self.texto += '='
                    elif event.key == K_LEFTBRACKET: self.texto += '['
                    elif event.key == K_RIGHTBRACKET: self.texto += ']'
                    #elif event.key == K_BACKSLAS: self.texto += '\\'
                    elif event.key == K_SEMICOLON: self.texto += ';'
                    elif event.key == K_QUOTE: self.texto += '\''
                    elif event.key == K_COMMA: self.texto += ','
                    elif event.key == K_PERIOD: self.texto += '.'
                    elif event.key == K_SLASH: self.texto += '/'
                    elif event.key == K_BACKSPACE:
                        if len(self.texto) > 0:
                            self.texto = self.texto[:-1]
                    else: pass

    def focused(self, raton_coordx, raton_coordy):

        if raton_coordx > self.rect.x and raton_coordx < self.rect.x + self.rect.width                and raton_coordy > self.rect.y and raton_coordy < self.rect.y + self.rect.height:

            return True
