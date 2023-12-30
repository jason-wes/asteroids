import pygame
import random
import time
import math

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
            self.original_player_icon = pygame.image.load('edited-ship.png')
            self.original_player_icon = pygame.transform.scale(self.original_player_icon, (self.width, self.height))
            self.player_icon = self.original_player_icon
            self.angle = 0
            self.speed = 5

        def rotate(self, angle):
            self.angle += angle
            old_center = (self.x + self.width // 2, self.y + self.height // 2)
            self.player_icon = pygame.transform.rotate(self.original_player_icon, self.angle)
            self.width, self.height = self.player_icon.get_size()
            self.x = old_center[0] - self.width // 2
            self.y = old_center[1] - self.height // 2

        def update(self, keys):
            if keys[pygame.K_w]:
                self.y -= 300 * dt
            if keys[pygame.K_a]:
                self.x -= 300 * dt
            if keys[pygame.K_s]:
                self.y += 300 * dt
            if keys[pygame.K_d]:
                self.x += 300 * dt

            if keys[pygame.K_UP]:
                dx = self.speed * math.cos(math.radians(self.angle + 90))
                dy = self.speed * math.sin(math.radians(self.angle - 90))
                moved_rect = self.move(dx, dy)
                self.x = moved_rect.x
                self.y = moved_rect.y
            if keys[pygame.K_LEFT]:
                self.rotate(5)
            if keys[pygame.K_RIGHT]:
                self.rotate(-5)

            # pygame.draw.rect(screen, "white", self, 25, 5)
            screen.blit(self.player_icon, (self.x, self.y))

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
        
        for asteroid in asteroid_array:
            asteroid.update()

        # keys
        keys = pygame.key.get_pressed()
        # handle keys
        player.update(keys)

        handle_boundaries(player)

        # collision detection (asteroid on ship)
        for asteroid in asteroid_array:
            if asteroid.colliderect(player):
                screen.fill("red")
                pygame.display.flip()
                time.sleep(2)
                game()
            
            handle_boundaries(asteroid)
            
        # flip/update
        pygame.display.flip()

        dt = clock.tick(60) / 1000
            
    pygame.quit()

game()