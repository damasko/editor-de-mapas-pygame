import pygame


class Boton(object):

    def __init__(self, tamx, tamy, posx, posy, texto, imagen="boton.png",
                 imagen_click=None):

        ### imagen, surface y rect
        if not imagen:
            self.surface = pygame.surface.Surface((tamx, tamy)).convert()
        else:
            self.surface = pygame.image.load(imagen).convert()

        if not imagen_click:
            self.surface_click = self.surface
        else:
            self.surface_click = self.surface

        self.surface = pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        self.surface_click = pygame.transform.scale(self.surface, (tamx, tamy)).convert()
        if not posx:
            self.posx = 0
        else:
            self.posx = posx
        if not posy:
            self.posy = 0
        else:
            self.posy = posy

        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.posx, self.posy)

        ### texto
        self.texto = texto
        self.texto_x = 0
        self.texto_y = 0
        pygame.font.init()
        self.color_texto = (255, 150, 0)
        self.fuente = pygame.font.Font("fuente3.ttf", 30)
        self.offset_x = tamx / 3
        self.offset_y = tamy / 3
        self.centrar_texto()
        ### funcion externa para bindear
        self.funcion_externa = None

    def set_fuente(self, archivo_ttf, tam):

        self.fuente = pygame.font.Font(archivo_ttf, tam)

    def centrarx(self, rect_raiz, posy):

        self.rect.centerx = rect_raiz.centerx
        self.rect.centery = posy
        #self.rect.move(posicionx, posy)

    def centrar_texto(self):

        self.texto_tam = self.fuente.size(self.texto)

        self.texto_x = (self.surface.get_size()[0] - self.texto_tam[0]) / 2
        self.texto_y = (self.surface.get_size()[1] - self.texto_tam[1]) / 2

    def set_coord(self, nx, ny):
        self.rect.x = nx
        self.rect.y = ny

    def imprime(self):

        self.surface.blit(self.fuente.render(self.texto,
                    True, self.color_texto), (self.texto_x, self.texto_y))
        self.surface.blit(self.surface, (0, 0))

    def raton_encima(self, raton_rect):
        if self.rect.colliderect(raton_rect):
            return True

    def click(self, raton_rect):

        if  pygame.mouse.get_pressed()[0] and self.rect.colliderect(raton_rect):
            #surface_copia = self.surface
            self.surface = self.surface_click
            #self.surface_click = surface_copia
            #self.color_texto = (100,100,100)

            try:
                self.funcion_externa()

            except:
                print "el boton debe estar bindeado a una funcion!!"

    def bind(self, funcion_externa):

        self.funcion_externa = funcion_externa





