# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Welcome to The Matrix')
clock = pygame.time.Clock()
running = True
color_choice = 'green'  # Default color

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# draw lines to track the trajectory of the circle/ball by keeping track of the circle's positions in a list
trajectory = []

while running:
    # poll for events - everything that happends from the user
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detects key presses
            if event.key == pygame.K_r: 
                color_choice = 'red'
            elif event.key == pygame.K_g:
                color_choice = 'grey'
            elif event.key == pygame.K_y:
                color_choice = 'yellow'
            elif event.key == pygame.K_b:
                color_choice = 'blue'
            elif event.key == pygame.K_m:
                color_choice = 'magenta'
            elif event.key == pygame.K_i:
                color_choice = 'indigo'
            elif event.key == pygame.K_o:
                color_choice = 'orange'


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw circle
    pygame.draw.circle(screen, color_choice, player_pos, 30) 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos.y - 30 > 0:
        player_pos.y -= 300 * dt
        trajectory.append(player_pos.copy())
    if keys[pygame.K_DOWN] and player_pos.y + 30 < 720:
        player_pos.y += 300 * dt
        trajectory.append(player_pos.copy())
    if keys[pygame.K_LEFT] and player_pos.x - 30 > 0:
        player_pos.x -= 300 * dt
        trajectory.append(player_pos.copy())
    if keys[pygame.K_RIGHT] and player_pos.x + 30 < 1280:
        player_pos.x += 300 * dt
        trajectory.append(player_pos.copy())

    # Draw trajectory lines
    if len(trajectory) > 1:
        pygame.draw.lines(screen, color_choice, False, trajectory, 2)


    # flip() the display to put work on screen
    pygame.display.flip()

    # limits FPS to 60 
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000


pygame.quit()