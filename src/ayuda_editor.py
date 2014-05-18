import pygame


class Ayuda(pygame.sprite.Sprite):

    def __init__(self, pantalla_tam):
        super(Ayuda, self).__init__()
        self.offset = 10
        pygame.font.init()
        self.fuente = pygame.font.SysFont('Arial', 20)
        self.surface = pygame.image.load("res/ayuda.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (pantalla_tam[0] / 2,
                        pantalla_tam[1])).convert()
        self.surface_bg = self.surface.copy()
        self.rect = self.surface.get_rect()
        self.rect.centerx = pantalla_tam[0] / 2
        self.rect.y = 0
        self.offset = 5
        self.run = False
        self.array_textos = []
        self.info_capa = " -Solo se puede trabajar sobre la capa activa"
        self.array_textos.append(self.info_capa)
        self.info_save = " -El mapa se graba solo con autosave o manualmente, en /mapas/"
        self.array_textos.append(self.info_save)
        self.info_base = " -Usar un tile como base convertira toda la capa a ese tile!!"
        self.array_textos.append(self.info_base)
        self.texto_teclas = " -Teclas: "
        self.array_textos.append(self.texto_teclas)
        self.grabar = "    Grabar mapa : S"
        self.array_textos.append(self.grabar)
        self.autosave = "    Autosave (on/off): A (activado por defecto)"
        self.array_textos.append(self.autosave)
        self.seleccionar_capa = "    Seleccionar capa: 1 (suelo), 3 (paredes), 4 (tejados)"
        self.array_textos.append(self.seleccionar_capa)
        self.esconder_capa = "    Esconder capas (solo paredes y techos):"
        self.array_textos.append(self.esconder_capa)
        self.capas = "        space (paredes), L_alt (tejados)"
        self.array_textos.append(self.capas)
        self.tam_pincel = "   Tamano del pincel: m_wheelup, m_wheeldown"
        self.array_textos.append(self.tam_pincel)
        self.moverse = "   Mouse2: moverse por el mapa"
        self.array_textos.append(self.moverse)
        self.borrar = "    Borrar: E"
        self.array_textos.append(self.borrar)
        self.usar_tilebase = "    Usar tile base: L + X (CAMBIA TODA LA CAPA POR EL TILE)"
        self.array_textos.append(self.usar_tilebase)
        self.enemigos = "   Tecla L Control para menu entidades (activar/desactivar"
        self.array_textos.append(self.enemigos)
        self.enemigos2 = "   E para borrar entidades (activar/desactivar)"
        self.array_textos.append(self.enemigos2)
        self.enemigos3 = "   Las entidades solo se pueden poner en la capa 1 y 4"
        self.array_textos.append(self.enemigos3)
        self.salir = " Pulsa F1 para cerrar la ayuda"
        self.array_textos.append(self.salir)

    def ejecutar(self):

        i = 25
        #self.surface.fill((0, 0, 0))
        self.surface.blit(self.surface_bg, (0, 0))
        for texto in self.array_textos:

            self.surface.blit(self.fuente.render(texto, True, (255, 255, 0)),
                                 (self.offset, self.offset + i))
            i += 25
