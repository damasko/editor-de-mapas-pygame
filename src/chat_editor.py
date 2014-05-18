import pygame
from pygame.locals import *
from tile_editor import Tile
#from enemigo_editor import Enemigo

class Chat(object):

    def __init__(self, pantalla_tam, tile_seleccionado, capa,
                        modo_entidad, borrar, autosave, mundo):

        # Rehacer esta clase

        self.surface = pygame.image.load("res/chat.png").convert()
        self.surface = pygame.transform.scale(self.surface, (pantalla_tam[0] / 2,
                        pantalla_tam[1] / 3)).convert()
        self.rect = self.surface.get_rect()

        self.rect.move_ip(0, 2 * pantalla_tam[1] / 3)
        self.tile_seleccionado = tile_seleccionado

        self.capa = capa
        self.modo_entidad = modo_entidad
        self.nombre_mundo = "Nombre del mapa: " + mundo.nombre
        self.borrar = borrar
        self.text_layer = "CAPA ACTUAL: " + str(self.capa)
        self.text_tnombre = "nombre tile: " + self.tile_seleccionado.nombre
        self.text_ttipo = "tile tipo: " + self.tile_seleccionado.tipo
        self.texto_ayuda = "Pulsa F1 para la ayuda"

        if self.tile_seleccionado.caminable:
            self.text_tcaminable = "caminable: Si"
        else:
            self.text_tcaminable = "caminable: No"

        self.texto_entidad = "MODO ENTIDAD"
        self.texto_ent_borrar = " (BORRAR ENTIDAD)"
        self.autosave = autosave
        self.texto_autosave = "Autosave"

        self.offset = 16
        pygame.font.init()

        self.fuente = pygame.font.SysFont('Arial', 14)
        self.fuente2 = pygame.font.SysFont('Arial', 22)
        self.surface_texto = pygame.surface.Surface((self.rect.width - 2 * self.offset,
                             self.rect.height - 2 * self.offset)).convert(self.surface)


    def get_rect(self):
        return self.rect

    def update(self, tile_seleccionado, capa, visible2, visible3,
                    modo_entidad, borrar, autosave, mundo):
        self.tile_seleccionado = tile_seleccionado
        self.capa = capa
        self.modo_entidad = modo_entidad
        self.borrar = borrar

        ### Mucho ojo con los try, el programa puede hacer cosas raras sin que te
        # des cuenta

        if self.modo_entidad:
            if self.borrar:
                self.texto_entidad = "MODO ENTIDAD" + self.texto_ent_borrar
            else:
                self.texto_entidad = "MODO ENTIDAD"
        self.nombre_mundo = "Nombre del mapa: " + mundo.nombre
        self.text_layer = "CAPA ACTUAL: " + str(self.capa)
        if self.capa == 3 and not visible2:
            self.text_layer = self.text_layer + " (OCULTA)"
        if self.capa == 4 and not visible3:
            self.text_layer = self.text_layer + " (OCULTA)"

        if isinstance(tile_seleccionado, Tile):
            self.text_tnombre = "nombre tile: " + self.tile_seleccionado.nombre
            self.text_ttipo = "tile tipo: " + self.tile_seleccionado.tipo
            if self.tile_seleccionado.caminable:
                self.text_tcaminable = "caminable: Si"
            else:
                self.text_tcaminable = "caminable: No"
        else:

            self.text_tnombre = "nombre: " + self.tile_seleccionado.nombre
            self.text_ttipo = "vida: " + str(self.tile_seleccionado.vida)
            self.text_tcaminable = "ataque: " + str(self.tile_seleccionado.ataque)
        self.autosave = autosave

    def imprime(self):
        self.surface_texto.fill((0, 0, 0))

        self.surface_texto.blit(self.fuente.render(self.text_tnombre, True,
                                (255, 255, 255)), (self.offset, self.offset + 20))
        self.surface_texto.blit(self.fuente.render(self.text_ttipo, True,
                                (255, 255, 255)), (self.offset, self.offset + 40))
        self.surface_texto.blit(self.fuente.render(self.text_tcaminable, True,
                                 (255, 255, 255)), (self.offset, self.offset + 80))
        self.surface_texto.blit(self.fuente.render(self.texto_ayuda, True,
                                (255, 255, 255)), (self.offset, self.offset + 100))
        self.surface_texto.blit(self.fuente2.render(self.text_layer, True,
                                (0, 255, 255)), (self.offset, self.offset + 120))
        self.surface_texto.blit(self.fuente.render(self.nombre_mundo, True,
                                (255, 255, 255)), (self.offset, self.offset + 140))
        if self.modo_entidad:
            self.surface_texto.blit(self.fuente.render(self.texto_entidad, True,
                            (255, 255, 255)), (self.offset + 200, self.offset + 200))

        self.surface_texto.blit(self.tile_seleccionado.surface,
                                    (self.rect.width - 130, 10))
        if self.autosave:

            self.surface_texto.blit(self.fuente.render(self.texto_autosave, True,
                            (255, 255, 255)), (self.offset, self.offset + 200))

        self.surface.blit(self.surface_texto, (self.offset, self.offset))




