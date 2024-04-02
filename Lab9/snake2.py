```python
import pygame as pg
import random
import time
from collections import namedtuple

pg.init()

font = pg.font.SysFont("Roboto-Bold .ttf", 30, True)
bigfont = pg.font.SysFont("Roboto-Bold .ttf", 50, True)


class Direction():
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'


Point = namedtuple('Point', 'x y')

WHITE = (255, 255, 255)
GOLD = (255, 223, 0)
RED = (200, 0, 0)
GREEN1 = (200, 155, 0)
GREEN2 = (255, 255, 0)
GREEN3 = (0, 40, 0)
BLACK = (0, 0, 0)
GRASS = (204, 153, 255)

BLOCK_SIZE = 20
SPEED = 7
running = True
game_over = False


class Game:
    def __init__(self, WIDTH=800, HEIGHT=600):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Snake')

        self.direction = Direction.RIGHT
        self.head = Point(self.WIDTH // 2, self.HEIGHT // 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.megafood_exists = False
        self.level = 0
        self.score = 0
        self.food = None
        self.megafood = None
        self.current = 0
        self.start = 0
        self.difference = 0
        self.counter = 10
        self.food_move()

    def food_move(self):
        x = random.randint(0, (self.WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()

    def megafood_move(self):
        x = random.randint(0, (self.WIDTH - BLOCK_SIZE * 2) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.HEIGHT - BLOCK_SIZE * 2) // BLOCK_SIZE) * BLOCK_SIZE
        self.start = time.time()
        self.megafood = Point(x, y)
        if self.food in self.snake:
            self.megafood_move()

    def play_step(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pg.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pg.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pg.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        self.move(self.direction)
        self.snake.insert(0, self.head)

        if self.collision():
            global game_over
            game_over = True

        if self.head == self.food:
            self.score += 1
            self.food_move()
            if self.score // 5 > self.level:
                global SPEED
                if random.randint(1, 2) == 1 and not self.megafood:
                    self.megafood_exists = True
                    self.megafood_move()
                SPEED += 3
                self.level = (SPEED - 7) // 3
        else:
            self.snake.pop()

        if self.head == self.megafood:
            self.score += 10
            self.megafood_exists = False

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        if self.head.x > self.WIDTH - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.HEIGHT - BLOCK_SIZE or self.head.y < 0:
            pg.display.flip()
            return True
        if self.head in self.snake[1:]:
            return True
        return False

    def update(self):
        self.display.fill(GRASS)
        for skin in self.snake:
            pg.draw.rect(self.display, GREEN1, pg.Rect(skin.x, skin.y, BLOCK_SIZE, BLOCK_SIZE))
            pg.draw.rect(self.display, GREEN2, pg.Rect(skin.x + 4, skin.y + 4, 12, 12))

        pg.draw.rect(self.display, RED, pg.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        if self.megafood_exists:


pg.draw.rect(self.display, BLACK, pg.Rect(self.megafood.x, self.megafood.y, BLOCK_SIZE, BLOCK_SIZE))
pg.draw.rect(self.display, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
             pg.Rect(self.megafood.x + 4, self.megafood.y + 4, 12, 12))

text1 = font.render(f"Score: {self.score}", True, WHITE)
text2 = font.render(f"Level: {self.level}", True, WHITE)

self.current = time.time()
self.difference = abs(int(self.current - self.start - self.counter))
if self.start + self.counter - self.current >= 0:
    text4 = font.render(str(self.difference), True, WHITE)

self.display.blit(text1, (10, 10))
self.display.blit(text2, (10, 30))

if self.megafood_exists and self.start + self.counter - self.current >= 0:
    self.display.blit(text4, (10, 50))
else:
    self.megafood_exists = False

if self.collision():
    text3 = bigfont.render(f"Press R to Restart", True, WHITE)
    self.display.blit(text3, (self.HEIGHT // 2 - 50, self.WIDTH // 2 - 140))
pg.display.flip()


def move(self, direction):
    x = self.head.x
    y = self.head.y
    if direction == Direction.RIGHT:
        x += BLOCK_SIZE
    elif direction == Direction.LEFT:
        x -= BLOCK_SIZE
    elif direction == Direction.DOWN:
        y += BLOCK_SIZE
    elif direction == Direction.UP:
        y -= BLOCK_SIZE
    self.head = Point(x, y)


game = Game()
while running:
    score = game.play_step()
    if game_over == True:
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        SPEED = 7
                        game = Game()
                        game_over = False

pg.quit()
exit()