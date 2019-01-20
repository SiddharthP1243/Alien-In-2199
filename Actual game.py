import pygame
import sys

pygame.init()
pygame.display.set_caption("click")
pygame.font.init()
pygame.display.set_caption('font example')
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
clock.tick(60)
Player_pos = (300, 275)
Player_size = 200
Player_size_2 = 50
Colour = (255, 0, 0)
button_1 = pygame.draw.rect(screen, Colour, (Player_pos[0], Player_pos[1], Player_size,Player_size_2))
click = pygame.mouse.get_pressed(button_1)
click = True
 
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render("Wait for 5 seconds for the game to start", True, (0, 0, 0), (255, 0, 0))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

game_over = False
screen.fill((0, 0, 0))

pygame.display.update()
screen.blit(text, textrect)

pygame.display.update()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.key.get_pressed():
            pygame.time.delay(5000)
            
            import pygame
            pygame.init()


            SIZE = WIDTH, HEIGHT = (800, 600)
            FPS = 30
            screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
            clock = pygame.time.Clock()


            def blit_text(surface, text, pos, font, color=pygame.Color('black')):
                words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
                space = font.size(' ')[0]  # The width of a space.
                max_width, max_height = surface.get_size()
                x, y = pos
                for line in words:
                    for word in line:
                        word_surface = font.render(word, 0, color)
                        word_width, word_height = word_surface.get_size()
                        if x + word_width >= max_width:
                            x = pos[0]  # Reset the x.
                            y += word_height  # Start on new row.
                        surface.blit(word_surface, (x, y))
                        x += word_width + space
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.


            text = "It is the year 2199, Hello Leon Clarke. The ozone layer has been depleted. " \
                   "Earth is vulnerable to invasion. The aliens have come to attack Earth." \
                   " We need your help, Leon Clarke, we really do..." \
                   " The controls are arrow keys to move, space to jump and LMB(Left mouse button) to click."
            font = pygame.font.SysFont('Calibri', 44)
            pygame.time.display(10000)
            import pygame
            import sys

            Player_posx = 70
            Player_posy = 128
            Width = 800
            Height = 600
             
            Player_size = 64

            screen = pygame.display.set_mode((Width,Height))

            game_over = False

            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_RIGHT:
                            Player_posx -= 32
                        elif event.key == K_LEFT:
                            Player_posx += 32
                        elif event.key == K_SPACE:


            while True:

                dt = clock.tick(FPS) / 1000

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

                screen.fill(pygame.Color('white'))
                blit_text(screen, text, (20, 20), font)
                pygame.display.update()



                




                
                



        
