import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

# 1초 동안 while문을 몇번이나 동작 시킬 것인가
fps = pygame.time.Clock()

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

# 키보드를 꾹 누르고 있을 때 움직일 수 있게 해주는 변수
to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(60)  # 1초에 60프레임
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -5
            elif event.key == pygame.K_DOWN:
                to_y = 5
            elif event.key == pygame.K_RIGHT:
                to_x = 5
            elif event.key == pygame.K_LEFT:
                to_x = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0

    x_pos += to_x
    y_pos += to_y

    background.fill((255, 255, 255))
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)
    pygame.display.update()

print(event.key)
pygame.quit()
