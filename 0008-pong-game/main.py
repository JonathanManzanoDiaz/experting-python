# Example file showing a basic pygame "game loop"
import pygame
from pygame.locals import *

# pygame setup
pygame.init()

screen_width = 800
screen_height = 600


fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong by Jonathan Manzano Diaz")

# define font
font = pygame.font.SysFont('Constatia', 30)

# define game variables
margin = 60

# define colors
live_ball = False
bg = (0,0,0)
white = (255,255,255)
cpu_score = 0
player_score = 0
fps = 60
winner = 0
start = 'Click for continue'


def draw_board():
  screen.fill(bg)
  pygame.draw.line(screen, white, (0, margin), (screen_width, margin))


def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


class Paddle():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.rect = Rect(self.x, self.y, 20, 100)
    self.speed = 5
  
  def move(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and self.rect.top > margin +5:
      self.rect.move_ip(0, -1 * self.speed)
    if key[pygame.K_s] and self.rect.bottom < screen_height -5:
      self.rect.move_ip(0, self.speed)

  def ai(self):
    #ai move to paddle automatically
    #move down
    if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
      self.rect.move_ip(0, self.speed)
    #move up
    if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
      self.rect.move_ip(0, -1 * self.speed)
      
    
  
  
  def draw(self):
    pygame.draw.rect(screen, white, self.rect)



class Ball():
  def __init__(self, x, y):
    self.reset(x, y)
    
  def move(self):
    
    #add collision detection


    #check collision with top margin
    if self.rect.top < margin:
      self.speed_y *= -1
    #check collision with bottom screen
    if self.rect.bottom > screen_height:
      self.speed_y *= -1

    #add collision detection with paddles
    if self.rect.colliderect(player_paddle.rect) or self.rect.colliderect(cpu_paddle.rect):
      self.speed_x *= -1

    #check out of bounds
    if self.rect.left < 0:
      self.winner = -1
    if self.rect.right > screen_width:
      self.winner = 1
    
    #update ball position
    self.rect.x += self.speed_x
    self.rect.y += self.speed_y
    
    return self.winner
    
    
  def draw(self):
    pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
  
  def reset(self, x, y):
    self.x = x
    self.y = y
    self.ball_rad = 8
    self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
    self.speed_x = -4
    self.speed_y = 4
    self.winner = 0
    
# Create paddle
player_paddle = Paddle(10, screen_height // 2)
cpu_paddle = Paddle(screen_width - 40, screen_height // 2)

#create pong ball
pong = Ball(30, screen_height // 2 + 40)

last_point = ""

running = True
while running:
  fpsClock.tick(fps)
  draw_board()
  draw_text('CPU: ' + str(cpu_score), font, white, screen_width -100, 20)
  draw_text('Player: ' + str(player_score), font, white, 20, 20)
  
  if not live_ball:
    draw_text("CLICK ANYWHERE or PRESS SPACE for continue", font, white, 160, screen_height // 2)
    if last_point != "":
        draw_text(last_point, font, white, screen_width // 2 - 50, 100)
  #draw paddles
  player_paddle.draw()
  cpu_paddle.draw()
  
  
  if live_ball:
    # move ball
    winner = pong.move()
    if winner == 0:
      # move paddle
      player_paddle.move()
      #move ai
      cpu_paddle.ai()
      # draw ball
      pong.draw()
    else:
      live_ball = False
      if winner == 1:
        player_score += 1
        last_point = "PLAYER SCORE"
      elif winner == -1:
        cpu_score += 1
        last_point = "CPU SCORE"

      
    
    
  
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if (event.type == pygame.MOUSEBUTTONDOWN and not live_ball) or \
        (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not live_ball):
      live_ball = True
      pong.reset(30, screen_height // 2 + 40)
  
  pygame.display.update()

pygame.quit()