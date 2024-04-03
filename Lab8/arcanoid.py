from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, bricks, color):
        self.canvas = canvas
        self.paddle = paddle
        self.bricks = bricks
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.start_time = time.time()  # Track start time
        self.speed = 1  # Initial speed
        self.hit_bottom = False
        self.x = self.speed
        self.y = -self.speed  # Adjust as needed

    def draw(self):
        current_time = time.time()
        time_difference = current_time - self.start_time
        if time_difference > 30:  # Adjust time duration
            self.speed = 5  # Increase speed

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -self.speed

        # Collision detection with bricks
        for brick in self.bricks:
            brick_pos = self.canvas.coords(brick.id)
            if brick_pos and self.hit_brick(pos, brick_pos):
                self.y = self.speed
                self.canvas.delete(brick.id)
                self.bricks.remove(brick)

        if pos[0] <= 0:
            self.x = self.speed
        if pos[2] >= self.canvas_width:
            self.x = -self.speed

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def hit_brick(self, ball_pos, brick_pos):
        if (brick_pos[0] <= ball_pos[2] <= brick_pos[2] or
                brick_pos[0] <= ball_pos[0] <= brick_pos[2]):
            if (brick_pos[1] <= ball_pos[3] <= brick_pos[3] or
                    brick_pos[1] <= ball_pos[1] <= brick_pos[3]):
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 20, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.start_time = time.time()  # Track start time
        self.paddle_width = 100  # Initial paddle width
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0  # Initialize x attribute
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        current_time = time.time()
        time_difference = current_time - self.start_time
        if time_difference > 60:  # Adjust time duration
            self.paddle_width = 50  # Decrease paddle width

        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


class Brick:
    def __init__(self, canvas, color, x, y, bonus=False):
        self.canvas = canvas
        self.bonus = bonus
        self.id = canvas.create_rectangle(x, y, x + 50, y + 20, fill=color)


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'dark green')

# Create bricks
bricks = []
for i in range(0, 500, 50):
    for j in range(0, 100, 20):
        if random.randint(1, 10) == 1:
            bricks.append(Brick(canvas, "blue", i, j, bonus=True))
        else:
            bricks.append(Brick(canvas, "gray", i, j))

ball = Ball(canvas, paddle, bricks, 'purple')
ball.canvas_height = canvas.winfo_height()
ball.canvas_width = canvas.winfo_width()

while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
