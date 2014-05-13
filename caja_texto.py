import pygame
from pygame.locals import *


class CajaTexto(pygame.sprite.Sprite):

    def __init__(self, tamx, tamy, posx, posy):
        super(CajaTexto, self).__init__()
        pygame.font.init()
        self.texto = ""
        #self.surface = pygame.surface.Surface((tamx, tamy)).convert()
        self.surface = pygame.image.load("caja.png")
        pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        self.rect = self.surface.get_rect()
        self.rect.move_ip(posx, posy)
        self.activo = False

        #fuente provisional
        self.fuente = pygame.font.SysFont('Arial', 14)

    def update(self, raton_coordx, raton_coordy):
        #print self.rect.x
        #print self.rect.y
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect)
        if self.focused(raton_coordx, raton_coordy):

            for event in pygame.event.get():
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
                    elif event.key == K_: self.texto += '5'
                    elif event.key == K_6: self.texto += '6'
                    elif event.key == K_7: self.texto += '7'
                    elif event.key == K_8: self.texto += '8'
                    elif event.key == K_9: self.texto += '9'
                    elif event.key == K_MINUS: self.texto += '-'
                    elif event.key == K_EQUALS: self.texto += '='
                    elif event.key == K_LEFTBRACKET: self.texto += '['
                    elif event.key == K_RIGHTBRACKET: self.texto += ']'
                    elif event.key == K_BACKSLAS: self.texto += '\\'
                    elif event.key == K_SEMICOLON: self.texto += ';'
                    elif event.key == K_QUOTE: self.texto += '\''
                    elif event.key == K_COMMA: self.texto += ','
                    elif event.key == K_PERIOD: self.texto += '.'
                    elif event.key == K_SLASH: self.texto += '/'
                    else: pass

        self.surface.blit(self.fuente.render(self.texto, True,
                            (0, 0, 255)), (self.rect.x, self.rect.y))

    def focused(self, raton_coordx, raton_coordy):

        if raton_coordx > self.rect.x and raton_coordx < self.rect.x + self.rect.width                and raton_coordy > self.rect.y and raton_coordy < self.rect.y + self.rect.height:

            return True
