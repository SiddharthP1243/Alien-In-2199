import pygame
import sys

pygame.init()
pygame.display.set_caption('font example')
size = [700, 500]
screen = pygame.display.set_mode(size)
 
clock = pygame.time.Clock()
 
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('You have reached Planet Earth. Welcome!', True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
 
screen.fill((255, 255, 255))
screen.blit(text, textrect)
 
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    clock.tick(20)
