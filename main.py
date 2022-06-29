from bs4 import BeautifulSoup
import pygame   #libreria 
from monster import Mob #clase de nuestro pj ppal
from levels import tiles #clases para generar niveles
from variables import *
from pygame.locals import *
pygame.init()

ventana = pygame.display.set_mode(TAM_PANTALLA) 
pygame.display.set_caption("BreaBall") #establecemos nombre de la ventana
clock = pygame.time.Clock()
salir = False 
i=0


plataformas_lv1= ((15,80,150,5),(100,200,150,5),(168,260,350,5))
plataformas=pygame.sprite.Group()
monster = Mob((20,20))  
terreno= []  
# tile = tiles(15 , 40, 150 , 20)
# for tile in plataformas_lv1:
#     terreno.append(tiles(tile[0],tile[1],tile[2],tile[3]))
for i in plataformas_lv1:
     plataforma=tiles(i[0],i[1],i[2],i[3])
     plataformas.add(plataforma)



# Iniciamos el bucle del juego
while salir == False:
    # Obtenemos las acciones del jugador, y las pocesamos  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
            break
        

    monster.accion(event)
      
    #actualizamos todo

    caer=pygame.sprite.spritecollide(monster, plataformas, False)   
    monster.caer(caer)
    monster.moving()
    #dibujamos todo

    #Actualizamos la pantalla
    ventana.fill(GRIS)
    plataformas.draw(ventana)
    ventana.blit(monster.imagen, monster.rect)

    if i ==0:
        i=1
    else:
        i=0
    pygame.display.flip()
    
    clock.tick(20) #frames por seg
pygame.quit()
   