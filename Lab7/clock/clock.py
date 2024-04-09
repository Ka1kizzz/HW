import pygame
import datetime


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect


pygame.init()

clock_main = pygame.display.set_mode((900, 700))
h = pygame.image.load("clock_main.png")
h = pygame.transform.scale(h, clock_main.get_size())
clock_main.blit(h, (0, 0))
clock_second = pygame.image.load("clock_second-removebg-preview .png")
cl = clock_main.get_rect().center

clock_minute = pygame.image.load("clock-removebg-preview.png")

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            exit()
    clock_main.blit(h, (0, 0))
    time_now = datetime.datetime.now()
    seconds_time = time_now.second
    minutes_time = time_now.minute
    some_second, pos_second = rot_center(clock_second, 135 - seconds_time * 6, *cl)
    some_minute, pos_minute = rot_center(clock_minute, 135 - minutes_time * 6, *cl)
    clock_main.blit(some_second, pos_second)
    clock_main.blit(some_minute, pos_minute)
    pygame.display.update()