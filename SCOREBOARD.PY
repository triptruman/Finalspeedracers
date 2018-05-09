# MAKING DAT SCOREBOARD

import pygame
import sys
pygame.init()

WIDTH = 500
HEIGHT = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
totalPoints = 0

if pygame.K_q:  
    sys.exit()

# font_name = pygame.font.match_font('arial')
# def draw_text(surf, text, size, x, y):
#     font = pygame.font.Font(font_name, size)
#     text_surface = font.render(text, True, WHITE)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     surf.blit(text_surface, text_rect)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

draw_text(screen, str(totalPoints), 34, WIDTH/2, 10)
   