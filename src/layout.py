import pygame


class Layout(object):

    def __init__(self, tamx=50, tamy=50, posx=0, posy=0, filas=1, columnas=1):
        super(Layout, self).__init__()
        self.rect_array = []
        self.bool_array = []
        self.posx = posx
        self.posy = posy
        self.tamx = tamx
        self.tamy = tamy
        self.filas = filas
        self.columnas = columnas


class GridLayout(object):

    def __init__(self, tamx=50, tamy=50, posx=0, posy=0, filas=1, columnas=1):

        #super(GridLayout, self).__init__()
        if filas == 0:
            filas = 1
        if columnas == 0:
            columnas = 1
        self.rect_array = []
        self.bool_array = []
        self.posx = posx
        self.posy = posy
        self.tamx = tamx
        self.tamy = tamy
        self.filas = filas
        self.columnas = columnas
        self.build()

    def build(self):

        for i in range(self.filas):
            linea = []
            linea_bool = []
            for j in range(self.columnas):
                rect = pygame.rect.Rect(self.posx + j * self.tamx,
                    self.posy + i * self.tamy, self.tamx, self.tamy)
                #rect.move_ip(self.posx + j * self.tamx,
                            #self.posy + i * self.tamy)
                linea.append(rect)
                linea_bool.append(False)
            self.rect_array.append(linea)
            self.bool_array.append(linea_bool)

    def add(self, nsprite):

        pygame.transform.scale(nsprite.surface, (self.tamx, self.tamy)).convert()
        nsprite.rect = nsprite.surface.get_rect()
        encontrado = False
        i = 0
        j = 0
        while not encontrado and i < len(self.bool_array):

            while not encontrado and j < len(self.bool_array[0]):
                if not self.bool_array[i][j]:
                    self.bool_array[i][j] = True
                    nsprite.rect = self.rect_array[i][j]
                    nsprite.rect.move_ip(self.rect_array[i][j].x, self.rect_array[i][j].y)
                    #self.rect_array.append(nsprite)
                    encontrado = True

                j += 1
            i += 1

    #def dibuja():

        #for linea in self.rect_array:
            #for