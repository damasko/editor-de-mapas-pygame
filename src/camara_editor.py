
import pygame
from pygame.locals import *
from tile_editor import Tile
from pincel import Pincel
from operator import attrgetter


class Camara(pygame.sprite.Sprite):

    def __init__(self, mundo, raton, tam=(200, 200)):
        super(Camara, self).__init__()
        self.mundo = mundo

        self.raton = raton
        self.tam = tam

        self.tilex_ini = 0
        self.tiley_ini = 0

        self.velocidad = 20
        self.restox = 0
        self.restoy = 0

        self.rect = pygame.rect.Rect(0, 0, (tam[0] / 2), 2 * tam[1] / 3)
        ### importante el tam minimo del mapa debe ser como poco el tam de la camara
        self.tam_minx = self.rect.x / 32 + 1
        self.tam_miny = self.rect.y / 32 + 1

        self.rect_left = pygame.rect.Rect(0, 0, self.rect.width / 4, self.rect.height)
        self.rect_top = pygame.rect.Rect(0, 0, self.rect.width,
                                            self.rect.height / 4)
        self.rect_right = pygame.rect.Rect(self.rect.width - self.rect.width / 4,
             0, self.rect.width / 4, self.rect.height)
        self.rect_bottom = pygame.rect.Rect(0, self.rect.height - self.rect.height / 4,
             self.rect.width, self.rect.height / 4)

        self.surface = pygame.surface.Surface((self.rect.width,
                                                self.rect.height)).convert()
        ## Rect para comprobar el raton
        self.rectangulo = self.surface.get_rect()
        self.rectangulo.move_ip(0, 0)

        self.finx = False
        self.finy = False
        self.mostrar_capa3 = True
        self.mostrar_capa4 = True
        self.grupo_mundo = self.mundo.grupo_mundo
        self.entes = []
        self.pincel = Pincel()

    def update(self, tile_seleccionado):

        if self.focused():
            self.pincel.update()
            if self.mundo.modo_entidad and self.pincel.borrar:

                coordx = self.get_coord()[0] / 32
                coordy = self.get_coord()[1] / 32
                self.pincel.borra_enemigo(coordx, coordy, self.mundo)

            posx = 0
            posy = 0

            # monstruosidad :D maneja la camara

            if pygame.mouse.get_pressed()[2] and self.raton.puntero.colliderect(self.rect_left) and self.rect.x > 0:
                posx = -self.velocidad
            if pygame.mouse.get_pressed()[2] and self.raton.puntero.colliderect(self.rect_top) and self.rect.y > 0:
                posy = -self.velocidad
            if pygame.mouse.get_pressed()[2] and self.raton.puntero.colliderect(self.rect_right) and self.rect.bottomright[0] / 32 < len(self.mundo.mapa_suelos1[0]):
                posx = +self.velocidad
            if pygame.mouse.get_pressed()[2] and self.raton.puntero.colliderect(self.rect_bottom) and self.rect.bottomright[1] / 32 < len(self.mundo.mapa_suelos1):
                posy = +self.velocidad

            if pygame.mouse.get_pressed()[0]:
                self.set_tile(tile_seleccionado)

            self.entes_visibles()
            self.rect.move_ip(posx, posy)

    def focused(self):

        if self.rectangulo.colliderect(self.raton.puntero):
            return True

    def set_tile(self, tile_seleccionado):

        coordx = self.get_coord()[0] / 32
        coordy = self.get_coord()[1] / 32

        if self.mundo.capa == 1:

            capa_activa = self.mundo.mapa_suelos1

        elif self.mundo.capa == 3:

            capa_activa = self.mundo.mapa_paredes

        else:

            capa_activa = self.mundo.mapa_tejados

        self.pincel.rellena(tile_seleccionado, capa_activa, self.mundo,
                                        coordx, coordy, self.mundo.modo_entidad)

    def tile_base(self, tile_activo):

        if not self.mundo.modo_entidad:

            if self.mundo.capa == 1:
                for i in range(len(self.mundo.mapa_suelos1)):
                    for j in range(len(self.mundo.mapa_suelos1[0])):

                        tile = Tile()
                        tile.surface = tile_activo.surface
                        tile.x = self.mundo.mapa_suelos1[i][j].x
                        tile.y = self.mundo.mapa_suelos1[i][j].y
                        tile.nombre = tile_activo.nombre
                        tile.tipo = tile_activo.tipo
                        tile.caminable = tile_activo.caminable
                        self.mundo.mapa_suelos1[i][j] = tile

            elif self.mundo.capa == 3:

                for i in range(len(self.mundo.mapa_paredes)):
                    for j in range(len(self.mundo.mapa_paredes[0])):

                        tile = Tile()
                        tile.surface = tile_activo.surface
                        tile.x = self.mundo.mapa_suelos1[i][j].x
                        tile.y = self.mundo.mapa_suelos1[i][j].y
                        tile.nombre = tile_activo.nombre
                        tile.tipo = tile_activo.tipo
                        tile.caminable = tile_activo.caminable
                        self.mundo.mapa_paredes[i][j] = tile

            else:

                for i in range(len(self.mundo.mapa_tejados)):
                    for j in range(len(self.mundo.mapa_tejados[0])):

                        tile = Tile()
                        tile.surface = tile_activo.surface
                        tile.x = self.mundo.mapa_suelos1[i][j].x
                        tile.y = self.mundo.mapa_suelos1[i][j].y
                        tile.nombre = tile_activo.nombre
                        tile.tipo = tile_activo.tipo
                        tile.caminable = tile_activo.caminable
                        self.mundo.mapa_tejados[i][j] = tile

    def recargar(self, mundo):

        self.__init__(mundo, self.raton, self.tam)

    def set_pos(self, x, y):

        self.rect.move(x, y)

    def get_coord(self):

        coord = []
        x = pygame.mouse.get_pos()[0] + self.rect.x
        coord.append(x)
        y = pygame.mouse.get_pos()[1] + self.rect.y
        coord.append(y)
        return coord

    def render(self):

        # con esto acotamos un tile, y con el resto la posicion exacta para hacer el blit
        self.tilex_ini = self.rect.x / 32
        self.restox = self.rect.x % 32
        self.tiley_ini = self.rect.y / 32
        self.restoy = self.rect.y % 32

        self.finx = False
        self.finy = False
        # comprobacion de que no dibujamos fuera de la camara
        if self.rect.bottomright[0] / 32 == len(self.mundo.mapa_suelos1[0]):
            self.finx = True

        if self.rect.bottomright[1] / 32 == len(self.mundo.mapa_suelos1):
            self.finy = True

        if self.finx:
            self.tilex_max = self.rect.bottomright[0] / 32
        else:
            self.tilex_max = (self.rect.bottomright[0] / 32) + 1

        if self.finy:
            self.tiley_max = self.rect.bottomright[1] / 32
        else:

            self.tiley_max = (self.rect.bottomright[1] / 32) + 1
        self.surface.fill((0, 0, 0))
        if self.mundo.capa == 1:

            for i in range(self.tiley_ini, self.tiley_max):
                for j in range(self.tilex_ini, self.tilex_max):
                    self.surface.blit(self.mundo.mapa_suelos1[i][j].surface,
                     (self.mundo.mapa_suelos1[i][j].x - self.rect.x,
                          self.mundo.mapa_suelos1[i][j].y - self.rect.y))
            for ente in self.entes:
                if ente.capa == 1:
                    self.surface.blit(ente.surface, (ente.rect.x - self.rect.x,
                                ente.rect.y - self.rect.y))

        elif self.mundo.capa == 3:
            for i in range(self.tiley_ini, self.tiley_max):
                for j in range(self.tilex_ini, self.tilex_max):
                    self.surface.blit(self.mundo.mapa_suelos1[i][j].surface,
                     (self.mundo.mapa_suelos1[i][j].x - self.rect.x,
                          self.mundo.mapa_suelos1[i][j].y - self.rect.y))
                    if self.mostrar_capa3:
                        self.surface.blit(self.mundo.mapa_paredes[i][j].surface,
                             (self.mundo.mapa_paredes[i][j].x - self.rect.x,
                                  self.mundo.mapa_paredes[i][j].y - self.rect.y))

            for ente in self.entes:
                if ente.capa == 1:
                    self.surface.blit(ente.surface, (ente.rect.x - self.rect.x,
                                ente.rect.y - self.rect.y))
        else:
            if self.mundo.capa == 4:
                for i in range(self.tiley_ini, self.tiley_max):
                    for j in range(self.tilex_ini, self.tilex_max):
                        self.surface.blit(self.mundo.mapa_suelos1[i][j].surface,
                         (self.mundo.mapa_suelos1[i][j].x - self.rect.x,
                              self.mundo.mapa_suelos1[i][j].y - self.rect.y))
                        self.surface.blit(self.mundo.mapa_paredes[i][j].surface,
                         (self.mundo.mapa_paredes[i][j].x - self.rect.x,
                              self.mundo.mapa_paredes[i][j].y - self.rect.y))

                for ente in self.entes:
                    if ente.capa == 1:
                        self.surface.blit(ente.surface, (ente.rect.x - self.rect.x,
                                        ente.rect.y - self.rect.y))

                if self.mostrar_capa4:
                    for i in range(self.tiley_ini, self.tiley_max):
                        for j in range(self.tilex_ini, self.tilex_max):
                            self.surface.blit(self.mundo.mapa_tejados[i][j].surface,
                                (self.mundo.mapa_tejados[i][j].x - self.rect.x,
                                self.mundo.mapa_tejados[i][j].y - self.rect.y))

                for ente in self.entes:
                    if ente.capa == 4:
                        self.surface.blit(ente.surface, (ente.rect.x - self.rect.x,
                            ente.rect.y - self.rect.y))

        if self.focused():
            self.pincel.rect.clamp_ip(self.raton.puntero)
            self.surface.blit(self.pincel.surface, (self.pincel.rect.x, self.pincel.rect.y))

        #pygame.draw.rect(self.surface, (255, 0, 0), self.rect_left)
        #pygame.draw.rect(self.surface, (255, 255, 0), self.rect_top)
        #pygame.draw.rect(self.surface, (0, 255, 0), self.rect_right)
        #pygame.draw.rect(self.surface, (0, 0, 255), self.rect_bottom)

        return self.surface

    def entes_visibles(self):

        self.entes = pygame.sprite.spritecollide(self, self.grupo_mundo, False)
        # en el editor quiza se puede coger todo el array de entes y ordenarlo
        # por cada ente nuevo, en cambio en el juego se requerira que este
        # constantemente ordenandose, ya que los entes cambiaran de posicion
        self.entes = sorted(self.entes, key=attrgetter('rect.y'))





