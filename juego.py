import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600)) # crea Pantalla

game_over = False # Condicion para acabar el juego
while not game_over:

    eventos = pygame.event.get() # Procesa eventos. Al meterlos en una varible evita que se pierdan al acabar/iniciar el blucle
    for evento in eventos:
        if evento.type == pygame.QUIT:
            game_over = True

    pantalla.fill((255, 0, 0)) # Color de fonfo

    pygame.display.flip() # Manda el programa a la panatalla

pygame.quit()