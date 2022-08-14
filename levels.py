import pygame
from variables import *


class level():
    lista_plataformas =None
    lista_paredes =None
    lista_manzanas = None
    def __init__(self, nombre = "uno") -> None:
        self.nombre  = nombre     
        self.lista_plataformas = pygame.sprite.Group()
        self.lista_paredes = pygame.sprite.Group()
        self.lista_manzanas = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.paredes= ((0,0,800,5),(0,5,5,600),(5,595,795,5), (795,5,5,595))

class level1(level):
    def __init__(self):
        self.pos_player=(25,25)
        super().__init__()

        plataformas_lv1= ((15,80,150,5),(100,200,150,5),(168,260,350,5))
        for i in plataformas_lv1:
            plataforma=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(plataforma)
        for i in self.paredes:
            pared=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(pared)
        #lista_manzanas= ((117, 178),(146, 58),(227, 240),(468, 239),(629, 170))
        lista_manzanas= ((130, 70),(156, 187),(210, 246),(473, 250),(629, 170))
        for i in lista_manzanas:
            manzana=Manzana(i)
            self.lista_manzanas.add(manzana)
        self.portal.add(portal((700,500)))
class level2(level):
    def __init__(self):
        super().__init__()
        self.pos_player=(25,25)

        plataformas_lv1= ((29, 540,150,8),(621, 532,150,8),(262, 426,150,5),(100, 333,150,5),(342, 241,150,5),(514, 182,150,5),(655, 113,150,5))
        for i in plataformas_lv1:
            plataforma=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(plataforma)
        paredes_lv1= ((0,0,800,5),(0,5,5,600),(5,595,795,5), (795,5,5,595))
        for i in paredes_lv1:
            pared=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(pared)
        lista_manzanas= ((118, 535),(693, 515),(352, 411),(158, 317),(475, 222))
        for i in lista_manzanas:
            manzana=Manzana(i)
            self.lista_manzanas.add(manzana)
        self.portal.add(portal((670, 20)))
class level3(level):
    def __init__(self):
        super().__init__()
        self.pos_player=(350,25)

        plataformas_lv1= ((260, 125,185,5),(5, 210,150,5),(545, 125,170,5),(660, 363,150,5),(132, 429,150,5),(2, 509,150,5))
        for i in plataformas_lv1:
            plataforma=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(plataforma)
        paredes_lv1= ((0,0,800,5),(0,5,5,600),(5,595,795,5), (795,5,5,595))
        for i in paredes_lv1:
            pared=tiles(i[0],i[1],i[2],i[3])
            self.lista_plataformas.add(pared)
        lista_manzanas= ((646, 114),(85, 185),(740, 343),(251, 413),(102, 497))
        for i in lista_manzanas:
            manzana=Manzana(i)
            self.lista_manzanas.add(manzana)
        self.portal.add(portal((0, 520)))
        

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
        super().__init__()
        self.i = 0
        self.j = 0
        #self.portal = { 0: pygame.image.load("Assets/img/portal1.png"), 2: pygame.image.load("Assets/img/portal2.png"), 1: pygame.image.load("Assets/img/portal3.png"), 3: pygame.image.load("Assets/img/portal4.png") }
        #self.image = self.portal[self.i]
        self.spriteSheet= pygame.image.load("Assets/img/Portal.png")
        self.image = self.spriteSheet.subsurface(0,0,100,100)
        self.image = pygame.transform.scale(self.spriteSheet.subsurface(0,0,100,100),(70,70))
        self.rect = self.image.get_rect()
        self.rect.topleft=pos
      
    def update(self):
        if self.i >= 10:
            self.j +=1
            self.i =0
        if self.j==9:
            self.j=0
        #print(self.j,self.i)
        self.image = pygame.transform.scale(self.spriteSheet.subsurface(self.i*100,self.j*100,100,100), (70,70))
        self.i = self.i +1 
    def dibujar_hitbox(self,ventana):
        pygame.draw.rect(ventana, (255,0,0), self.rect)

        
class Manzana(pygame.sprite.Sprite):
    def __init__ (self, pos):
        super().__init__()
        self.spriteSheet=pygame.image.load("Assets/img/Apple.png")
        #self.image= pygame.image.load("Assets/img/Item__64.png")
        self.image = self.spriteSheet.subsurface((512,0,32,32))
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.center=pos
    def update(self):
        self.i +=1
        if self.i >16:
            self.i=0
        self.image = self.spriteSheet.subsurface((self.i*32,0,32,32))
