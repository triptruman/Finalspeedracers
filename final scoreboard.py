import pygame
import time
pygame.init()

DW = 1280
DH = 720

DS = pygame.display.set_mode((DW,DH))
pygame.display.set_caption("score")

WHITE = (255,255,255)



font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
        font = pygame.font.font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surf.blit(text_surface, text_rect)
        time.sleep(2)

draw_text(surf, "test", 10, 10, 10)