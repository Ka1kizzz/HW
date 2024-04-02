import random
import pygame
import math

def main():
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Paint')
    work_surf = pygame.Surface((800, 600))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 1
    figure = 'pen'

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0)
    }

    points = list()

    def Rect_pos(x1, y1, x2, y2):
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

    def Square_pos(x1, y1, x2, y2):
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))

    def Equilateral_Triangle_pos(x1, y1, x2, y2):
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2+x2-x1, y1))
        return points

    def Right_Triangle_pos(x1, y1, x2, y2):
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x1, y2))
        return points

    def Rhombus_pos(x1, y1, x2, y2):
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x2-x1+x2, y1))
        points.append((x2, y1+y1-y2))
        return points

    done = False
    while not done:
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = 'red'
                if event.key == pygame.K_2:
                    mode = 'blue'
                if event.key == pygame.K_3:
                    mode = 'green'
                if event.key == pygame.K_r:
                    figure = 'rectangle'
                if event.key == pygame.K_p:
                    figure = 'pen'
                if event.key == pygame.K_e:
                    figure = 'erase'
                if event.key == pygame.K_c:
                    figure = 'circle'
                if event.key == pygame.K_s:
                    figure = 'square'
                if event.key == pygame.K_u:
                    figure = 'equilateral triangle'
                if event.key == pygame.K_t:
                    figure = 'right triangle'
                if event.key == pygame.K_a:
                    figure = 'rhombus'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                draw_on = True
                last_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                work_surf.blit(screen, (0, 0))
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    if figure == 'pen':
                        pygame.draw.line(screen, color, last_pos, event.pos, radius)
                        last_pos = event.pos
                    if figure == 'erase':
                        pygame.draw.circle(screen, (0, 0, 0), (event.pos[0], event.pos[1]), 6)
                    if figure == 'rectangle':
                        t = Rect_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'square':
                        t = Square_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.rect(screen, color, pygame.Rect(t))
                    if figure == 'equilateral triangle':
                        t = Equilateral_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = []
                    if figure == 'right triangle':
                        t = Right_Triangle_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = []
                    if figure == 'rhombus':
                        t = Rhombus_pos(last_pos[0], last_pos[1], event.pos[0], event.pos[1])
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.polygon(screen, color, t)
                        points = []
                    if figure == 'circle':
                        screen.blit(work_surf, (0, 0))
                        pygame.draw.circle(screen, color, (last_pos[0], last_pos[1]), int(math.sqrt((event.pos[0]-last_pos[0])**2 + (event.pos[1]-last_pos[1])**2)))

        pygame.display.flip()

    pygame.quit()

main()
