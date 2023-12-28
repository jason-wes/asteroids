import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

playing = True

player_pos = pygame.Vector2(screen_width/2, screen_height/2) # x,y

clock = pygame.time.Clock()
dt = 0

while playing:
    # event polling
    for event in pygame.event.get():
        # check quit
        if event.type == pygame.QUIT:
            playing = False

    # wipe screen
    screen.fill("purple")        
    
    pygame.draw.circle(screen, "white", player_pos, 50, 5)
    # keys
    keys = pygame.key.get_pressed()
    # handle keys
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        
    # flip/update
    pygame.display.flip()

    dt = clock.tick(60) / 1000
        
pygame.quit()