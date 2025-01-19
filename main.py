import pygame
import time
import random
from player import Player
pygame.font.init()
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("arial", 30)
clock = pygame.time.Clock()
start_time = time.time()
elapsed_time = 0
BULLET_SPEED = 30
pygame.display.set_caption("Galaga")

starting_pos = (0,0)


pygame.display.set_caption("Maryo")

BG_IMG = pygame.transform.scale(pygame.image.load("./assets/bg.jpg"), (WIDTH, HEIGHT))

def draw(player, elapsed_time, shoot):
    WIN.blit(BG_IMG, (0,0))
    time_text = FONT.render(f"TIME: {round(elapsed_time)}s", 1, "white")
    mouse_position = pygame.mouse.get_pos()
    # mouse_position
    mouse_position_render = FONT.render(f"MOUSE: {mouse_position}", 1, "white")
    WIN.blit(time_text, (28, 28))
    WIN.blit(mouse_position_render, (28, 60))
    pygame.draw.rect(WIN, "red", player.PLAYER, 100)
    if shoot:
        endPosX = mouse_position[0]
        endPosY = mouse_position[1]
        startPosX = player.PLAYER.x
        startPosY = player.PLAYER.y
        bullet = pygame.Rect(startPosX - 10, startPosY- 10, 30,30) 
        pygame.draw.rect(WIN, "white", bullet, 100)
        while True:
            if endPosX > startPosX:
                bullet.x += BULLET_SPEED
            elif endPosX < startPosX:
                bullet.x -= BULLET_SPEED
            if endPosY > startPosY:
                bullet.y += BULLET_SPEED
            elif endPosY < startPosY:
                bullet.y -= BULLET_SPEED
            if bullet.x == endPosX and bullet.y == endPosY:
                shoot = False
                break
    pygame.display.update()

def main():
    run = True
    object = Player()
    shoot = False
    while run:
        clock.tick(90)
        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
<<<<<<< HEAD
        shoot = False
=======
>>>>>>> b155d1b032028b0c97de966d20371e8ab3353db4
        if keys[pygame.K_a] and object.PLAYER.x > 10:
            object.moveLeft()
        if keys[pygame.K_d] and object.PLAYER.x < WIDTH - object.PLAYER_HITBOX_X - 10:
            object.moveRight()
        if keys[pygame.K_w] and object.PLAYER.y > 10:
            object.moveUp()
        if keys[pygame.K_s] and object.PLAYER.y < (HEIGHT - 10 - object.PLAYER_HITBOX_Y):
            object.moveDown()
        if keys[pygame.K_SPACE]:
            shoot = True
        draw(object, elapsed_time, shoot)
    pygame.quit()

if __name__ == "__main__":
    main()