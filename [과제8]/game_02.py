import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Game")

player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

coin_size = 20
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = -coin_size
coin_speed = 3

score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
running = True
game_over = False

def reset_game():
    global player_x, player_y, coin_x, coin_y, score, game_over
    player_x = WIDTH // 2
    player_y = HEIGHT - player_size - 10
    coin_x = random.randint(0, WIDTH - coin_size)
    coin_y = -coin_size
    score = 0
    game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        coin_y += coin_speed
        if coin_y > HEIGHT:
            game_over = True

        if (player_x < coin_x + coin_size and
            player_x + player_size > coin_x and
            player_y < coin_y + coin_size and
            player_y + player_size > coin_y):
            score += 1
            coin_x = random.randint(0, WIDTH - coin_size)
            coin_y = -coin_size

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, (255, 255, 0), (coin_x, coin_y, coin_size, coin_size))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 150, 10))

    if game_over:
        over_text = font.render("GAME OVER - Press R to restart", True, (255, 0, 0))
        screen.blit(over_text, (50, HEIGHT // 2 - 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
