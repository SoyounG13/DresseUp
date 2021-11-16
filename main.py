import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init(44100, -16, 2, 512)
pygame.mixer.set_num_channels(32)
pygame.mixer.music.load('C:/Users/Laptop/Desktop/bgm.mp3')
pygame.mixer.music.play(-1)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("👚옷입히기👚")

background = pygame.image.load("data/background/background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

character_name = ['dodo.png', 'dada.png', 'ssissi.png']
character = pygame.image.load("data/character/dodo.png")
character = pygame.transform.scale(character, (200, 334))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - 100
character_x_middle = character_x_pos + character_width // 2
character_y_middle = character_y_pos + character_height // 2

dragging = False
cloths = []
error_amt = 3


class cloth:
    def __init__(self, filename, cloth_type, pos):
        self.image = pygame.image.load("data/cloths/" + filename)

        self.type = cloth_type
        self.x = pos[0]
        self.y = pos[1]

        cloths.append(self)

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def set(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, x, y):
        screen.blit(self.image, (x, y))

    def clothing_on(self):
        self.image = pygame.transform.scale(())
        screen.blit(self.image, ())

    def width(self):
        return self.image.get_width()

    def height(self):
        return self.image.get_height()


j = cloth('j.png', 'bottom', (22, 200))
j.scale(120, 110)
sj = cloth('sj.png', 'bottom', (180, 200))
sj.scale(125, 75)
s = cloth('s.png', 'top', (250, 20))
s.scale(175, 135)
sl = cloth('sl.png', 'top', (480, 20))
sl.scale(130, 95)
lt = cloth('lt.png', 'top', (680, 20))
lt.scale(175, 135)
t = cloth('t.png', 'top', (20, 20))
t.scale(160, 135)
sn = cloth('sn.png', 'footwear', (21, 400))
sn.scale(120, 50)
sg = cloth('sg.png', 'acc', (150, 400))
sg.scale(100, 40)

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    if not dragging:
        j.set()
        sj.set()
        lt.set()
        s.set()
        sl.set()
        t.set()
        sn.set()
        sg.set()

    else:
        dragging_cloth.move(click_x - dragging_cloth.width() // 2, click_y - dragging_cloth.height() // 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                character = pygame.image.load("data/character/" + character_name[random.randint(0, 2)])
                character = pygame.transform.scale(character, (200, 334))

        if event.type == pygame.MOUSEBUTTONUP:
            click_x = event.pos[0]
            click_y = event.pos[1]

            if event.button == 1:
                if not dragging:
                    for cloth in cloths:
                        if cloth.x <= click_x <= cloth.x + cloth.width() and click_y <= click_y <= click_y + cloth.height():
                            dragging = True
                            dragging_cloth = cloth
                            break

                else:
                    dragging_cloth.x = click_x - dragging_cloth.width() // 2
                    dragging_cloth.y = click_y - dragging_cloth.height() // 2
                    dragging = False

        if event.type == pygame.MOUSEMOTION:
            click_x = event.pos[0]
            click_y = event.pos[1]

    pygame.display.update()
    pygame.time.Clock().tick(60)
