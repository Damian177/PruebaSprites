import pygame
from variables import *


class level():
    lista_plataformas =None
    lista_paredes =None
    def __init__(self, nombre = "uno") -> None:
        self.nombre  = nombre     
        self.lista_plataformas = pygame.sprite.Group()
        self.lista_paredes = pygame.sprite.Group()

class level1(level):
    def __init__(self):
        super().__init__()
        plataformas_lv1= ((15,80,150,5),(100,200,150,5),(168,260,350,5))
        for i in plataformas_lv1:
            plataforma=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(plataforma)

#tile, plataforma, contorno, con color o imagen 
class tiles(pygame.sprite.Sprite):
    def __init__ (self, x,y,tx,ty): 
        pygame.sprite.Sprite.__init__(self)
        self.pos = ( x,y )
        self.tam=(tx,ty)
        self.image = pygame.Surface(self.tam)
        self.image.fill((200,100,0))
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y


    def draw (self, pantalla):
        pygame.draw.rect(pantalla, (120,120,250), [self.pos, self.tam], 0)


#portal, gira cada frame, una imagen,o gif, en colision se expande
class portal(pygame.sprite.Sprite):
    def __init__ (self, pos):
        self.pos=pos
        self.image= pygame.image.load("Assets/img/Item_64.png")
