import pygame
from tile_editor import Tile
from enemigo_editor import Enemigo


class Pincel(pygame.sprite.Sprite):

    def __init__(self):
        super(Pincel, self).__init__()
        self.surface = pygame.image.load("pincel.png").convert_alpha()
        self.surface_1 = pygame.image.load("pincel.png").convert_alpha()
        self.surface_2 = pygame.image.load("pincel2.png").convert_alpha()
        self.surface_3 = pygame.image.load("pincel3.png").convert_alpha()
        #self.tile_seleccionado = tile_seleccionado
        self.array = []
        self.rect = self.surface.get_rect()
        self.tam = 1
        self.array_deshacer = []
        self.borrar = False
        self.tile_mapa = False

    def update(self):

        #for event in pygame.event.get():
        #if self.rect
        #self.array_undo = []

        if self.tam == 1:
            self.surface = self.surface_1
            self.rect = self.surface.get_rect()
        elif self.tam == 2:
            self.surface = self.surface_2
            self.rect = self.surface.get_rect()
        else:
            self.surface = self.surface_3
            self.rect = self.surface.get_rect()

    def rellena(self, tile_seleccionado, arraymap, mundo, coordx, coordy, modo_entidad):

        # Debido a la naturaleza de la camara, se hace dificil
        # trabajar con colisiones (el raton esta sobre la pantalla principal,
        # mientras que la camara se mueve por otra surface, por lo cual
        # la colision he decidido hacerla a mano, aunque es mucho
        # menos eficiente

        if not modo_entidad:

            if self.tam == 1:

                try:
                    tile = Tile()
                    tile.surface = tile_seleccionado.surface.copy()
                    tile.rect = tile.surface.get_rect()
                    tile.rect.move_ip(coordx * 32, coordy * 32)
                    tile.nombre = tile_seleccionado.nombre
                    tile.tipo = tile_seleccionado.tipo
                    tile.caminable = tile_seleccionado.caminable
                    #self.array_undo.append(arraymap[coordy][coordx])
                    arraymap[coordy][coordx] = tile
                except:
                    pass

            if self.tam == 2:

                inix = coordx - 1
                iniy = coordy - 1
                if inix < 0:
                    inix = 0
                if iniy < 0:
                    iniy = 0

                for i in range(iniy, coordy + 2):
                    for j in range(inix, coordx + 2):
                        try:

                            tile = Tile()
                            tile.surface = tile_seleccionado.surface.copy()
                            tile.rect = tile.surface.get_rect()
                            tile.rect.move_ip(j * 32, i * 32)
                            tile.nombre = tile_seleccionado.nombre
                            tile.tipo = tile_seleccionado.tipo
                            tile.caminable = tile_seleccionado.caminable
                            #self.array_undo.append(arraymap[coordy][coordx])
                            arraymap[i][j] = tile

                        except:
                            pass

            if self.tam == 3:

                inix = coordx - 2
                iniy = coordy - 2
                if inix < 0:
                    if coordx - 1 < 0:
                        inix = 0
                    else:
                        inix = coordx - 1
                if iniy < 0:
                    if coordy - 1 < 0:
                        iniy = 0
                    else:
                        iniy = coordy - 1

                for i in range(iniy, coordy + 3):
                    for j in range(inix, coordx + 3):
                        try:

                            tile = Tile()
                            tile.surface = tile_seleccionado.surface.copy()
                            tile.rect = tile.surface.get_rect()
                            tile.rect.move_ip(j * 32, i * 32)
                            tile.nombre = tile_seleccionado.nombre
                            tile.tipo = tile_seleccionado.tipo
                            tile.caminable = tile_seleccionado.caminable
                            arraymap[i][j] = tile

                        except:
                            pass

        else:

                # Renombrar tile_seleccionado a algo mas generico
            if not self.borrar:

                coordx = coordx * 32
                coordy = coordy * 32

                try:
                    # comprobacion para no poner 2 enemigos en un mismo punto
                    # comprueba la posx, posy y si estan en la misma capa
                    # aunque mas engorroso, mejor un while para hacer una busqueda
                    # OJO, el enemigo en la pos 0, esta en el -16, en principio
                    # ahi no deberia de dibujarse, pero si da problemas
                    # puede ser eso
                    existe = False
                    try:
                        encontrado = False
                        i = 0
                        while not encontrado and i < len(mundo.mapa_enemigos):
                            if mundo.mapa_enemigos[i].rect.x == coordx - 16 and mundo.mapa_enemigos[i].rect.y == coordy - 32 and mundo.mapa_enemigos[i].capa == mundo.capa:
                                existe = True
                                encontrado = True
                            i += 1

                    except:

                        existe = False

                    if not existe:

                        enemigo = Enemigo()
                        enemigo.surface = tile_seleccionado.surface.copy()
                        enemigo.rect = enemigo.surface.get_rect()
                        enemigo.rect.move_ip(coordx - 16, coordy - 32)
                        enemigo.nombre = tile_seleccionado.nombre
                        enemigo.capa = mundo.capa
                        mundo.mapa_enemigos.append(enemigo)
                        mundo.grupo_mundo.add(enemigo)

                except:
                    pass

    def borra_enemigo(self, coordx, coordy, mundo):

        if pygame.mouse.get_pressed()[0]:
            coordx = coordx * 32
            coordy = coordy * 32
            if len(mundo.mapa_enemigos) > 0:
                i = 0
                encontrado = False
                while not encontrado and i < len(mundo.mapa_enemigos):

                    if mundo.mapa_enemigos[i].rect.x == coordx - 16 and mundo.mapa_enemigos[i].rect.y == coordy - 32 and mundo.mapa_enemigos[i].capa == mundo.capa:

                        mundo.grupo_mundo.remove(mundo.mapa_enemigos[i])
                        del mundo.mapa_enemigos[i]
                        encontrado = True
                    i += 1

    #def get_tile_mapa(self, tile_activo, coordx, coordy, mundo):
        ## coger un tile del mapa para usarlo como default
        #if pygame.mouse.get_pressed()[0]:
            ##coordx = coordx * 32
            ##coordy = coordy * 32
            #tile = Tile()

            #if mundo.capa == 1:

                #tile.surface = mundo.mapa_suelos1[coordy][coordx].surface.copy()
                #tile.nombre = mundo.mapa_suelos1[coordy][coordx].nombre
                #tile.tipo = mundo.mapa_suelos1[coordy][coordx].tipo
                #tile.caminable = mundo.mapa_suelos1[coordy][coordx].caminable

            #elif mundo.capa == 2:

                #tile.surface = mundo.mapa_paredes[coordy][coordx].surface.copy()
                #tile.nombre = mundo.mapa_paredes[coordy][coordx].nombre
                #tile.tipo = mundo.mapa_paredes[coordy][coordx].tipo
                #tile.caminable = mundo.mapa_paredes[coordy][coordx].caminable

            #else:

                #tile.surface = mundo.mapa_tejados[coordy][coordx].surface.copy()
                #tile.nombre = mundo.mapa_tejados[coordy][coordx].nombre
                #tile.tipo = mundo.mapa_tejados[coordy][coordx].tipo
                #tile.caminable = mundo.mapa_tejados[coordy][coordx].caminable

            #self.tile_mapa = False

            #tile_activo = tile



