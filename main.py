import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

PLAYER_HITBOX_X = 40
PLAYER_HITBOX_Y = 60
PLAYER_SPEED = 5
FONT = pygame.font.SysFont("arial", 30)
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

pygame.display.set_caption("Testing")

BG_IMG = pygame.transform.scale(pygame.image.load("./assets/bg.jpg"), (WIDTH, HEIGHT))

def draw(player, elapsed_time):
    WIN.blit(BG_IMG, (0,0))
    time_text = FONT.render(f"TIME: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (28, 28))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HITBOX_Y + 10, PLAYER_HITBOX_Y, PLAYER_HITBOX_X)

    while run:
        clock.tick(90)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 10:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_HITBOX_X - 30:
            player.x += PLAYER_SPEED
        
        draw(player, elapsed_time)

    pygame.quit()


if __name__ == "__main__":
    main()

