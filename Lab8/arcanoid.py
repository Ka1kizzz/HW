import pygame
import random
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Brick dimensions
BRICK_WIDTH = 80
BRICK_HEIGHT = 30

# Paddle dimensions
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Ball dimensions
BALL_RADIUS = 10

# Define bonuses
BONUS_TYPES = ["unbreakable", "speed", "shrink"]
BONUS_COLORS = {
    "unbreakable": GREEN,
    "speed": BLUE,
    "shrink": RED
}

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arkanoid")

clock = pygame.time.Clock()

# Define fonts
font = pygame.font.Font(None, 36)

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color=WHITE, bonus=None):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bonus = bonus

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 5
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            # Ball is out of bounds, reset the game
            return True

        # Check collisions with paddle
        if pygame.sprite.collide_rect(self, paddle):
            self.speed_y *= -1
            self.rect.bottom = paddle.rect.top

        # Check collisions with bricks
        brick_hit = pygame.sprite.spritecollide(self, bricks, True)
        if brick_hit:
            self.speed_y *= -1
            for brick in brick_hit:
                if brick.bonus:
                    activate_bonus(brick.bonus)
            if len(bricks) == 0:
                # Player wins
                return True
        return False

def activate_bonus(bonus_type):
    if bonus_type == "unbreakable":
        print("Unbreakable bonus activated!")
    elif bonus_type == "speed":
        print("Speed bonus activated!")
        ball.speed_x *= 1.1
        ball.speed_y *= 1.1
    elif bonus_type == "shrink":
        print("Shrink bonus activated!")
        paddle.rect.width -= 20
        if paddle.rect.width < 20:
            paddle.rect.width = 20

# Create sprites
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()
paddle = Paddle()
ball = Ball()

all_sprites.add(paddle, ball)

# Create bricks
for row in range(5):
    for column in range(10):
        brick_color = random.choice([WHITE, BLUE, RED])
        bonus = random.choice([None] + BONUS_TYPES)  # Add None to have bricks with no bonuses
        brick = Brick(column * BRICK_WIDTH + 5, row * BRICK_HEIGHT + 50, brick_color, bonus)
        all_sprites.add(brick)
        bricks.add(brick)

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.speed = -7
            elif event.key == pygame.K_RIGHT:
                paddle.speed = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.speed = 0

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
