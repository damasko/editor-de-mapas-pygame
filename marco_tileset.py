import pygame
from pygame.locals import *
from tile_editor import Tile
from enemigo_editor import Enemigo


class MarcoTileset(pygame.sprite.Sprite):

    ### Leccion aprendida: nunca metas un submenu dentro de un menu cuando funcionan ambos
    ### sobre la pantalla, mejor ponlos al mismo nivel y ajustalos para que parezca que uno
    ### esta dentro de otro (problemas con colisiones)

    def __init__(self, mundo, raton):

        super(MarcoTileset, self).__init__()
        self.mundo = mundo

        self.tiles_suelos = self.mundo.tiles_suelos1
        self.tiles_paredes = self.mundo.tiles_paredes
        self.tiles_tejados = self.mundo.tiles_tejados
        self.tiles_enemigos = self.mundo.tiles_enemigos
        self.raton = raton
        self.copia_tiles = []
        self.copia_tiles_paredes = []
        self.copia_tiles_tejados = []
        self.copia_tiles_enemigos = []
        self.miniatura()
        self.miniatura_l2()
        self.miniatura_l3()
        self.miniatura_enemigos()
        self.surface = pygame.surface.Surface((len(self.copia_tiles[0]) * 16,
                             len(self.copia_tiles) * 16))
        self.tile_seleccionado_suelos = self.tiles_suelos[0][0]
        self.tile_seleccionado_paredes = self.tiles_paredes[0][0]
        self.tile_seleccionado_tejados = self.tiles_tejados[0][0]
        self.tile_seleccionado_enemigos = self.tiles_enemigos[0][0]
        self.offsetx = 0
        self.offsety = 0
        self.rect = self.surface.get_rect()
        self.capa = 1
        self.default = False
        self.default1 = self.tiles_suelos[31][31]
        self.default2 = self.tiles_paredes[31][31]
        self.default3 = self.tiles_tejados[31][31]
        self.default4 = self.tiles_enemigos[0][0]
        self.modo_entidad = False

    def miniatura(self):

        x = 0
        y = 0
        for fila in self.tiles_suelos:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                tile.surface = elemento.surface.copy()
                tile.surface = pygame.transform.scale(tile.surface,
                            (tile.surface.get_width() / 2, tile.surface.get_height() / 2))
                tile.rect = tile.surface.get_rect()
                tile.rect.move_ip(x, y)
                linea.append(tile)
                x = x + 16
            self.copia_tiles.append(linea)
            y = y + 16

        return self.copia_tiles

    def miniatura_l2(self):

        x = 0
        y = 0
        for fila in self.tiles_paredes:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                tile.surface = elemento.surface.copy()
                tile.surface = pygame.transform.scale(tile.surface,
                        (tile.surface.get_width() / 2, tile.surface.get_height() / 2))
                tile.rect = tile.surface.get_rect()
                tile.rect.move_ip(x, y)
                linea.append(tile)
                x = x + 16
            self.copia_tiles_paredes.append(linea)
            y = y + 16

    def miniatura_l3(self):

        x = 0
        y = 0
        for fila in self.tiles_tejados:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                tile.surface = elemento.surface.copy()
                tile.surface = pygame.transform.scale(tile.surface,
                        (tile.surface.get_width() / 2, tile.surface.get_height() / 2))
                tile.rect = tile.surface.get_rect()
                tile.rect.move_ip(x, y)
                linea.append(tile)
                x = x + 16
            self.copia_tiles_tejados.append(linea)
            y = y + 16

        return self.copia_tiles_tejados

    def miniatura_enemigos(self):

        x = 0
        y = 0
        for fila in self.tiles_enemigos:
            x = 0
            linea = []
            for elemento in fila:
                enemigo = Enemigo()
                enemigo.surface = elemento.surface.copy()
                enemigo.surface = pygame.transform.scale(enemigo.surface,
                     (enemigo.surface.get_width() / 2, enemigo.surface.get_height() / 2))
                enemigo.rect = enemigo.surface.get_rect()
                enemigo.rect.move_ip(x, y)
                linea.append(enemigo)
                x = x + 32
            self.copia_tiles_enemigos.append(linea)
            y = y + 32

        return self.copia_tiles_enemigos

    def centrarx(self, rect_root, offsety):

        self.offsety = offsety
        self.offsetx = (rect_root.width - self.rect.width) / 2
        self.rect.move_ip(self.offsetx, offsety)

    def focused(self, coordx, coordy, offsetx, offsety):
        # la madre que le pario al colliderect
        x = False
        y = False

        if coordx > self.rect.x or self.rect.width < coordx - self.offsetx:
            x = True
        if coordy > self.rect.y or self.rect.height < coordy - self.offsety :
            y = True
        if x and y:

            return True

    def update(self):
        ## cuando termines poner elses
        self.surface.fill((0, 0, 0))
        if not self.modo_entidad:
            if self.capa == 1:
                tiles_min = self.copia_tiles
            elif self.capa == 3:
                tiles_min = self.copia_tiles_paredes
            elif self.capa == 4:
                tiles_min = self.copia_tiles_tejados
            if self.default:

                if self.capa == 1:
                    self.tile_seleccionado_suelos = self.default1
                elif self.capa == 3:
                    self.tile_seleccionado_paredes = self.default2
                else:
                    self.tile_seleccionado_tejados = self.default3
                self.default = False

        else:

            tiles_min = self.copia_tiles_enemigos
            if self.default:
                self.tile_seleccionado_enemigos = self.tiles_enemigos[15][15]

        for fila in tiles_min:
            for tile in fila:
                self.surface.blit(tile.surface, (tile.rect.x, tile.rect.y))
            ### anadir los else

    def get_tileselec(self, coord):


        if pygame.mouse.get_pressed()[0]:
            if not self.modo_entidad:
                tilex = coord[0] / 16
                tiley = coord[1] / 16
                # dejar es try ya que si accede fuera de la miniatura tira error de indice
                try:
                    if self.capa == 1:

                        self.tile_seleccionado_suelos = self.tiles_suelos[tiley][tilex]

                    elif self.capa == 3:

                        self.tile_seleccionado_paredes = self.tiles_paredes[tiley][tilex]

                    else:

                        self.tile_seleccionado_tejados = self.tiles_tejados[tiley][tilex]

                except:
                    pass

            else:
                try:
                    tilex = coord[0] / 32
                    tiley = coord[1] / 32
                    self.tile_seleccionado_enemigos = self.tiles_enemigos[tiley][tilex]

                except:
                    pass





