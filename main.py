from pygame import *
from random import randint as ri

window = display.set_mode((802, 502))
display.set_caption("Ping Pong")

background = transform.scale(image.load("background.png"), (802, 455))
scoreboard_left = transform.scale(image.load("score_bar_left.png"), (341, 47))
scoreboard_right = transform.scale(image.load("score_bar_right.png"), (341, 47))


clock = time.Clock()
FPS = 60

finish = False

x_speed = 5
y_speed = 5

left_score = 0
right_score = 0

# clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
        
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 67:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 372:
            self.rect.y += self.speed

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 67:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 377:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global x_speed, y_speed, left_racket, right_racket
        if self.rect.y < 67 or self.rect.y > 467:
            y_speed = -y_speed
        
        if self.rect.colliderect(left_racket.rect) or self.rect.colliderect(right_racket.rect):
            x_speed = -x_speed

            if x_speed > 0:
                x_speed += 1
            else:
                x_speed -= 1

            if y_speed > 0:
                y_speed += 1
            else:
                y_speed -= 1
        
        
        self.rect.x += x_speed
        self.rect.y += y_speed
        
        

left_racket = Player('left_player.png', 30, 167, 12, 120, 5)
right_racket = Player('right_player.png', 760, 167, 12, 120, 5)
ball = Ball('Ball.png', 386, ri(60, 490), 30, 30, 0)

font.init()
font1 = font.SysFont('Arial', 30)

game = True
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if finish != True:
        window.blit(background, (0,47))
        window.blit(scoreboard_left, (0,0))
        window.blit(scoreboard_right, (461,0))

        left_racket.update_l()
        right_racket.update_r()
        ball.update()

        left_racket.reset()
        right_racket.reset()
        ball.reset()

        window.blit(font1.render(f"{left_score}", True, (255, 255, 255)), (10, 6))
        window.blit(font1.render(f"{right_score}", True, (255, 255, 255)), (770, 6))

        if ball.rect.x <= 0:
            right_score += 1
            ball.rect.x = 401
            ball.rect.y = 304
        
        if ball.rect.x >= 825:
            left_score += 1
            ball.rect.x = 401
            ball.rect.y = 304

    
    clock.tick(FPS)
    display.update()