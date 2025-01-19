import pygame

class Player():
    PLAYER_HITBOX_X = 40
    PLAYER_HITBOX_Y = 60
    PLAYER_SPEED = 5
    PLAYER = ""
    def __init__(self):
        self.PLAYER = pygame.Rect(200, 800 - self.PLAYER_HITBOX_Y + 10, self.PLAYER_HITBOX_X, self.PLAYER_HITBOX_Y)
    def moveLeft(self):
        self.PLAYER.x -= self.PLAYER_SPEED
    def moveRight(self):
        self.PLAYER.x += self.PLAYER_SPEED
    def moveUp(self):
        self.PLAYER.y -= self.PLAYER_SPEED
    def moveDown(self):
        self.PLAYER.y += self.PLAYER_SPEED