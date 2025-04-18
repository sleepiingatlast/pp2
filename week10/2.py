import pygame
import random
import sys
import psycopg2

#коннект с базой
con = psycopg2.connect(
    #dbname="snake_game",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cur = con.cursor()

def create_user_score_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER,
            score INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    con.commit()


def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        con.commit()
        return cur.fetchone()[0]

def get_current_level(user_id):
    cur.execute("SELECT MAX(level) FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()[0]
    return result if result else 1

def save_score(user_id, level, score):
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
                (user_id, level, score))
    con.commit()

#вводы юзера перед началом игры
create_user_score_table()
username = input("enter your username: ")
user_id = get_or_create_user(username)
level = get_current_level(user_id)


#сама игра уже 
pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels')

font = pygame.font.SysFont("Verdana", 20)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)

clock = pygame.time.Clock()
                                                                                    
#настраиваем змейку
snake = [(100, 100), (80, 100), (60, 100)]  #параметры тела
direction = 'RIGHT'
speed = 6
score = 0
level = 1

#стены
walls = []
for x in range(0, WIDTH, CELL_SIZE):
    walls.append((x, 0))
    walls.append((x, HEIGHT - CELL_SIZE))
for y in range(0, HEIGHT, CELL_SIZE):
    walls.append((0, y))
    walls.append((WIDTH - CELL_SIZE, y))

#генерируем еду не на стене или положении змеи
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            return (x, y)

food = generate_food()

def draw_elements():
    screen.fill(BLACK)

    #рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, BLUE, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    #рисуем еду
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

    #рисуем стены
    for wall in walls:
        pygame.draw.rect(screen, GREEN, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))

    #лвл и очки 
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

#столкновение со стеной или с собой чекаем
def check_collision():
    head = snake[0]
    if head in walls or head in snake[1:]:
        return True
    return False

running = True
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #движения
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'

    #змею двигаем
    x, y = snake[0]
    if direction == 'UP':
        y -= CELL_SIZE
    elif direction == 'DOWN':
        y += CELL_SIZE
    elif direction == 'LEFT':
        x -= CELL_SIZE
    elif direction == 'RIGHT':
        x += CELL_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)

    #съела ли еду
    if new_head == food:
        score += 1
        food = generate_food()
        #увеличиваем скор и скорость
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()  #отрезаем хвост если не съела

    if check_collision():
        print("Game Over")
        running = False

    draw_elements()
    pygame.display.update()

pygame.quit()
sys.exit()