# por el momento el programa deberia ser capaz de mover el personaje en su onterfaz grafica
import pygame
import monster
pygame.init()

alto =600
ancho=800

ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Prueba sprite movimiento")
clock = pygame.time.Clock()
salir = False
i=0



monster = monster.Mob((20,20))     

while salir == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            monster.rect.x +=3
    
    ventana.fill((244,2,244))
    monster.accion(event)
    ventana.blit(monster.imagen, monster.rect)
    

    if i ==0:
        i=1
    else:
        i=0
    pygame.display.flip()
    clock.tick(16)
pygame.quit()
   