import pygame


class Tileset(object):

    def __init__(self, imagen, tilesize_x, tilesize_y):

        self.imagen = imagen
        self.tilesize_x = tilesize_x
        self.tilesize_y = tilesize_y
        self.array = []
        #self.cortar_tileset()
        self.tiles_cortados = []
        self.colorkey = (255, 0, 255)

    def cortar_tileset(self):

        self.imagen = pygame.image.load(self.imagen).convert_alpha()
        self.imagen.set_colorkey(self.colorkey)
        imagen_ancho, imagen_alto = self.imagen.get_size()

        for y in range(0, imagen_alto / self.tilesize_x):
            linea = []
            self.array.append(linea)
            for x in range(0, imagen_ancho / self.tilesize_y):
                rect = (x * self.tilesize_x, y * self.tilesize_y,
                     self.tilesize_x, self.tilesize_y)

                linea.append(self.imagen.subsurface(rect))

        return self.array

