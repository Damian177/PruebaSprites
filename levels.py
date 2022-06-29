import pygame

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
