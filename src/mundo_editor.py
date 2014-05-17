import os
from mapa_editor import Mapa


class Mundo(object):

    def __init__(self, nombre):

        self.mapa = Mapa()
        self.tiles_suelos1 = self.mapa.crear_tiles_suelos()
        self.tiles_paredes = self.mapa.crear_tiles_paredes()
        self.tiles_tejados = self.mapa.crear_tiles_tejados()
        self.tiles_enemigos = self.mapa.crear_tiles_enemigos()
        #self.cargar_mapa("mapa_default.txt")
        self.default()
        self.ruta_mapas = "/mapas/"
        self.path = os.getcwd()
        self.aut_save = True
        self.nombre = nombre

        self.capa = 1
        self.grupo_mundo = self.mapa.grupo_mundo
        #self.grupo_enemigos = self.mapa.grupo_enemigos
        self.modo_entidad = False

    def clear_arrays(self):

        self.mapa_suelos1 = []
        self.mapa_paredes = []
        self.mapa_tejados = []
        self.mapa_enemigos = []
        self.mapa.clear_arrays()

    def default(self):

        self.nombre = "default"
        self.mapa.crear_mapa(30, 30)
        self.mapa.layer1 = []
        self.mapa.layer2 = []
        self.mapa.layer3 = []
        self.mapa_suelos1 = self.mapa.parsear_suelos()
        self.mapa_paredes = self.mapa.parsear_paredes()
        self.mapa_tejados = self.mapa.parsear_tejados()
        self.mapa_enemigos = self.mapa.parsear_enemigos()

    def nuevo_mundo(self, nombre, tamx, tamy):

        #self.clear_arrays()
        # parece que layer1 no se vacia bien con self.mapa.clear_arrays()
        self.nombre = nombre
        self.mapa.grupo_mundo.empty()
        self.mapa.crear_mapa(tamx, tamy)
        self.mapa.layer1 = []
        self.mapa.layer2 = []
        self.mapa.layer3 = []
        self.mapa_suelos1 = []
        self.mapa_paredes = []
        self.mapa_tejados = []
        self.mapa_enemigos = []
        self.mapa_suelos1 = self.mapa.parsear_suelos()
        self.mapa_paredes = self.mapa.parsear_paredes()
        self.mapa_tejados = self.mapa.parsear_tejados()
        self.mapa_enemigos = self.mapa.parsear_enemigos()
        #print "tam grupo enemigos nuevo " + str(len(self.mapa.grupo_mundo))

    def cargar_mapa(self, fichero):

        #self.clear_arrays()
        self.mapa.grupo_mundo.empty()
        self.mapa.layer1 = []
        self.mapa.layer2 = []
        self.mapa.layer3 = []
        self.tiles_suelos1 = []
        self.tiles_paredes = []
        self.tiles_tejados = []
        self.tiles_enemigos = []
        self.mapa.leer_ascii_map(fichero, self.nombre)
        self.mapa_suelos1 = self.mapa.parsear_suelos()
        self.mapa_paredes = self.mapa.parsear_paredes()
        self.mapa_tejados = self.mapa.parsear_tejados()
        self.mapa_enemigos = self.mapa.parsear_enemigos()
        #print "tam grupo enemigos cargar " + str(len(self.mapa.grupo_mundo))

    def grabar(self, nombre):

        total = self.path + self.ruta_mapas + nombre + ".txt"
        ### mapa suelos
        mapa = open(total, 'w')
        mapa.write(self.nombre + '\n')
        mapa.write('@end_nombre\n')

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




