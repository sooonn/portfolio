import pygame
# pylint: disable=no-member
import sys
import random


pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Avoiding Coconut')
icon = pygame.image.load('coconut.png')
pygame.display.set_icon(icon)

Clock = pygame.time.Clock()

background = pygame.image.load('background.png')
character = pygame.image.load('character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 0.8

enemy = pygame.image.load('enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 8.5

enemy2 = pygame.image.load('enemy2.png')
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randint(0, screen_width - enemy2_width)
enemy2_y_pos = 0
enemy2_speed = 10

enemy3 = pygame.image.load('enemy3.png')
enemy3_size = enemy3.get_rect().size
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_x_pos = random.randint(0, screen_width - enemy3_width)
enemy3_y_pos = 0
enemy3_speed = 12

to_y = 0

game_font = pygame.font.Font(None, 50)
total_time = 50
start_ticks = pygame.time.get_ticks()

pygame.mixer.init()
pygame.mixer.music.load('background_music.wav') 
pygame.mixer.music.play(-1)
#game_over_sound = pygame.mixer.Sound('game_over.wav')


running = True
while running:
    dt = Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    enemy_y_pos += to_y * dt
    enemy2_y_pos += to_y * dt
    enemy3_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    enemy2_y_pos += enemy2_speed
    enemy3_y_pos += enemy3_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    if enemy2_y_pos > screen_height:
        enemy2_y_pos = 0
        enemy_2x_pos = random.randint(0, screen_width - enemy2_width)

    if enemy3_y_pos > screen_height:
        enemy3_y_pos = 0
        enemy_3x_pos = random.randint(0, screen_width - enemy3_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos))

    if character_rect.colliderect(enemy_rect) or character_rect.colliderect(enemy2_rect) or character_rect.colliderect(enemy3_rect):
        game_message = "Game Over"
        running = False

    pygame.display.update()

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_message = "Mission Complete"
        running = False

    pygame.display.update()

text = game_font.render(game_message, True, (255, 0, 0))
text_rect = text.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(text, text_rect)
pygame.display.update()


pygame.time.delay(2000)

pygame.quit()
sys.exit()

