import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

font_test = pygame.font.SysFont(None, 30)  # 글자체 이름, 폰트 사이즈
point = 10

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    text = font_test.render(str(point), True, (255, 255, 255))
    background.blit(text, (200, 150))
    pygame.display.update()


pygame.quit()
