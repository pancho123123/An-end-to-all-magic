import pygame
from random import randint
import random


WIDTH = 1300
HEIGHT = 700

BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
# PLOMO = (122,122,122)
# BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("An End To All Magic")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 4
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, BLACK, border, 1)

def draw_hp_bar3(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, RED, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar4(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

def draw_hp_bar5(surface, x, y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, YELLOW, fill)
	pygame.draw.rect(surface, BLACK, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/player.png").convert(),(50,65))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.speed = 0
		self.hp = 100
		self.mana = 100
		self.dir_num = 1
		self.jump_counter = True
		self.counter = True
		self.start_time = 0
		self.drag = False
		self.counter2 = True
		self.drag_dir = 0
		self.start_time2 = 0

	def jump(self):
		if self.dir_num == 1:
			self.rect.y -= 200
		elif self.dir_num == 2:
			self.rect.x += 100
			self.rect.y -= 100
		elif self.dir_num == 3:
			self.rect.x += 200
		elif self.dir_num == 4:
			self.rect.x += 100
			self.rect.y += 100
		elif self.dir_num == 5:
			self.rect.y += 200
		elif self.dir_num == 6:
			self.rect.x -= 100
			self.rect.y += 100
		elif self.dir_num == 7:
			self.rect.x -= 200
		else:
			self.rect.x -= 100
			self.rect.y -= 100
		
class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.centerx = WIDTH//2 - 50
		self.rect.centery = HEIGHT//2
		
	def update(self):
		now = pygame.time.get_ticks()
		if not self.jump_counter:
			if self.counter:
				self.start_time = pygame.time.get_ticks()
				self.counter = False
		if not self.counter:
			if now - self.start_time >= 4000:
				self.counter = True
				self.jump_counter = True
		if self.drag:
			if now - self.start_time2 <= 700:
				if self.drag_dir == 1:
					self.rect.y += 4
				elif self.drag_dir == 2:
					self.rect.x -= 4
				elif self.drag_dir == 3:
					self.rect.y -= 4
				else:
					self.rect.x += 4
			else:
				self.drag = False
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
					
		if self.hp > 100:
			self.hp = 100
		if self.hp <= 0:
			self.hp = 0
			self.kill()
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if not self.drag:
			if keystate[pygame.K_a]:
				self.speed_x = -4
			if keystate[pygame.K_d]:
				self.speed_x = 4
			self.rect.x += self.speed_x
			if keystate[pygame.K_w]:
				self.speed_y = -4
			if keystate[pygame.K_s]:
				self.speed_y = 4
		if keystate[pygame.K_a] and not keystate[pygame.K_w] and not keystate[pygame.K_s]:
			self.dir_num = 7
		if keystate[pygame.K_w] and not keystate[pygame.K_a] and not keystate[pygame.K_d]:
			self.dir_num = 1
		if keystate[pygame.K_d] and not keystate[pygame.K_w] and not keystate[pygame.K_s]:
			self.dir_num = 3
		if keystate[pygame.K_s] and not keystate[pygame.K_a] and not keystate[pygame.K_d]:
			self.dir_num = 5
		if keystate[pygame.K_w] and keystate[pygame.K_d]:
			self.dir_num = 2
		if keystate[pygame.K_d] and keystate[pygame.K_s]:
			self.dir_num = 4
		if keystate[pygame.K_s] and keystate[pygame.K_a]:
			self.dir_num = 6
		if keystate[pygame.K_a] and keystate[pygame.K_w]:
			self.dir_num = 8
		self.rect.y += self.speed_y
		if self.rect.left > WIDTH + 50:
			self.rect.left = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700
		

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.centerx = WIDTH//2 + 50
		self.rect.centery = HEIGHT//2
		
	def update(self):
		now = pygame.time.get_ticks()
		if not self.jump_counter:
			if self.counter:
				self.start_time = pygame.time.get_ticks()
				self.counter = False
		if not self.counter:
			if now - self.start_time >= 4000:
				self.counter = True
				self.jump_counter = True
		if self.drag:
			if now - self.start_time2 <= 700:
				if self.drag_dir == 1:
					self.rect.y += 4
				elif self.drag_dir == 2:
					self.rect.x -= 4
				elif self.drag_dir == 3:
					self.rect.y -= 4
				else:
					self.rect.x += 4
			else:
				self.drag = False
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp > 100:
			self.hp = 100
		if self.hp <= 0:
			self.hp = 0
			self.kill()
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if not self.drag:
			if keystate[pygame.K_LEFT]:
				self.speed_x = -4
			if keystate[pygame.K_RIGHT]:
				self.speed_x = 4
			self.rect.x += self.speed_x
			if keystate[pygame.K_UP]:
				self.speed_y = -4
			if keystate[pygame.K_DOWN]:
				self.speed_y = 4
		self.rect.y += self.speed_y
		if keystate[pygame.K_LEFT] and not keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
			self.dir_num = 7
		if keystate[pygame.K_UP] and not keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
			self.dir_num = 1
		if keystate[pygame.K_RIGHT] and not keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
			self.dir_num = 3
		if keystate[pygame.K_DOWN] and not keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
			self.dir_num = 5
		if keystate[pygame.K_UP] and keystate[pygame.K_RIGHT]:
			self.dir_num = 2
		if keystate[pygame.K_RIGHT] and keystate[pygame.K_DOWN]:
			self.dir_num = 4
		if keystate[pygame.K_DOWN] and keystate[pygame.K_LEFT]:
			self.dir_num = 6
		if keystate[pygame.K_LEFT] and keystate[pygame.K_UP]:
			self.dir_num = 8
		
		if self.rect.left > WIDTH + 50:
			self.rect.left = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700


class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.centerx = WIDTH//2
		self.rect.centery = HEIGHT//2 + 20
		
	def update(self):
		now = pygame.time.get_ticks()
		if not self.jump_counter:
			if self.counter:
				self.start_time = pygame.time.get_ticks()
				self.counter = False
		if not self.counter:
			if now - self.start_time >= 4000:
				self.counter = True
				self.jump_counter = True
		if self.drag:
			if now - self.start_time2 <= 700:
				if self.drag_dir == 1:
					self.rect.y += 4
				elif self.drag_dir == 2:
					self.rect.x -= 4
				elif self.drag_dir == 3:
					self.rect.y -= 4
				else:
					self.rect.x += 4
			else:
				self.drag = False
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
					
		if self.hp > 100:
			self.hp = 100
		if self.hp <= 0:
			self.hp = 0
			self.kill()
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if not self.drag:
			if keystate[pygame.K_g]:
				self.speed_x = -4
			if keystate[pygame.K_j]:
				self.speed_x = 4
			self.rect.x += self.speed_x
			if keystate[pygame.K_y]:
				self.speed_y = -4
			if keystate[pygame.K_h]:
				self.speed_y = 4
		if keystate[pygame.K_g] and not keystate[pygame.K_y] and not keystate[pygame.K_h]:
			self.dir_num = 7
		if keystate[pygame.K_y] and not keystate[pygame.K_g] and not keystate[pygame.K_j]:
			self.dir_num = 1
		if keystate[pygame.K_j] and not keystate[pygame.K_y] and not keystate[pygame.K_h]:
			self.dir_num = 3
		if keystate[pygame.K_h] and not keystate[pygame.K_g] and not keystate[pygame.K_j]:
			self.dir_num = 5
		if keystate[pygame.K_y] and keystate[pygame.K_j]:
			self.dir_num = 2
		if keystate[pygame.K_j] and keystate[pygame.K_h]:
			self.dir_num = 4
		if keystate[pygame.K_h] and keystate[pygame.K_g]:
			self.dir_num = 6
		if keystate[pygame.K_g] and keystate[pygame.K_y]:
			self.dir_num = 8
		self.rect.y += self.speed_y
		if self.rect.left > WIDTH + 50:
			self.rect.left = WIDTH + 50
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.bottom > 700:
			self.rect.bottom = 700


class Boss(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/00.png").convert(),(90,90))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH//2
		self.rect.y = 5
		self.image_n = 1
		self.pos_listx = [400,500,600,700,800,900,1000]
		self.pos_listy = [100,180,260,340,420]
		self.start_time = pygame.time.get_ticks()
		self.a = 6000
		self.counter1 = True
		self.counter2 = False
		self.attack_n = randint(8,12)
		self.attack_counter = 0
		self.b = 1000
	
	def update(self):
		now = pygame.time.get_ticks()
		self.image.set_colorkey(WHITE)
		if self.image_n == 1:
			self.rect.y = 10
			self.image = pygame.transform.scale(pygame.image.load("img/1.png").convert(),(90,90))
			self.image.set_colorkey(WHITE)
			if self.counter1:
				if now - self.start_time >= self.a:
					self.rect.x = random.choice(self.pos_listx)
					self.shoot()
					self.counter1 = False
					self.counter2 = True
					self.attack_counter += 1
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
					
			if self.counter2:
				if now - self.start_time >= self.b:
					self.rect.x = random.choice(self.pos_listx)
					self.shoot()
					self.counter2 = False
					self.counter1 = True
					self.a = 1000
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
		elif self.image_n == 2:
			self.rect.x = 1180
			self.image = pygame.transform.scale(pygame.image.load("img/2.png").convert(),(90,90))
			self.image.set_colorkey(WHITE)
			if self.counter1:
				if now - self.start_time >= self.a:
					self.rect.y = random.choice(self.pos_listy)
					self.shoot()
					self.counter1 = False
					self.counter2 = True
					self.attack_counter += 1
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
					
			if self.counter2:
				if now - self.start_time >= self.b:
					self.rect.x = random.choice(self.pos_listy)
					self.shoot()
					self.counter2 = False
					self.counter1 = True
					self.a = 1000
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
		elif self.image_n == 3:
			self.rect.y = 550
			self.image = pygame.transform.scale(pygame.image.load("img/3.png").convert(),(90,90))
			self.image.set_colorkey(WHITE)
			if self.counter1:
				if now - self.start_time >= self.a:
					self.rect.x = random.choice(self.pos_listx)
					self.shoot()
					self.counter1 = False
					self.counter2 = True
					self.attack_counter += 1
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
					
			if self.counter2:
				if now - self.start_time >= self.b:
					self.rect.x = random.choice(self.pos_listx)
					self.shoot()
					self.counter2 = False
					self.counter1 = True
					self.a = 1000
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
		else:
			self.rect.x = 300
			self.image = pygame.transform.scale(pygame.image.load("img/4.png").convert(),(90,90))
			self.image.set_colorkey(WHITE)
			if self.counter1:
				if now - self.start_time >= self.a:
					self.rect.y = random.choice(self.pos_listy)
					self.shoot()
					self.counter1 = False
					self.counter2 = True
					self.attack_counter += 1
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()
					
			if self.counter2:
				if now - self.start_time >= self.b:
					self.rect.y = random.choice(self.pos_listy)
					self.shoot()
					self.counter2 = False
					self.counter1 = True
					self.a = 1000
					if self.attack_n > self.attack_counter:
						self.attack_counter += 1
					else:
						self.image_n = randint(1,4)
						self.attack_counter = 0
						self.attack_n = randint(8,12)
					self.start_time = pygame.time.get_ticks()

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.centery, self.image_n)
		all_sprites.add(bullet)
		bullets.add(bullet)
		blast_sound.play()



class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y,number):
		super().__init__()
		self.n = number
		if self.n == 1:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet1.png"),(100,100)).convert()
		if self.n == 2:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet2.png"),(100,100)).convert()
		if self.n == 3:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet3.png"),(100,100)).convert()
		if self.n == 4:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet4.png"),(100,100)).convert()
		
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speed = 6
		self.counter_p1 = True
		self.counter_p2 = True
		self.counter_p3 = True
		

	def update(self):
		self.image.set_colorkey(WHITE)
		if self.n == 1:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet1.png"),(100,100)).convert()
			self.image.set_colorkey(WHITE)
			self.rect.y += self.speed
			if self.rect.top > 600:
				self.kill()
		if self.n == 2:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet2.png"),(100,100)).convert()
			self.image.set_colorkey(WHITE)
			self.rect.x -= self.speed
			if self.rect.right < 330:
				self.kill()
		if self.n == 3:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet3.png"),(100,100)).convert()
			self.image.set_colorkey(WHITE)
			self.rect.y -= self.speed
			if self.rect.bottom < 150:
				self.kill()
		if self.n == 4:
			self.image = pygame.transform.scale(pygame.image.load("img/bullet4.png"),(100,100)).convert()
			self.image.set_colorkey(WHITE)
			self.rect.x += self.speed
			if self.rect.left > 1200:
				self.kill()

def show_game_over_screenp1():
	screen.fill(BLACK)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp5():
	screen.fill(BLACK)
	draw_text1(screen, "Draw", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False


blast_sound = pygame.mixer.Sound("sound/blast.wav")
invo_talk_sound = pygame.mixer.Sound("sound/dial.wav")

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(),(1300,700))


game_over1 = False
game_over2 = False
game_over3 = False
game_over5 = False
running = True
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
player3 = Player3()

players.add(player1, player2, player3)
boss = Boss()
all_sprites.add(player1, player2, player3, boss)
counter = True
start_time = pygame.time.get_ticks()
invo_talk_sound.play()


while running:
	if game_over1:
		game_over1 = False
		show_game_over_screenp1()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		players.add(player1, player2, player3)
		boss = Boss()
		all_sprites.add(player1, player2, player3, boss)
		counter = True
		start_time = pygame.time.get_ticks()
		invo_talk_sound.play()
	
	if game_over2:
		game_over2 = False
		show_game_over_screenp2()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		players.add(player1, player2, player3)
		boss = Boss()
		all_sprites.add(player1, player2, player3, boss)
		counter = True
		start_time = pygame.time.get_ticks()
		invo_talk_sound.play()

	if game_over3:
		game_over3 = False
		show_game_over_screenp3()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		players.add(player1, player2, player3)
		boss = Boss()
		all_sprites.add(player1, player2, player3, boss)
		counter = True
		start_time = pygame.time.get_ticks()
		invo_talk_sound.play()

	if game_over5:
		game_over5 = False
		show_game_over_screenp5()
		player1 = Player1()
		player2 = Player2()
		player3 = Player3()
		players.add(player1, player2, player3)
		boss = Boss()
		all_sprites.add(player1, player2, player3, boss)
		start_time = pygame.time.get_ticks()
		invo_talk_sound.play()

	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				if player2.hp > 0:
					if player2.jump_counter:
						if player2.mana >= 10:
							player2.jump()
							player2.mana -= 10
							player2.jump_counter = False
				else:
					pass
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_f:
				if player1.hp > 0:
					if player1.jump_counter:
						if player1.mana >= 10:
							player1.jump()
							player1.mana -= 10
							player1.jump_counter = False
				else:
					pass

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_k:
				if player3.hp > 0:
					if player3.jump_counter:
						if player3.mana >= 10:
							player3.jump()
							player3.mana -= 10
							player3.jump_counter = False
				else:
					pass

	if player1.hp <= 0 or player1.rect.left > 1250 or player1.rect.right < 350 or player1.rect.bottom < 100 or player1.rect.top > 530:
		player1.kill()
		
	if player2.hp <= 0 or player2.rect.left > 1250 or player2.rect.right < 350 or player2.rect.bottom < 100 or player2.rect.top > 530:
		player2.kill()

	if player3.hp <= 0 or player3.rect.left > 1250 or player3.rect.right < 350 or player3.rect.bottom < 100 or player3.rect.top > 530:
		player3.kill()

	if len(players) == 1:
		if player1 in players:
			game_over1 = True
			player1.kill()
		elif player2 in players:
			game_over2 = True
			player2.kill()
		elif player3 in players:
			game_over3 = True
			player3.kill()
		counter = False
		boss.kill()
	if counter:
		if len(players) == 0:
			game_over5 = True
			boss.kill()

	# Checar colisiones - boss - bullets
	for bullet in bullets:
		for p in players:
			if pygame.sprite.collide_rect(bullet, p):
				if bullet.counter_p1:
					if p == player1:
						bullet.counter_p1 = False
						if bullet.n == 1:
							p.drag_dir = 1
						elif bullet.n == 2:
							p.drag_dir = 2
						elif bullet.n == 3:
							p.drag_dir = 3
						else:
							p.drag_dir = 4
						p.drag = True
						p.start_time2 = pygame.time.get_ticks()
						p.hp -= 8
				if bullet.counter_p2:
					if p == player2:
						bullet.counter_p2 = False
						if bullet.n == 1:
							p.drag_dir = 1
						elif bullet.n == 2:
							p.drag_dir = 2
						elif bullet.n == 3:
							p.drag_dir = 3
						else:
							p.drag_dir = 4
						p.drag = True
						p.start_time2 = pygame.time.get_ticks()
						p.hp -= 8
				if bullet.counter_p3:
					if p == player3:
						bullet.counter_p3 = False
						if bullet.n == 1:
							p.drag_dir = 1
						elif bullet.n == 2:
							p.drag_dir = 2
						elif bullet.n == 3:
							p.drag_dir = 3
						else:
							p.drag_dir = 4
						p.drag = True
						p.start_time2 = pygame.time.get_ticks()
						p.hp -= 8


	all_sprites.update()

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	for p in players:
		if p.hp > 0:
			if p == player1:
				draw_hp_bar3(screen, p.rect.x, p.rect.y - 10, p.hp)
				draw_hp_bar2(screen, p.rect.x, p.rect.y - 1, p.mana)
			if p == player2:
				draw_hp_bar4(screen, p.rect.x, p.rect.y - 10, p.hp)
				draw_hp_bar2(screen, p.rect.x, p.rect.y - 1, p.mana)
			if p == player3:
				draw_hp_bar5(screen, p.rect.x, p.rect.y - 10, p.hp)
				draw_hp_bar2(screen, p.rect.x, p.rect.y - 1, p.mana)
			

	#reloj
	draw_text1(screen, str((pygame.time.get_ticks()- start_time)//1000), 30, 340, 16)

	pygame.display.flip()