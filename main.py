import pygame
import time
import random
from player import Player

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont("arial", 30)
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0

pygame.display.set_caption("Galaga")

BG_IMG = pygame.transform.scale(pygame.image.load("./assets/bg.jpg"), (WIDTH, HEIGHT))

def draw(player, elapsed_time):
    WIN.blit(BG_IMG, (0,0))
    time_text = FONT.render(f"TIME: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (28, 28))
    pygame.draw.rect(WIN, "red", player)
    pygame.display.update()

def main():
    run = True
    object = Player()
    while run:
        clock.tick(90)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and object.PLAYER.x > 10:
            object.moveLeft()
        if keys[pygame.K_RIGHT] and object.PLAYER.x < WIDTH - object.PLAYER_HITBOX_X - 10:
            object.moveRight()
        if keys[pygame.K_UP] and object.PLAYER.y > 10:
            object.moveUp()
        if keys[pygame.K_DOWN] and object.PLAYER.y < (HEIGHT - 10 - object.PLAYER_HITBOX_Y):
            object.moveDown()
        draw(object.PLAYER, elapsed_time)

    pygame.quit()


if __name__ == "__main__":
    main()