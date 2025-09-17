import pygame
import random
import math

from pygame import MOUSEBUTTONDOWN

pygame.init()
# screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# fps
clock = pygame.time.Clock()

# variable of time and position
last_time = 0
delay = 2000
circle_pos = (640, 360)  # start position
circle_size = 30


# variables game
score = 0
font = pygame.font.Font(None, 36)
clicked = False

#FUNCTIONS
def generate_circle():
    #global for modify the outside variables
    global last_time, circle_pos, score, clicked, miss_text, miss_time, miss_pos
    # get time since opened the game
    now = pygame.time.get_ticks()
    # last time is greater than than 2 seconds
    if now - last_time > delay:
      #generate a random position
      if not clicked:
        score -= 2
      circle_pos = (random.randint(40, screen_width - 40), random.randint(40, screen_height - 40))
      last_time = now
      clicked = False
def click_circle(event):
  # circle position
  cx, cy = circle_pos
  # mouse position
  mouse_x, mouse_y = event.pos
  # distance from mouse (Using AI for this)
  distance = math.sqrt((mouse_x - cx) ** 2 + (mouse_y - cy) ** 2)
  # invoke the variables
  global score, delay, circle_size, clicked
  # if mouse is in distance
  if distance <= circle_size:
    score += 1
    clicked = True
    
  # SCORES DIFFICULTY
  if score >= 20:
    circle_size = 12
    delay = 650
    
  elif score >= 10:
    circle_size = 15
    delay = 800
    
  elif score >= 5:
    circle_size = 20
    delay = 1000
def game_over():
  global running
  if score < 0:
    screen.fill('black')
    gameover_font = pygame.font.Font(None, 100)
    gameover_surface = gameover_font.render("GAME OVER", True, (255, 0, 0))
    gameover_rect = gameover_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(gameover_surface, gameover_rect)
    pygame.display.flip()
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == MOUSEBUTTONDOWN:
          click_circle(event)
          
    # game logic
    generate_circle()

    #fill the screen with white
    screen.fill('white')
    
    # draw
    pygame.draw.circle(screen, 'red', circle_pos, circle_size)
    
    # show score
    text_surface = font.render(f"Score: {score}", True, 'black')
    screen.blit(text_surface, (10, 10))
    game_over()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
