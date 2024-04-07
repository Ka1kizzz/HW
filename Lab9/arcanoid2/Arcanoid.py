import pygame
from random import randrange as rnd

WIDTH, HEIGHT = 1200, 800
FPS = 60

paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256),)for i in range(10) for j in range(4)]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
image = pygame.image.load('1.jpg').convert()

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left

    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                elif event.key == pygame.K_s:
                    settings_menu()

        screen.blit(image, (0, 0))
        font = pygame.font.Font(None, 64)
        text = font.render("Press SPACE to start", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        settings_text = font.render("Press S for Settings", True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(settings_text, settings_rect)

        pygame.display.flip()
        clock.tick(FPS)

def settings_menu():
    pass

def game_loop():
    global dx, dy, FPS
    paused = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if not paused:
            screen.blit(image, (0, 0))
            [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
            pygame.draw.rect(screen, pygame.Color('darkorange'), paddle)
            pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_radius)

            ball.x += ball_speed * dx
            ball.y += ball_speed * dy

            if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
                dx = -dx
            if ball.centery < ball_radius:
                dy = -dy
            if ball.colliderect(paddle) and dy > 0:
                dx, dy = detect_collision(dx, dy, ball, paddle)
            hit_index = ball.collidelist(block_list)
            if hit_index != -1:
                hit_rect = block_list.pop(hit_index)
                hit_color = color_list.pop(hit_index)
                dx, dy = detect_collision(dx, dy, ball, hit_rect)
                hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
                pygame.draw.rect(screen, hit_color, hit_rect)
                FPS += 2

            if ball.bottom > HEIGHT:
                print('GAME OVER !!!')
                pygame.quit()
                exit()
            elif not len(block_list):
                print('WIN !!!')
                pygame.quit()
                exit()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddle_speed
            if key[pygame.K_RIGHT] and paddle.right < WIDTH:
                paddle.right += paddle_speed

        if paused:
            font = pygame.font.Font(None, 64)
            text = font.render("Paused", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

main_menu()
game_loop()
