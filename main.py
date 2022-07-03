import pygame   #libreria 
from monster import Player #clase de nuestro pj ppal
from levels import * #clases para generar niveles
from variables import *
from pygame.locals import *
pygame.init()

ventana = pygame.display.set_mode(TAM_PANTALLA) 
pygame.display.set_caption("BreaBall") #establecemos nombre de la ventana
clock = pygame.time.Clock()
salir = False 
i=0


monster = Player((25,25))  
terreno= []  
nivel = level1()

monster.plataformas_del_nivel = nivel.lista_plataformas
monsterg=pygame.sprite.GroupSingle
monsterg.add(monster)

# Iniciamos el bucle del juego
while salir == False:
    # Obtenemos las acciones del jugador, y las pocesamos  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT or event.key== pygame.K_a:
                monster.move_dir('left')
            if event.key== pygame.K_RIGHT or event.key== pygame.K_d:
                monster.move_dir('right')
            if event.key== pygame.K_UP or event.key== pygame.K_w:
                monster.move_dir('jump')     
            if event.key== pygame.K_DOWN:
                monster.move_dir('spin')                  
        if event.type == pygame.KEYUP:  
            if monster.vel_x !=0:
                if event.key == pygame.K_LEFT:
                    monster.move_dir('stay')
                if event.key == pygame.K_RIGHT:
                    monster.move_dir('stay')
            if monster.vel_x ==0:
                if event.key == pygame.K_DOWN:
                    monster.move_dir('stay')
                if event.key == pygame.K_UP:
                    monster.move_dir('stay')


      
    #actualizamos todo

    monster.update()
    
    #monster.moving()
    #dibujamos todo

    #Actualizamos la pantalla
    ventana.fill(GRIS)
    nivel.lista_plataformas.draw(ventana)
    pygame.draw.rect(ventana, ROJO, monster.rect)
    ventana.blit(monster.imagen, (monster.rect.x -11, monster.rect.y -21))
    #monsterg.draw(ventana)
    if i ==0:
        i=1
    else:
        i=0
    pygame.display.flip()
    
    clock.tick(20) #frames por seg
pygame.quit()
   