#10. 충돌 판정(Collision)
import pygame
import random
pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Collision")

clock = pygame.time.Clock() 

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")        
    self.image = pygame.transform.scale(self.image, (50, 50))  
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 3

  def update(self): 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    if keys[pygame.K_UP]:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
      self.rect.y += self.speed

  def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


all_sprites = pygame.sprite.Group()  #추가: Sprite 그룹 생성 및 Player / Enemy 추가 #추가: 적 전용 그룹
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

score = 0                                   # 코인 먹은 횟수(게임 느낌)

running = True
game_over = False        #추가: 게임 오버 상태 표시용 플래그
apples = []   # 각 원소: {"rect": Rect, "vx": int, "vy": int},
              #rext:위치정보, vx:x축이동, vy:Y축 이동

#추가: 사과 생성 주기 관리용 카운터
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30   # 프레임마다 체크 (약 0.5초 간격 @60FPS 기준)


def spawn_apple():
    size = 40
    x = WIDTH
    y= HEIGHT

    rect = apple_img.get_rect()
    rect.x = random.randint(0, x - size)
    rect.y = random.randint(-50, -10)
    speed_y = random.randint(1, 3)

    rect = pygame.Rect(x, y, size, size)
    apples.append({"rect": rect, "vx": vx, "vy": vy})   #추가: 리스트에 사과 추가

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #변경: 게임 오버가 아닐 때만 움직임/충돌 처리
  if not game_over:
    all_sprites.update() #추가: game_over == False 일 때만 업데이트


    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_apple()

    #추가: 각 사과 이동 & 충돌 처리
    new_apples = []
    for apple in apples:
      rect = apple["rect"]
      vx = apple["vx"]
      vy = apple["vy"]

      rect.x += vx
      rect.y += vy

      #화면을 완전히 벗어난 사과는 버림
      if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
        continue

      hits = pygame.sprite.spritecollide(player, apples, False)
    if hits:
        # 먹힌 사과는 리스트에 다시 넣지 않음 (즉, 사라짐)
        continue

      apples.append(apple)

    apples = new_apples    #추가: 창은 유지, 상태만 게임오버로

  # ---------------- 그림 그리기 영역 ----------------
  screen.fill((170, 200, 255))  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))  # 땅

  # 초록 원(코인 느낌) - coin_rect 기준으로 중앙 잡기

  pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)  # 장애물 선
 
  all_sprites.draw(screen)  #추가: Sprite 그룹 그리기 (Player + Enemy)

  #추가: 점수 텍스트 출력해서 진짜 게임 느낌
  font = pygame.font.SysFont(None, 24)
  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))


  for apple in apples:
        screen.blit(apple_img, apple["rect"])

  all_sprites.draw(screen)  # (Player + Enemy)

    # 점수 텍스트
  font = pygame.font.SysFont(None, 24)
  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))
    #추가: 게임오버 메시지 (플래그가 True일 때만)
  if game_over:
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2 #글씨 정중앙에 배치
        over_y = (HEIGHT - over_text.get_height()) // 2 
        screen.blit(over_text, (over_x, over_y))

  pygame.display.flip()
  clock.tick(60)
pygame.quit()