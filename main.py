# por el momento el programa deberia ser capaz de mover el personaje en su onterfaz grafica
import pygame

pygame.init()

alto =600
ancho=800

ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Prueba sprite movimiento")
clock = pygame.time.Clock()
salir = False

        

while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            lala =0
    ventana.fill((244,2,244))
    pygame.display.flip()
pygame.quit()
   