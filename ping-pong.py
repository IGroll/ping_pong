from pygame import *
font.init()
window = display.set_mode((800,600))
bg = transform.scale(image.load('bg.png'),(800,600))
display.set_caption(':o')
game = True
fps = 60
clock = time.Clock()
class Sprites(sprite.Sprite):
    def __init__(self,speed,sprite,player_x,player_y):
        super().__init__()
        self.image = transform.scale(image.load(sprite),(80,70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Sprites):
    def __init__(self,speed,sprite,player_x,player_y):
        super().__init__(speed,sprite,player_x,player_y)
        self.image = transform.scale(image.load(sprite),(50,150))
    def move1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 25:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 425:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 25:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 425:
            self.rect.y += self.speed
class Ball(Sprites):
    def __init__(self,speed,sprite,player_x,player_y):
        super().__init__(speed,sprite,player_x,player_y)
        self.image = transform.scale(image.load(sprite),(100,100))
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        self.rect.x -= self.speed
player1 = Player(5,'player1.png',650,100)
player2 = Player(5,'player2.png',100,100)
ball = Ball(3,'ball.png',400,100)
while game:
    window.blit(bg,(0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    player1.update()
    player1.move1()
    player2.update()
    player2.move2()
    ball.update()
    clock.tick(fps)
    display.update()