import sys, os, pygame

pygame.init()

start_screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True
font = pygame.font.Font(None, 36)

#screen = pygame.display.set_mode((WIDTH,HEIGHT))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    start_screen.fill("black")
    high_score = font.render("High Score: ", True, (255, 215, 0))
    text_rect = high_score.get_rect(center=(400,400))
    start_screen.blit(start_screen, text_rect)



    # flip() the display to put your work on screen
    pygame.display.flip()

    #dt is delta time in seconds since last frame, used for framerate independent physics
    dt = clock.tick(5) # limits FPS to 60

pygame.quit()   




# Start Screen
    # Select screen size (mode) 300x 500x 800x
    # Select mode (speed) slow normal fast
    # Select color snake (type a color)
        # if color is not spelled right, try again
    # select color background
        # if color is not spelled right, try again
    # Select start button
    # Show high score

# method to remember high score
# display current score
# change color of current score when it's greater than older score
# Start snake in center facing right
# method for adding snake parts
# method for moving snake as a whole
# method for spawning an apple
# method for eating the apple
# method for making the snake hit itself or hitting wall

start_screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((WIDTH,HEIGHT))


player_pos_x = screen.get_width() / 2
player_pos_y = screen.get_height() / 2
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    pygame.draw.rect(screen, "green", (player_pos.x, player_pos.y, 20, 20)) 
    pygame.draw.rect(screen, "green", (player_pos.x - 43, player_pos.y, 20, 20)) 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 0.8 * dt
    if keys[pygame.K_s]:
        player_pos.y += 0.8 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 0.8 * dt
    if keys[pygame.K_d]:
        player_pos.x += 0.8 * dt
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    #dt is delta time in seconds since last frame, used for framerate independent physics
    dt = clock.tick(5) # limits FPS to 60

pygame.quit()






















"""
python3 -m pygame.examples.chimp



if not pygame.font:
    print("warnning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname)
    
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

"""
























# Move Spongebob and Have multiple characters running back and forth 
"""
# #NEWCONCEPT ---------------------------------------------------------
# screen = [1, 1, 2, 2, 2, 1]
# print(screen)

# playerpos = 3
# screen[playerpos] = 8
# print(screen)

# playerpos = playerpos - 1
# screen[playerpos] = 8
# print(screen)

# background = [1, 1, 2, 2, 2, 1]
# screen = [0]*6
# for i in range(6):
#     screen[i] = background[i]
# print(screen)
# playerpos = 3
# screen[playerpos] = 8
# print(screen)

# #NEWCONCEPT ---------------------------------------------------------
# # move hero 8 left
# screen[playerpos] = background[playerpos]
# playerpos = playerpos - 1
# screen[playerpos] = 8
# print(screen)

# #NEWCONCEPT ---------------------------------------------------------
# background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
# screen = create_graphics_screen()
# for i in range(6):
#     screen.blit(background[i], (i*10, 0))
# playerpos = 3
# screen.blit(playerimage, (playerpos*10, 0))
# screen.blit(background[playerpos], (playerpos*10, 0))
# playerpos = playerpos - 1
# screen.blit(playerimage, (playerpos*10,0))

# #NEWCONCEPT ---------------------------------------------------------
# screen = pygame.display.set_mode((626, 398))
# clock = pygame.time.Clock()
# player = pygame.image.load('/Users/maximilin/Desktop/VS Projects/player.webp').convert()
# background = pygame.image.load('/Users/maximilin/Desktop/VS Projects/liquid.webp').convert()
# screen.blit(background, (0, 0))
# position = player.get_rect()
# screen.blit(player, position)
# pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen.blit(background, position, position) #copes one surface like background over another like screen at a position
#     position = position.move(2,0) # creates new rect obj with new position (x, y)
#     screen.blit(player, position)
#     pygame.display.update()
#     clock.tick(60)

# #NEWCONCEPT ---------------------------------------------------------
# class GameObject:
#     def __init__(self, image, height, speed):
#         self.speed = speed
#         self.image = image
#         self.pos = image.get_rect().move(0, height)
#     def move(self):
#         self.pos = self.pos.move(self.speed, 0)
#         if self.pos.right > 600:
#             self.pos.left = 0

# screen = pygame.display.set_mode((626, 398))
# clock = pygame.time.Clock()            #get a pygame clock object
# player = pygame.image.load('/Users/maximilin/Desktop/VS Projects/player.webp').convert()
# background = pygame.image.load('/Users/maximilin/Desktop/VS Projects/liquid.webp').convert()
# screen.blit(background, (0, 0))
# objects = []
# for x in range(10):                    #create 10 objects</i>
#     o = GameObject(player, x*40, x)
#     objects.append(o)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     for o in objects:
#         screen.blit(background, o.pos, o.pos)
#     for o in objects:
#         o.move()
#         screen.blit(o.image, o.pos)
#     pygame.display.update()
#     clock.tick(60)

#NEWCONCEPT ---------------------------------------------------------
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT-SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT-SPRITE_HEIGHT


WIDTH, HEIGHT = 626, 398
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.image.load('/Users/maximilin/Desktop/VS Projects/player.webp').convert()
entity = pygame.image.load('/Users/maximilin/Desktop/VS Projects/alien.jpg').convert()
background = pygame.image.load('/Users/maximilin/Desktop/VS Projects/liquid.webp').convert()
SPRITE_HEIGHT = player.get_rect().height
SPRITE_WIDTH = player.get_rect().width

clock = pygame.time.Clock()            #get a pygame clock object
screen.blit(background, (0, 0))
objects = []
p = GameObject(player, 10, 3)          #create the player object

for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)
"""

# Move a Purple Circle 1.0 
"""
import sys, pygame
#from pygame.locals import *

pygame.init()

size = width, height = 900, 850
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)



ball = pygame.image.load("/Users/maximilin/Desktop/intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
"""



# Move a Purple Circle 2.0
"""
# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #poll for events
    #pygame.QUIT event means the user clicked X to close their window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    #RENDER YOUR GAME HERE

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 0.8 * dt
    if keys[pygame.K_s]:
        player_pos.y += 0.8 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 0.8 * dt
    if keys[pygame.K_d]:
        player_pos.x += 0.8 * dt
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    #dt is delta time in seconds since last frame, used for framerate independent physics
    dt = clock.tick(60) # limits FPS to 60

pygame.quit()
"""