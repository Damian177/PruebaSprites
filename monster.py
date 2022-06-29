import pygame

class Mob(pygame.sprite.Sprite):
    def __init__ (self,pos):
        self.imagen = pygame.image.load("Assets/img/Idle/Idle01.png")
        self.idle = { 0: pygame.image.load("Assets/img/Idle/Idle01.png"), 1: pygame.image.load("Assets/img/Idle\Idle02.png") }
        self.jump = { 0: pygame.image.load("Assets/img/Jump\Jump01.png"), 1: pygame.image.load("Assets/img/Jump\Jump02.png") , 2: pygame.image.load("Assets/img/Jump\Jump03.png") , 3: pygame.image.load("Assets/img/Jump\Jump04.png") , 4: pygame.image.load("Assets/img/Jump\Jump05.png") , 5: pygame.image.load("Assets/img/Jump\Jump06.png") , 6: pygame.image.load("Assets/img/Jump\Jump07.png") , 7: pygame.image.load("Assets/img/Jump\Jump08.png") , 8: pygame.image.load("Assets/img/Jump\Jump09.png") }
        self.spin = { 0: pygame.image.load("Assets/img/Spin\Spin01.png"), 1: pygame.image.load("Assets/img/Spin\Spin02.png"), 2: pygame.image.load("Assets/img/Spin\Spin03.png"), 3: pygame.image.load("Assets/img/Spin\Spin04.png"), 4: pygame.image.load("Assets/img/Spin\Spin05.png"), 5: pygame.image.load("Assets/img/Spin\Spin06.png"), 6: pygame.image.load("Assets/img/Spin\Spin07.png"), 7: pygame.image.load("Assets/img/Spin\Spin08.png"), 8: pygame.image.load("Assets/img/Spin\Spin09.png"), 9: pygame.image.load("Assets/img/Spin\Spin10.png"), 10: pygame.image.load("Assets/img/Spin\Spin11.png"), 11: pygame.image.load("Assets/img/Spin\Spin12.png") }
        self.sleep = { 0: pygame.image.load("Assets/img/Sleep\Sleep01.png"), 1: pygame.image.load("Assets/img/Idle\Idle02.png") }
        self.walk = { 0: pygame.image.load("Assets/img/Walk\walk01.png"),1: pygame.image.load("Assets/img/Walk\walk02.png"),2: pygame.image.load("Assets/img/Walk\walk03.png"),3: pygame.image.load("Assets/img/Walk\walk04.png")}
        self.i =0
        self.j=0
        self.flip =False
        self.rect = self.imagen.get_rect()   
        self.rect = self.rect.inflate(-2,-2)   
        self.rect.topleft = pos
        self.vel_x = 0
        self.vel_y = 0
        self.vel_g = 1.5
        self.ima = pygame.Surface.copy(self.imagen)
        self.ima = self.ima.fill((255,20,20))
    def img_refresh (self, move):
        
        if move =='left' :
            if self.i >= len(self.walk):
                self.i =0
            self.flip=True
            self.imagen = pygame.transform.flip(self.walk[self.i], self.flip, False)
            self.i = self.i +1
        if move== 'stay':
            if self.i >= len(self.idle):
                self.i =0
            self.imagen = pygame.transform.flip(self.idle[self.i], self.flip, False)
            self.i = self.i +1   
        if move =='right' :
            if self.i >= len(self.walk):
                self.i =0
            self.imagen = self.walk[self.i]
            self.flip = False
            self.i = self.i +1   
        if move =='jump' :
            if self.i >= len(self.jump):
                self.i =0
                self.j=0
            self.imagen = pygame.transform.flip(self.jump[self.i], self.flip, False)
            self.i = self.i +1   
        if move =='spin' :
            if self.i >= len(self.spin):
                self.i =3
            self.imagen = pygame.transform.flip(self.spin[self.i], self.flip, False)
            self.i = self.i +1           
            
            
    def accion (self,event):
       # for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_LEFT or event.key== pygame.K_a:
                    self.img_refresh('left')
                    self.vel_x = -5
                if event.key== pygame.K_RIGHT or event.key== pygame.K_d:
                    self.img_refresh('right')
                    self.vel_x = 5    
                if event.key== pygame.K_UP or event.key== pygame.K_w:
                    self.img_refresh('jump') 
                    self.saltar()      
                if event.key== pygame.K_DOWN:
                    self.img_refresh('spin')                  
            if event.type == pygame.KEYUP:
                self.img_refresh('stay')
                self.vel_x = 0
                                         
            
    def moving (self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    #placeholders
    def saltar (self):

        if self.vel_y == 0:
            self.vel_y = -20                
    def caer (self,fall):
        if not fall:
            self.vel_y += self.vel_g
        else:
            self.vel_y = 0
            