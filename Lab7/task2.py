import pygame
import os
import time

pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 200

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

path = "C:\\Users\\antos\\Desktop\\music"
list_of_music = os.listdir(path)
current = 0

while True:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_p]:
        pygame.mixer.music.load(os.path.join(path, list_of_music[current]))
        pygame.mixer.music.play(1)

    elif key[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    elif key[pygame.K_n]:
        if current == len(list_of_music) - 1:
            current = 0
        else:
            current += 1
        pygame.mixer.music.load(os.path.join(path, list_of_music[current]))
        pygame.mixer.music.play(1)

    elif key[pygame.K_b]:
        if current == 0:
            current = len(list_of_music) - 1
        else:
            current -= 1
        pygame.mixer.music.load(os.path.join(path, list_of_music[current]))
        pygame.mixer.music.play(1)

    if pygame.mixer.music.get_busy():
        progress = pygame.mixer.music.get_pos() / 1000
        pygame.draw.rect(window, BLACK, (50, 100, progress * 10, 20))
        pygame.draw.rect(window, BLACK, (45 + progress * 10, 95, 10, 30))

    pygame.display.update()
    time.sleep(0.1)
