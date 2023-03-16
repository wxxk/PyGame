import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

# 원 만들기 : x, y 좌표 필요
# 배경의 크기를 가지고 와서 중앙값을 구하기
x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                y_pos -= 10
            if event.key == pygame.K_DOWN:
                print("DOWN")
                y_pos += 10
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
                x_pos += 10
            if event.key == pygame.K_LEFT:
                print("LEFT")
                x_pos -= 10

    # 배경색깔 채우기
    background.fill((255, 255, 255))

    # 공을 그려주는 명령어 (위치, 색, 중앙, 반지름)
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.display.update()
pygame.quit()
