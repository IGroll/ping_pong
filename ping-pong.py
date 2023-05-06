from pygame import *
font.init()
window = display.set_mode((800,600))
bg = transform.scale(image.load('bg.png'),(800,600))
display.set_caption(':o')
game = True
end = True
wait = False
blue_goals = 0
red_goals = 0
font = font.SysFont('Arial',70)
blue = font.render(str(blue_goals),True,(0,50,255))
red = font.render(str(red_goals),True,(255,50,50))
fps = 60
wait_schetchik = 3
aaa = 0
waiter = font.render(str(wait_schetchik),True,(0,0,0))
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
        self.xspeed = speed
        self.yspeed = speed
    def update(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if sprite.collide_rect(self,player1):
            self.xspeed *= -1
        if self.rect.y <= 20:
            self.yspeed *= -1
        if self.rect.y >= 480:
            self.yspeed *= -1
        if sprite.collide_rect(self,player2):
            self.xspeed *= -1
player1 = Player(5,'player1.png',650,220)
player2 = Player(5,'player2.png',100,220)
ball = Ball(3,'ball.png',400,100)
while game:
    window.blit(bg,(0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if wait:
        aaa += 1
        if aaa >= fps:
            aaa = 0
            wait_schetchik -= 1
            waiter = font.render(str(wait_schetchik),True,(0,0,0))
            if wait_schetchik == 0:
                wait_schetchik = 3
                wait = False
                end = True
        window.blit(waiter,(380,300))  
        window.blit(blue,(650,50))    
        window.blit(red,(150,50)) 
    if end:
        player1.update()
        player1.move1()
        player2.update()
        player2.move2()
        ball.update()
        if ball.rect.x <= -110:
            blue_goals += 1
            blue = font.render(str(blue_goals),True,(0,50,255))
            ball.rect.x = 400
            ball.rect.y = 300
            end = False
            wait = True
        window.blit(blue,(650,50))    
        if ball.rect.x >= 910:
            red_goals += 1
            red = font.render(str(red_goals),True,(255,50,50))
            ball.rect.x = 400
            ball.rect.y = 300
            end = False
            wait = True
        window.blit(red,(150,50))    
        clock.tick(fps)
        display.update()
        player2.update()
        player2.move2()
        ball.update()
        if ball.rect.x <= -120:
            window.blit(blue,(300,250))    
        if ball.rect.x >= 910:
            window.blit(red,(300,250))    
    clock.tick(fps)
    display.update()
