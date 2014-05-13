import pygame


class Boton(object):

    def __init__(self, tamx, tamy, posx, posy, texto, imagen="res/boton_1.png",
                 imagen_click="res/boton_2.png"):

        ### imagen, surface y rect

        if not imagen:
            self.surface_normal = pygame.surface.Surface((tamx, tamy))
        else:
            self.surface_normal = pygame.image.load(imagen)

        if not imagen_click:
            self.surface_click = pygame.surface.Surface((tamx, tamy))
        else:

            self.surface_click = pygame.image.load(imagen_click)

        self.surface_normal = pygame.transform.scale(self.surface_normal,
                    (tamx, tamy)).convert()
        self.surface_click = pygame.transform.scale(self.surface_click,
                    (tamx, tamy)).convert()
        self.surface = self.surface_normal
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
        self.color_texto = (255, 0, 0)
        self.fuente = pygame.font.Font("res/font/fuente3.ttf", 30)
        self.offset_x = tamx / 3
        self.offset_y = tamy / 3
        self.centrar_texto()
        ### funcion externa para bindear
        self.funcion_externa = None
        self.variable = 0

    def set_fuente(self, archivo_ttf, tam):

        self.fuente = pygame.font.Font(archivo_ttf, tam)

    def centrarx(self, rect_raiz):

        self.rect.centerx = rect_raiz.width/2

    def centrary(self, rect_raiz):

        self.rect.centery = rect_raiz.centery

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


    def focused(self, raton_coordx, raton_coordy):

        if raton_coordx > self.rect.x and raton_coordx < self.rect.x + self.rect.width               and raton_coordy > self.rect.y and raton_coordy < self.rect.y + self.rect.height:

            return True

    def click(self, raton_coordx, raton_coordy):

        self.variable = 0
        #lo mejor sera al final que los botones no vayan dentro del menu sino sobre
        #la propia pantalla

        if self.focused(raton_coordx, raton_coordy):

            self.surface = self.surface_click
            self.color_texto = (180, 0, 0)

            if pygame.mouse.get_pressed()[0]:

            #surface_copia = self.surface

                try:
                    #self.funcion_externa

                    self.toggle_variable()

                except:

                    print "el boton debe estar bindeado a una funcion!!"

        else:

            self.surface = self.surface_normal
            self.color_texto = (255, 0, 0)

    def bind(self, funcion_externa):

        self.funcion_externa = funcion_externa

    def toggle_variable(self):

        #if self.variable == 0:

        self.variable = 1

        #else:
            #self.variable = 0






