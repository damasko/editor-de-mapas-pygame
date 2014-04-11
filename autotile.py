#import pygame
import random


#class Autotile(pygame.sprite.Sprite):
class Autotile(object):
    def __init__(self):
        #super(Autotile, self).__init__()

        self.nombre = "default"
        #self.surface = pygame.surface.Surface((32, 32)).convert_alpha()
        #self.rect = self.surface.get_rect()
        self.tipo = "0"
        self.tipo_parent = "0"
        self.caminable = True

        self.bits = []
        for i in range(4):
            self.bits.append(0)


class ConectaAutoTiles(object):

    def __init__(self, array_posibilidades):
        self.array_posibilidades = array_posibilidades
        self.capa_autotiles = []
        self.bits_esquinas = []

    def conecta_tiles(self, tile):
        # en vez de 1 1 le debemos pasar la posicion del mapa
        self.capa_autotiles[1][1] = tile
        for i in range(len(self.capa_autotiles)):
            #print "i " + str(i)
            for j in range(len(self.capa_autotiles[0])):
                #print "j " + str(j)
                if i != 1 and j != 1:
                    #pass
                #else:
                    if i == 0 and j == 0:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[2])

                    elif i == 0 and j == 1:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[2])
                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[3])

                    elif i == 0 and j == 2:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[3])

                    elif i == 1 and j == 2:
                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[0])
                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[3])

                    elif i == 2 and j == 2:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[0])

                    elif i == 2 and j == 1:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[0])
                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[1])

                    elif i == 2 and j == 0:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[0])

                    #elif i == 1 and j == 0:
                    else:

                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[1])
                        self.bits_esquinas.append(self.capa_autotiles[i][j].bits[2])


array_posibilidades = []
tile1 = Autotile()
tile1.bits[0] = 1
array_posibilidades.append(tile1)

tile2 = Autotile()
tile2.bits[1] = 1
array_posibilidades.append(tile2)

tile3 = Autotile()
tile3.bits[2] = 1
array_posibilidades.append(tile3)

tile4 = Autotile()
tile4.bits[3] = 1
array_posibilidades.append(tile4)

tile5 = Autotile()
tile5.bits[0] = 1
tile5.bits[1] = 1
array_posibilidades.append(tile5)

tile6 = Autotile()
tile6.bits[2] = 1
tile6.bits[3] = 1
array_posibilidades.append(tile6)

tile7 = Autotile()
tile7.bits[0] = 1
tile7.bits[3] = 1
array_posibilidades.append(tile7)

tile8 = Autotile()
tile8.bits[1] = 1
tile8.bits[2] = 1
array_posibilidades.append(tile8)

tile9 = Autotile()
tile9.bits[0] = 1
tile9.bits[2] = 1
array_posibilidades.append(tile9)

tile10 = Autotile()
tile10.bits[1] = 1
tile10.bits[3] = 1
array_posibilidades.append(tile10)

tile11 = Autotile()
tile11.bits[1] = 1
tile11.bits[2] = 1
tile11.bits[3] = 1
array_posibilidades.append(tile11)

tile12 = Autotile()
tile12.bits[0] = 1
tile12.bits[2] = 1
tile12.bits[3] = 1
array_posibilidades.append(tile12)

tile13 = Autotile()
tile13.bits[0] = 1
tile13.bits[1] = 1
tile13.bits[3] = 1
array_posibilidades.append(tile13)

tile14 = Autotile()
tile14.bits[0] = 1
tile14.bits[1] = 1
tile14.bits[2] = 1
array_posibilidades.append(tile14)

tile15 = Autotile()
array_posibilidades.append(tile15)

tile16 = Autotile()
tile16.bits[0] = 1
tile16.bits[1] = 1
tile16.bits[2] = 1
tile16.bits[3] = 1
array_posibilidades.append(tile16)

autotiler = ConectaAutoTiles(array_posibilidades)
for i in range(0, 3):
    linea = []
    random_tile = random.randrange(0,15)
    for j in range(0, 3):
        tile_random = array_posibilidades[random_tile]
        linea.append(tile_random)
    autotiler.capa_autotiles.append(linea)
i = 0
for fila in autotiler.capa_autotiles:
    for tile in fila:
        print tile.bits

tile_random = array_posibilidades[random.randrange(len(array_posibilidades))]
autotiler.conecta_tiles(tile_random)

for i in autotiler.bits_esquinas:

    print i


