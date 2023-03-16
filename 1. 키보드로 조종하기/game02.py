import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:  # 이벤트 타입이 키보드를 눌렀는지
            if event.key == pygame.K_UP:
                print("UP")
            if event.key == pygame.K_DOWN:
                print("DOWN")
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
            if event.key == pygame.K_LEFT:
                print("LEFT")

pygame.quit()
