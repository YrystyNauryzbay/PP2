import pygame
import random
import psycopg2
import sys

WIDTH, HEIGHT = 600, 400
CELL = 20
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL



conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='232326.Asiko',
    host='localhost'
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) UNIQUE
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    score INTEGER,
    level INTEGER
);
""")
conn.commit()


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Класс Змейка
class Snake:
    def __init__(self):
        self.body = [(COLS//2, ROWS//2)]
        self.direction = (1, 0)
        self.paused = False

    def move(self):
        if self.paused:
            return True
        head = self.body[0]
        new_head = ((head[0] + self.direction[0]) % COLS, (head[1] + self.direction[1]) % ROWS)
        if new_head in self.body or new_head in walls:
            return False
        self.body.insert(0, new_head)
        if new_head == food:
            global score, level, speed
            score += 1
            if score % 5 == 0:
                level += 1
                speed += 2
                create_walls()
            spawn_food()
        else:
            self.body.pop()
        return True

    def change_direction(self, dir):
        if (dir[0]*-1, dir[1]*-1) != self.direction:
            self.direction = dir

def get_or_create_user(name):
    cur.execute("SELECT user_id FROM users WHERE user_name = %s;", (name,))
    row = cur.fetchone()
    if row:
        uid = row[0]
        cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1;", (uid,))
        level_row = cur.fetchone()
        return uid, level_row[0] if level_row else 1
    else:
        cur.execute("INSERT INTO users (user_name) VALUES (%s) RETURNING user_id;", (name,))
        uid = cur.fetchone()[0]
        conn.commit()
        return uid, 1

def save_score(uid):
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s);", (uid, score, level))
    conn.commit()

# Стены по уровням
def create_walls():
    global walls
    walls = []
    if level == 2:
        for i in range(5, COLS - 5):
            walls.append((i, ROWS // 2))
    elif level == 3:
        for i in range(3, ROWS - 3):
            walls.append((COLS // 2, i))
    # больше уровней 

def spawn_food():
    global food
    while True:
        pos = (random.randint(1, COLS - 2), random.randint(1, ROWS - 2))
        if pos not in snake.body and pos not in walls:
            food = pos
            break

# Pygame окно и ввод имени
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with DB")

font = pygame.font.Font(None, 32)
input_box = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50)
user_text = ""
active = True
color_active = pygame.Color('dodgerblue2')
color_inactive = pygame.Color('lightskyblue3')
color = color_inactive

while active:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            color = color_active if input_box.collidepoint(e.pos) else color_inactive
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN:
                active = False
            elif e.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += e.unicode
    screen.fill(BLACK)
    txt = font.render(user_text, True, color)
    input_box.w = max(200, txt.get_width()+10)
    screen.blit(txt, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.flip()

# Запуск игры
snake = Snake()
user_id, level = get_or_create_user(user_text)
score = 0
speed = 10 + (level - 1) * 2
create_walls()
spawn_food()

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP: snake.change_direction((0, -1))
            if e.key == pygame.K_DOWN: snake.change_direction((0, 1))
            if e.key == pygame.K_LEFT: snake.change_direction((-1, 0))
            if e.key == pygame.K_RIGHT: snake.change_direction((1, 0))
            if e.key == pygame.K_SPACE: snake.paused = not snake.paused
            if e.key == pygame.K_s: save_score(user_id)

    if not snake.move():
        running = False


    for x, y in snake.body:
        pygame.draw.rect(screen, WHITE, (x * CELL, y * CELL, CELL, CELL))
    pygame.draw.rect(screen, RED, (food[0] * CELL, food[1] * CELL, CELL, CELL))
    for x, y in walls:
        pygame.draw.rect(screen, (0, 255, 255), (x * CELL, y * CELL, CELL, CELL))

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(speed)


save_score(user_id)
pygame.quit()
conn.close()


