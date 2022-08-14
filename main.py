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

FUENTE=pygame.font.Font(None,30) #(tipoletra, tamFuente)


monster = Player((25,25))  
terreno= []  
lista_niveles = (level1(),level2(),level3())
nivel_actual=0
nivel = lista_niveles[nivel_actual]

monster.plataformas_del_nivel = nivel.lista_plataformas
monsterg=pygame.sprite.GroupSingle
monsterg.add(monster)
all_sprites_on_level=pygame.sprite.Group
all_sprites_on_level.add(monster)
#all_sprites_on_level.add(nivel.lista_manzanas)
all_sprites_on_level.add(nivel.portal)
#all_sprites_on_level.add(nivel.lista_plataformas)
#all_sprites_on_level.add(nivel.lista_paredes)
manzanas_comidas  = []
score = 0
level_change=0
# Iniciamos el bucle del juego
while salir == False:
    # Obtenemos las acciones del jugador, y las pocesamos  
    if level_change:
        nivel_actual += 1
        if(nivel_actual==len(lista_niveles)):
            break
        print(nivel_actual)
        nivel=lista_niveles[nivel_actual]
        monster.rect.topleft=(nivel.pos_player)
        monster.plataformas_del_nivel = nivel.lista_plataformas
        level_change=0

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
            if event.key== pygame.K_r:
                monster.rect.center=(nivel.pos_player)
            if event.key== pygame.K_g:
                level_change=1

        if event.type == pygame.KEYUP:  
            if monster.vel_x !=0:
                if event.key == pygame.K_LEFT:
                    monster.move_dir('stay')
                if event.key == pygame.K_RIGHT:
                    monster.move_dir('stay')
            if monster.vel_x ==0:
                if event.key == pygame.K_DOWN and monster.vel_x < 0:
                    monster.move_dir('stay')
                if event.key == pygame.K_UP and monster.vel_x > 0:
                    monster.move_dir('stay')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


      
    #actualizamos todo
    monster.update()
    nivel.portal.update()
    nivel.lista_manzanas.update()
    #all_sprites_on_level.update()
    if pygame.sprite.spritecollide(monster, nivel.lista_manzanas, True):
        score += 1
    if pygame.sprite.spritecollide(monster, nivel.portal, False):
        level_change=1

     
    #monster.moving()
    #dibujamos todo

    #Actualizamos la pantalla
    ventana.fill(GRIS)
    nivel.lista_plataformas.draw(ventana)
    nivel.lista_manzanas.draw(ventana)
    nivel.portal.draw(ventana)
    #pygame.draw.rect(ventana, ROJO, monster.rect)
    ventana.blit(monster.imagen, (monster.rect.x -11, monster.rect.y -21))
    texto=FUENTE.render("score: " + str(score),1,NEGRO)
    ventana.blit(texto, (684, 6))
    #monsterg.draw(ventana)
    if i ==0:
        i=1
    else:
        i=0
    pygame.display.flip()
    
    clock.tick(20) #frames por seg
pygame.quit()
   