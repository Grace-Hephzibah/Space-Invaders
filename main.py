import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 🚀🚀🚀")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Importing the assets
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,
                                          (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))  # Scales down the size
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)  # Rotates the image

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE,
                                       (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))  # Scales down the size
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)  # Rotates the image


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # Text or images to be put on the screen
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if (keys_pressed[pygame.K_a or pygame.KSCAN_A]) and yellow.x - VEL > 0:  # Left
        yellow.x -= VEL
    if (keys_pressed[pygame.K_d or pygame.KSCAN_D]) and yellow.x + VEL + yellow.width < BORDER.x:  # Right
        yellow.x += VEL
    if (keys_pressed[pygame.K_w or pygame.KSCAN_W]) and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if (keys_pressed[pygame.K_s or pygame.KSCAN_S]) and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)  # Limits to the FPS rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
