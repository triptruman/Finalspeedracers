import pygame
import time
pygame.init()
DW = 1280 
DH = 720
score=pygame.display.set_caption("score")
DS = pygame.display.set_mode((DW,DH))
WHITE = (255,255,255)
####i got this code from mr. cozort in class on thursday
### i then sent thic code to gabe, thinking that it would be an easy variable change to make the code work
##gabe got back to me sauing that even after he changed the variables, the code did not work
#i met with my friends brother who is a computer science major and harvery mudd
###he proclaimed to me that surf is a variable the mr. cozort is using
## to know how to display the code, i first need to find where mr. cozort displayed surf
#i know the code workds with mr cozort
font_name = pygame.font.match_font('arial')
def draw_text(score, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        score.blit(text_surface, text_rect)
        time.sleep(2)
draw_text( score, "score", 10, 10, 10)
### the one thing i did not do was look up what surf means
### if ound out that surf is a library in pygame
##i will investigate further