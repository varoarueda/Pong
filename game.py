import pygame as pg

TAMAÑO = (800, 600)

class Bola():
    def __init__(self, x, y, w, h, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.derecha = True
        self.arriba = True

    def actualizate(self): # Avanza y busca los limites y robata
        if self.derecha:
            self.x += 5
        else:
            self.x -= 5

        if self.x + self.w >= TAMAÑO[0]:
            self.derecha = False
        if self.x <= 0:
            self.derecha = True

        if self.arriba:
            self.y -= 5
        else:
            self.y += 5

        if self.y + self.h >= TAMAÑO[1]:
            self.arriba = True
        if self.y <= 0:
            self.arriba = False


class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode((TAMAÑO)) # x,y son posicionales / w,y son de tamaño

    def bucle_principal(self):
        bola = Bola(700 - 10, TAMAÑO[1]//2 - 10, 20, 20) # Posicionamiento y  tamaño bola
        game_over = False
        pg.init()

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            bola.actualizate()

            self.pantalla.fill((0, 0, 0))
            pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            
            pg.display.flip()
        pg.quit()

juego = Game()
juego.bucle_principal()