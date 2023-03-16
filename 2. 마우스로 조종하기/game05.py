import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            print("MOUSEMOTION")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MOUSEBUTTONDOWN")
        if event.type == pygame.MOUSEBUTTONUP:
            print("MOUSEBUTTONUP")

pygame.QUIT()
