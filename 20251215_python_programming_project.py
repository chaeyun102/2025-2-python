import os
import pygame
import random

pygame.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'images')

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('햄버거 쌓기 게임')

clock = pygame.time.Clock()
font = pygame.font.SysFont('malgungothic', 22)
big_font = pygame.font.SysFont('malgungothic', 40)

ingredients = [
    'bun_bottom', 'patty', 'cheese', 'shrimp_patty',
    'chicken', 'tomato', 'bulgogi', 'lettuce',
    'mayonnaise', 'bun_top'
]

recipes = {
    '불고기 버거': ['bun_bottom', 'lettuce', 'tomato', 'bulgogi', 'mayonnaise', 'bun_top'],
    '치즈 버거': ['bun_bottom', 'lettuce', 'tomato', 'patty', 'cheese', 'mayonnaise', 'bun_top'],
    '치킨 버거': ['bun_bottom', 'lettuce', 'tomato', 'chicken', 'mayonnaise', 'bun_top'],
    '새우 버거': ['bun_bottom', 'lettuce', 'tomato', 'shrimp_patty', 'mayonnaise', 'bun_top']
}

name_map = {
    'bun_bottom': '아래빵',
    'lettuce': '양상추',
    'tomato': '토마토',
    'bulgogi': '불고기',
    'patty': '패티',
    'cheese': '치즈',
    'chicken': '치킨',
    'shrimp_patty': '새우패티',
    'mayonnaise': '마요네즈',
    'bun_top': '윗빵'
}

images = {}
for name in ingredients:
    path = os.path.join(IMG_DIR, f'{name}.png')
    images[name] = pygame.transform.scale(
        pygame.image.load(path).convert_alpha(),
        (80, 40)
    )

class Player:
    def __init__(self):
        self.x = WIDTH // 2 - 40
        self.y = HEIGHT - 80
        self.width = 80
        self.height = 15
        self.speed = 5
        self.stack = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        self.x = max(0, min(WIDTH - self.width, self.x))

    def catch(self, name):
        self.stack.append(name)

    def reset(self):
        self.stack.clear()

    def draw(self):
        pygame.draw.rect(screen, (50, 50, 50), (self.x, self.y, self.width, self.height))
        for i, name in enumerate(self.stack):
            screen.blit(images[name], (self.x, self.y - (i + 1) * 40))

class Ingredient:
    def __init__(self):
        self.speed = 5
        self.reset()

    def reset(self):
        self.name = random.choice(ingredients)
        self.x = random.randint(0, WIDTH - 80)
        self.y = -40

    def update(self):
        self.y += self.speed

    def draw(self):
        screen.blit(images[self.name], (self.x, self.y))

class Order:
    def __init__(self):
        self.new_order()

    def new_order(self):
        self.name, self.recipe = random.choice(list(recipes.items()))

    def check(self, stack):
        return stack == self.recipe

player = Player()
ingredient = Ingredient()
order = Order()

money = 0
goal_money = 20000
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over and event.key == pygame.K_SPACE:
                if order.check(player.stack):
                    money += 5000
                else:
                    money -= 3000
                player.reset()
                order.new_order()
                ingredient.reset()
                ingredient.speed += 0.5
                if money < 0:
                    game_over = True

            if game_over and event.key == pygame.K_RETURN:
                money = 0
                game_over = False
                ingredient.speed = 5
                player.reset()
                order.new_order()
                ingredient.reset()

    if not game_over:
        player.update()
        ingredient.update()
        if ingredient.y > player.y - 40:
            if abs(ingredient.x - player.x) < 60:
                player.catch(ingredient.name)
            ingredient.reset()

    screen.fill((255, 255, 255))

    screen.blit(font.render(f'주문: {order.name}', True, (0, 0, 0)), (20, 20))
    screen.blit(font.render(f'돈: {money}원', True, (0, 0, 0)), (20, 50))

    y = 90
    screen.blit(font.render('레시피', True, (0, 0, 0)), (20, y))
    y += 30
    for i, item in enumerate(order.recipe, 1):
        text = f'{i}. {name_map[item]}'
        screen.blit(font.render(text, True, (0, 0, 0)), (20, y))
        y += 25

    screen.blit(font.render('SPACE: 주문 제출', True, (0, 0, 0)), (20, HEIGHT - 40))

    ingredient.draw()
    player.draw()

    if game_over:
        text = big_font.render('GAME OVER (Enter)', True, (255, 0, 0))
        screen.blit(text, ((WIDTH - text.get_width()) // 2, HEIGHT // 2))

    if money >= goal_money:
        text = big_font.render('당신은 최고의 햄버거 요리사!', True, (0, 0, 0))
        screen.blit(text, (40, HEIGHT // 2 - 120))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()