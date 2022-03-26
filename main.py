
import pygame

pygame.font.init()
# game idea
'''
make a rectangle that can move.
when rectangle hits ball
ball moves oppisite direction

when ball hits bottom screen: game over

if ball hits rectangle score + 1
score board on screen.
'''


#initialize all ingame variables
screen_width = 1000
screen_height = 600

vel = 8
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60
pygame.display.set_caption("Ball Game!")
bg_color = (255,200,200)

# make start game
start = False
start_image = pygame.image.load('start_btn.png').convert_alpha()

# make ball
ball_image = pygame.image.load("basketball-ball.png")

# class for start button    
class Button() :
    def __init__(self, x, y, image, player, button):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.draw_button = True
        self.check = 100
        self.add = 100

    def draw(self):
        global start
        pos = pygame.mouse.get_pos()
        #print(pos)

        self.check += self.add

        if self.check == 3000:
            self.draw_button = False
            self.add = -100
        
        if self.check == 0:
            self.draw_button = True
            self.add = 100



        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                start = True
                if start == True:
                    player.plyr_rect.x = 400
                    ball.ball_rect.x = screen_width//2 - 50
                    ball.ball_rect.y = 100
                    ball.xvel = 6
                    ball.yvel = 6

        if self.draw_button:
            screen.blit(self.image, (self.rect.x, self.rect.y))
# class for player
class Player:

    def __init__(self, x, y, width, height, color):
        self.screen = screen
        self.vel = vel
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.plyr_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def drawing(self):
        pygame.draw.rect(screen,(self.color), self.plyr_rect)

    def move(self):
        self.keys = pygame.key.get_pressed()

        # make player move left
        if self.keys[pygame.K_a] and self.plyr_rect.x >= 0:
            self.plyr_rect.x -= self.vel

        # make player move right
        if self.keys[pygame.K_d] and self.plyr_rect.x <= screen_width - self.width:
            self.plyr_rect.x += self.vel
    
    def update(self):
        self.drawing()
# make the ball
class Ball:
    def __init__(self, x, y, image, scale, player):
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.xvel = 6
        self.yvel = 6
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.ball_rect = self.image.get_rect()
        self.ball_rect.topleft = (self.x, self.y)

    def draw(self):
        screen.blit(self.image, (self.ball_rect.x, self.ball_rect.y))

    def move(self):
        self.ball_rect.x += self.xvel
        self.ball_rect.y += self.yvel

    def check_collision(self):
        # game over
        global start

        #player collision
        if self.ball_rect.colliderect(player.plyr_rect):
            self.yvel = -1 * self.yvel

        # wall collision
        if self.ball_rect.x == 0:
            self.xvel = -1 * self.xvel
        if self.ball_rect.x == screen_width - 4:
            self.xvel = -1 * self.xvel
            #print("poep")
        if self.ball_rect.y == 4:
            self.yvel = -1 * self.yvel
            print("poep")

        if self.ball_rect.y >= screen_height - self.ball_rect.height:
            start = False
        
        print(self.ball_rect.x)
        #print(self.ball_rect.y)

# class variables
player = Player(400, 400, 150, 40, (255, 0, 0))
ball = Ball(screen_width//2 - 50, 100, ball_image, 0.1, player)
start_button = Button(350, 200, start_image, player, ball)

#make function to draw objects on screen
def drawing():
    win = screen
    win.fill(bg_color)
    player.update()
    ball.draw()
    if start == False:
        start_button.draw()
    else:
        player.move()
        ball.move()
        ball.check_collision()

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(FPS)
    drawing()
    pygame.display.update()