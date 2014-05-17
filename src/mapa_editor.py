import pygame
from tile_editor import Tile
from tileset_editor import Tileset
from enemigo_editor import Enemigo


class Mapa(object):

    def __init__(self):
        # Tilesets (surfaces)
        self.tileset1 = Tileset("res/tileset_suelos1.png", 32, 32).cortar_tileset()
        self.tileset2 = Tileset("res/tileset_paredes.png", 32, 32).cortar_tileset()
        self.tileset3 = Tileset("res/tileset_tejados.png", 32, 32).cortar_tileset()
        self.tileset_enemigos = Tileset("res/tileset_enemigos.png", 64, 64).cortar_tileset()
        # Tilesets (tiles, enemigos, npcs...)
        self.tiles_suelos1 = []
        self.tiles_paredes = []
        self.tiles_tejados = []
        self.tiles_enemigos = []
        # Mapas de txt a array de chars
        self.array_lectura_suelos = []  # <- array de chars del .txt leido
        self.array_lectura_paredes = []
        self.array_lectura_tejados = []
        self.array_lectura_enemigos = []
        # Mapas completados
        self.layer1 = []  # <- el array capa 1 o suelos
        self.layer2 = []
        self.layer3 = []
        self.enemigos = []
        # Grupos
        self.grupo_mundo = pygame.sprite.Group()
        #self.grupo_enemigos = pygame.sprite.Group()

    def crear_tiles_suelos(self):

        for i in range(len(self.tileset1)):
            linea = []
            for j in range(len(self.tileset1[0])):
                tile = Tile()
                #rect = pygame.rect.Rect((j*32, i*32), tile.surface.get_size())
                if i == 0 and j == 0:
                    #suelo arido
                    tile.nombre = "arido"
                    tile.surface = self.tileset1[0][0]
                    tile.tipo = "q"
                    tile.caminable = True
                elif i == 0 and j == 1:
                    # algo:
                    tile.nombre = "roca"
                    tile.tipo = "g"
                    tile.surface = self.tileset1[0][1]
                    tile.caminable = False
                elif i == 0 and j == 2:
                    # algo:
                    tile.nombre = "algo"
                    tile.surface = self.tileset1[0][2]
                    tile.tipo = "a"
                    tile.caminable = False
                elif i == 1 and j == 0:
                    # cesped:
                    tile.nombre = "cesped"
                    tile.surface = self.tileset1[1][0]
                    tile.tipo = "g"
                    tile.caminable = True
                elif i == 1 and j == 1:
                    # madera:
                    tile.nombre = "madera"
                    tile.surface = self.tileset1[1][1]
                    tile.tipo = "m"
                    tile.caminable = True

                elif i == 1 and j == 2:
                    tile.nombre = "suelo rocoso"
                    tile.surface = self.tileset1[1][2]
                    tile.tipo = "b"
                    tile.caminable = True

                elif i == 2 and j == 0:
                    tile.nombre = "agua chunga1"
                    tile.surface = self.tileset1[2][0]
                    tile.tipo = "u"
                    tile.caminable = False

                elif i == 2 and j == 1:
                    tile.nombre = "agua chunga2"
                    tile.surface = self.tileset1[2][1]
                    tile.tipo = "u"
                    tile.caminable = False
                elif i == 3 and j == 0:
                    tile.nombre = "agua chunga3"
                    tile.surface = self.tileset1[3][0]
                    tile.tipo = "u"
                    tile.caminable = False

                elif i == 3 and j == 1:
                    tile.nombre = "agua chunga4"
                    tile.surface = self.tileset1[3][1]
                    tile.tipo = "u"
                    tile.caminable = False

                elif i == 2 and j == 2:
                    tile.nombre = "hielo"
                    tile.surface = self.tileset1[2][2]
                    tile.tipo = "u"
                    tile.caminable = False

                elif i == 31 and j == 31:
                    tile.nombre = "default_suelo"
                    tile.surface = self.tileset1[31][31]
                    tile.tipo = "#"
                    tile.caminable = True

                linea.append(tile)
            self.tiles_suelos1.append(linea)

        return self.tiles_suelos1

    def clear_arrays(self):

        self.array_lectura_suelos = []
        self.array_lectura_paredes = []
        self.array_lectura_tejados = []
        self.array_lectura_enemigos = []
        self.layer1 = []
        self.layer2 = []
        self.layer3 = []
        self.enemigos = []

    def crear_tiles_paredes(self):
        for i in range(len(self.tileset2)):
            linea = []
            for j in range(len(self.tileset2[0])):
                tile = Tile()
                if i == 0 and j == 0:

                    tile.nombre = "pared1"
                    tile.surface = self.tileset2[0][0]
                    tile.tipo = "q"
                    tile.caminable = False
                elif i == 0 and j == 1:

                    tile.nombre = "pared2"
                    tile.tipo = "g"
                    tile.surface = self.tileset2[0][1]
                    tile.caminable = False
                elif i == 1 and j == 0:

                    tile.nombre = "pared3"
                    tile.surface = self.tileset2[0][2]
                    tile.tipo = "a"
                    tile.caminable = False
                elif i == 1 and j == 1:

                    tile.nombre = "pared4"
                    tile.surface = self.tileset2[1][0]
                    tile.tipo = "g"
                    tile.caminable = False
                elif i == 2 and j == 0:

                    tile.nombre = "pared5"
                    tile.surface = self.tileset2[1][1]
                    tile.tipo = "m"
                    tile.caminable = False
                elif i == 31 and j == 31:
                    tile.nombre = "default_pared"
                    tile.surface = self.tileset2[31][31]
                    tile.tipo = "$"
                    tile.caminable = True
                linea.append(tile)
            self.tiles_paredes.append(linea)

        return self.tiles_paredes

    def crear_tiles_tejados(self):

        for i in range(len(self.tileset3)):
            linea = []
            for j in range(len(self.tileset3[0])):
                tile = Tile()
                if i == 0 and j == 0:

                    tile.nombre = "tejado1"
                    tile.surface = self.tileset3[0][0].convert_alpha()
                    tile.tipo = "t"
                    tile.caminable = True
                elif i == 0 and j == 1:

                    tile.nombre = "tejado2"
                    tile.tipo = "g"
                    tile.surface = self.tileset3[0][1].convert_alpha()
                    tile.caminable = False
                elif i == 0 and j == 2:

                    tile.nombre = "tejado3"
                    tile.surface = self.tileset3[0][2].convert_alpha()
                    tile.tipo = "a"
                    tile.caminable = False
                elif i == 1 and j == 0:

                    tile.nombre = "tejado4"
                    tile.surface = self.tileset3[1][0].convert_alpha()
                    tile.tipo = "g"
                    tile.caminable = True
                elif i == 1 and j == 1:

                    tile.nombre = "tejado5"
                    tile.surface = self.tileset3[1][1].convert_alpha()
                    tile.tipo = "m"
                    tile.caminable = True
                elif i == 31 and j == 31:
                    tile.nombre = "default_tejado"
                    tile.surface = self.tileset3[31][31].convert_alpha()
                    tile.tipo = "&"
                    tile.caminable = True
                linea.append(tile)
            self.tiles_tejados.append(linea)

        return self.tiles_tejados

    def crear_tiles_enemigos(self):

        for i in range(len(self.tileset_enemigos)):
            linea = []
            for j in range(len(self.tileset_enemigos[0])):
                enemigo = Enemigo()
                if i == 0 and j == 0:

                    enemigo.nombre = "princesa"
                    enemigo.vida = 50
                    enemigo.ataque = 25
                    enemigo.surface = self.tileset_enemigos[0][0].convert_alpha()

                elif i == 0 and j == 1:

                    enemigo.nombre = "enemigo1"
                    enemigo.surface = self.tileset_enemigos[0][1].convert_alpha()

                elif i == 0 and j == 2:

                    enemigo.nombre = "enemigo2"
                    enemigo.surface = self.tileset_enemigos[0][2].convert_alpha()

                elif i == 0 and j == 3:

                    enemigo.nombre = "enemigo3"
                    enemigo.surface = self.tileset_enemigos[0][3].convert_alpha()

                elif i == 0 and j == 4:

                    enemigo.nombre = "enemigo4"
                    enemigo.surface = self.tileset_enemigos[0][4].convert_alpha()

                elif i == 15 and j == 15:
                    enemigo.nombre = "default_enemigo"
                    enemigo.surface = self.tileset_enemigos[15][15].convert_alpha()

                linea.append(enemigo)
            self.tiles_enemigos.append(linea)

        return self.tiles_enemigos

    def crear_mapa(self, tamy, tamx):

        # aprovechando que tanto el mapa paredes, suelos y tejados debe tener el mismo tamano
        # me aseguro reseteando los arrays aunque puede que no sea necesario mejor evitar
        # problemas
        self.clear_arrays()

        x = 0
        y = 0

        for i in range(tamy):

            x = 0
            j = 0
            linea_suelos = []  # suelos
            linea_paredes = []  # paredes
            linea_tejados = [] # tejados
            for j in range(tamx):

                tile = Tile()  # rehuso del objeto tile
                #tile.rect.move_ip(x, y)
                rect = pygame.rect.Rect((x, y), tile.surface.get_size())
                tile.x = x
                tile.y = y
                #suelos
                tile.nombre = "default_suelo"
                tile.surface = self.tileset1[31][31].subsurface(rect)
                tile.tipo = "#"
                tile.caminable = False
                linea_suelos.append(tile)

                #paredes
                #tile = Tile()
                #tile.rect.move_ip(x, y)
                tile.nombre = "default_pared"
                tile.surface = self.tileset2[31][31].subsurface(rect)
                tile.tipo = "$"
                tile.caminable = True
                linea_paredes.append(tile)

                #tejados
                #tile = Tile()
                #tile.rect.move_ip(x, y)
                tile.x = x
                tile.y = y
                tile.nombre = "default_tejado"
                tile.surface = self.tileset3[31][31].subsurface(rect)
                tile.tipo = "&"
                tile.caminable = True
                linea_tejados.append(tile)
                x = x * 32
                j += 1

            self.array_lectura_suelos.append(linea_suelos)
            self.array_lectura_paredes.append(linea_paredes)
            self.array_lectura_tejados.append(linea_tejados)

            y = y * 32
            i += 1

        self.parsear_suelos()
        self.parsear_paredes()
        self.parsear_tejados()
        self.parsear_enemigos()

    def leer_ascii_map(self, ascii_map, mundonombre):
        self.clear_arrays()
        a = open(ascii_map, 'r')

        lista = list(a)
        a.close()
        nombre = True
        suelos = True
        paredes = True
        tejados = True
        enemigos = True

        i = 2
        while i < len(lista):
            if nombre:
                if "@end_nombre" in lista[i]:
                    nombre = False
                else:
                    mundonombre = lista[i]
            if suelos:
                if "@end_suelos" in lista[i]:
                    suelos = False
                else:
                    self.array_lectura_suelos.append(lista[i].split())
            elif paredes:
                if "@end_paredes" in lista[i]:
                    paredes = False
                else:
                    self.array_lectura_paredes.append(lista[i].split())
            elif tejados:
                if "@end_tejados" in lista[i]:
                    tejados = False
                else:
                    self.array_lectura_tejados.append(lista[i].split())
            elif enemigos:
                if "@end_enemigos" in lista[i]:
                    enemigos = False
                else:
                    self.array_lectura_enemigos.append(lista[i].split())
            i += 1

        # creamos las listas por cada caracter:
        for i in range(len(self.array_lectura_suelos)):
            for a in self.array_lectura_suelos[i]:
                self.array_lectura_suelos[i] = list(a)

        for i in range(len(self.array_lectura_paredes)):
            for a in self.array_lectura_paredes[i]:
                self.array_lectura_paredes[i] = list(a)

        for i in range(len(self.array_lectura_tejados)):
            for a in self.array_lectura_tejados[i]:
                self.array_lectura_tejados[i] = list(a)

    def parsear_enemigos(self):

        for elemento in self.array_lectura_enemigos:

            enemigo = Enemigo()
            enemigo.nombre = elemento[0]
            if enemigo.nombre == "princesa":
                enemigo.vida = 50
                enemigo.ataque = 25
                enemigo.surface = self.tileset_enemigos[0][0].convert_alpha()
            else:
                enemigo.surface = self.tileset_enemigos[15][15].convert_alpha()
            enemigo.rect.x = int(elemento[1])
            enemigo.rect.y = int(elemento[2])
            enemigo.capa = int(elemento[3])
            self.grupo_mundo.add(enemigo)
            self.enemigos.append(enemigo)

        return self.enemigos

    def parsear_suelos(self):
        x = 0
        y = 0
        for fila in self.array_lectura_suelos:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                if elemento == 'q':
                    # suelo arido
                    tile.nombre = "arido"
                    tile.surface = self.tileset1[0][0]
                    tile.tipo = "q"
                    tile.caminable = True
                elif elemento == 'g':
                    # cesped:
                    tile.nombre = "cesped"
                    tile.surface = self.tileset1[1][0]
                    tile.tipo = "g"
                    tile.caminable = True
                elif elemento == 'm':
                    # madera:
                    tile.nombre = "madera"
                    tile.surface = self.tileset1[1][1]
                    tile.tipo = "m"
                    tile.caminable = True
                elif elemento == 'r':
                    # algo:
                    tile.nombre = "roca"
                    tile.tipo = "g"
                    tile.surface = self.tileset1[0][1]
                elif elemento == 'a':
                    # algo:
                    tile.nombre = "algo"
                    tile.surface = self.tileset1[0][2]
                    tile.tipo = "a"
                    tile.caminable = False
                else:
                    # algo:
                    tile.nombre = "default_suelo"
                    tile.surface = self.tileset1[31][31]
                    tile.tipo = "#"
                    tile.caminable = False
                #tile.rect.move_ip(x, y)
                tile.x = x
                tile.y = y
                linea.append(tile)
                x = x + 32
            self.layer1.append(linea)
            y = y + 32

        return self.layer1

    def parsear_paredes(self):
        x = 0
        y = 0
        for fila in self.array_lectura_paredes:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                if elemento == 'q':
                    #suelo arido
                    tile.nombre = "arido"
                    tile.surface = self.tileset2[0][0].convert_alpha()
                    tile.tipo = "q"
                    tile.caminable = True
                elif elemento == 'g':
                    # cesped:
                    tile.nombre = "cesped"
                    tile.surface = self.tileset2[1][0].convert_alpha()
                    tile.tipo = "g"
                    tile.caminable = True
                elif elemento == 'm':
                    # madera:
                    tile.nombre = "madera"
                    tile.surface = self.tileset2[1][1].convert_alpha()
                    tile.tipo = "m"
                    tile.caminable = True
                elif elemento == 'r':
                    # algo:
                    tile.nombre = "roca"
                    tile.tipo = "g"
                    tile.surface = self.tileset2[0][1].convert_alpha()
                elif elemento == 'a':
                    # algo:
                    tile.nombre = "algo"
                    tile.surface = self.tileset2[0][2].convert_alpha()
                    tile.tipo = "a"
                    tile.caminable = False
                else:
                    # algo:
                    tile.nombre = "default_pared"
                    tile.surface = self.tileset2[31][31].convert_alpha()
                    tile.tipo = "$"
                    tile.caminable = False
                #tile.rect.move_ip(x, y)
                tile.x = x
                tile.y = y
                linea.append(tile)
                x = x + 32
            self.layer2.append(linea)
            y = y + 32

        return self.layer2

    def parsear_tejados(self):
        x = 0
        y = 0
        for fila in self.array_lectura_tejados:
            x = 0
            linea = []
            for elemento in fila:
                tile = Tile()
                if elemento == 'q':
                    #suelo arido
                    tile.nombre = "tejado1"
                    tile.surface = self.tileset3[0][0].convert_alpha()
                    tile.tipo = "q"
                    tile.caminable = True
                elif elemento == 'g':
                    # cesped:
                    tile.nombre = "tejado2"
                    tile.surface = self.tileset3[1][0].convert_alpha()
                    tile.tipo = "g"
                    tile.caminable = True
                elif elemento == 'm':
                    # madera:
                    tile.nombre = "tejado3"
                    tile.surface = self.tileset3[1][1].convert_alpha()
                    tile.tipo = "m"
                    tile.caminable = True
                elif elemento == 'r':
                    # algo:
                    tile.nombre = "tejado4"
                    tile.tipo = "g"
                    tile.surface = self.tileset3[0][1].convert_alpha()
                elif elemento == 'a':
                    # algo:
                    tile.nombre = "tejado5"
                    tile.surface = self.tileset3[0][2].convert_alpha()
                    tile.tipo = "a"
                    tile.caminable = False
                else:
                    # algo:
                    tile.nombre = "default_tejado"
                    tile.surface = self.tileset3[31][31].convert_alpha()
                    tile.tipo = "$"
                    tile.caminable = False
                #tile.rect.move_ip(x, y)
                tile.x = x
                tile.y = y
                linea.append(tile)
                x = x + 32
            self.layer3.append(linea)
            y = y + 32

        return self.layer3
