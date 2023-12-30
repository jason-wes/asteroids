import pygame
import random
import time

def game(max_asteroids=5):
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    playing = True
    clock = pygame.time.Clock()
    dt = 0

    class Asteroid(pygame.Rect):
        # TODO is_child 
        def __init__(self, id, magnitude):
            ipos = pygame.Vector2(random.randint(0, 800), random.randint(-500, -50))
            super().__init__(ipos.x, ipos.y, 50, 50)
            self.id = id
            self.magnitude = magnitude
            self.bearing = 1 - 2 * random.randint(0, 1)

        def update(self):
            self.x += self.bearing * 50 * dt
            self.y += 50 * dt
            pygame.draw.rect(screen, "white", self, 5)

    class Player(pygame.Rect):
        def __init__(self):
            super().__init__(screen_width/2, screen_height/2, 50, 50)

        def update(self, keys):
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.y -= 300 * dt
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.x -= 300 * dt
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.y += 300 * dt
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.x += 300 * dt

            pygame.draw.rect(screen, "white", self, 25, 5)

    def handle_boundaries(rect):
        if rect.x < 0:
            rect.x = screen_width
        elif rect.x > screen_width:
            rect.x = 0
        if rect.y > screen_height:
            rect.y = 0
        elif rect.y < 0 and type(rect) is not Asteroid:
            rect.y = screen_height

    # establish asteroid array and player
    player = Player()
    asteroid_array = [Asteroid(i, 2) for i in range(max_asteroids)]

    while playing:
        # event polling
        for event in pygame.event.get():
            # check quit
            if event.type == pygame.QUIT:
                playing = False

        # wipe screen
        screen.fill("purple")        
        
        # draw entities
        for asteroid in asteroid_array:
            asteroid.update()

        # keys
        keys = pygame.key.get_pressed()
        # handle keys
        player.update(keys)

        handle_boundaries(player)

        # compute bounding box
        for asteroid in asteroid_array:
            if asteroid.colliderect(player):
                screen.fill("red")
                pygame.display.flip()
                time.sleep(5)
                game()
            
            handle_boundaries(asteroid)
            
        # flip/update
        pygame.display.flip()

        dt = clock.tick(60) / 1000
            
    pygame.quit()

game()