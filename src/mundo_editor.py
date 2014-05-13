import os
from mapa_editor import Mapa


class Mundo(object):

    def __init__(self, nombre):

        self.mapa = Mapa()
        self.tiles_suelos1 = self.mapa.crear_tiles_suelos()
        self.tiles_paredes = self.mapa.crear_tiles_paredes()
        self.tiles_tejados = self.mapa.crear_tiles_tejados()
        self.tiles_enemigos = self.mapa.crear_tiles_enemigos()

        self.mapa.leer_ascii_map("mapa_default.txt")
        self.mapa_suelos1 = self.mapa.parsear_suelos()
        self.mapa_paredes = self.mapa.parsear_paredes()
        self.mapa_tejados = self.mapa.parsear_tejados()
        self.mapa_enemigos = self.mapa.parsear_enemigos()

        self.ruta_mapas = "/mapas/"
        self.path = os.getcwd()
        self.aut_save = True
        self.nombre = nombre

        self.capa = 1
        self.grupo_mundo = self.mapa.grupo_mundo
        #self.grupo_enemigos = self.mapa.grupo_enemigos
        self.modo_entidad = False

    def grabar(self, nombre):

        total = self.path + self.ruta_mapas + nombre + ".txt"
        ### mapa suelos
        mapa = open(total, 'w')
        for fila in self.mapa_suelos1:
            for tile in fila:
                mapa.write(tile.tipo)
            mapa.write('\n')
        mapa.write('@end_suelos\n')
        for fila in self.mapa_paredes:
            for tile in fila:
                mapa.write(tile.tipo)
            mapa.write('\n')
        mapa.write('@end_paredes\n')
        for fila in self.mapa_tejados:
            for tile in fila:
                mapa.write(tile.tipo)
            mapa.write('\n')
        mapa.write('@end_tejados\n')
        for enemigo in self.mapa_enemigos:

            mapa.write(enemigo.nombre + " " + str(enemigo.rect.x) + " "
                    + str(enemigo.rect.y) + " " + str(enemigo.capa) + "\n")
        mapa.write('@end_enemigos')
        mapa.close()




