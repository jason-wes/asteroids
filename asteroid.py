import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

playing = True
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(screen_width/2, screen_height/2) # x,y
max_asteroids = 5

class Asteroid:
    # TODO missing pos and is_child 
    def __init__(self, id, size):
        self.id = id
        self.pos = pygame.Vector2(400, random.randint(-150, -50))
        self.size = size

    def draw_self(self):
        pygame.draw.rect(screen, "white", pygame.Rect(self.pos.x, self.pos.y, 50, 50), 5)

    def update_pos(self):
        self.pos.x -= 100 * dt
        self.pos.y += 100 * dt

def player_movement(keys):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    return

def handle_boundaries(pos):
    if pos.x < 0:
        pos.x = screen_width
    elif pos.x > screen_width:
        pos.x = 0
    if pos.y > screen_height:
        pos.y = 0
    elif pos.y < 0:
        pos.y = screen_height

# establish asteroid array 
asteroid = Asteroid(0, 2)

while playing:
    # event polling
    for event in pygame.event.get():
        # check quit
        if event.type == pygame.QUIT:
            playing = False

    # wipe screen
    screen.fill("purple")        
    
    # draw entities
    pygame.draw.circle(screen, "white", player_pos, 25, 5)

    asteroid.draw_self()
    asteroid.update_pos()

    # keys
    keys = pygame.key.get_pressed()
    # handle keys
    player_movement(keys)

    # handle player and asteroid boundary collisions
    handle_boundaries(player_pos)
    handle_boundaries(asteroid.pos)
        
    # flip/update
    pygame.display.flip()

    dt = clock.tick(60) / 1000
        
pygame.quit()