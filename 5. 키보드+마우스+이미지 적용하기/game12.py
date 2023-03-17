import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

# 1초 동안 while문을 몇번이나 동작 시킬 것인가
fps = pygame.time.Clock()

image_bg = pygame.image.load("image/bg.jpg")
image_dog = pygame.image.load("image/dog.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_dog_width = image_dog.get_rect().size[0]
size_dog_height = image_dog.get_rect().size[1]

x_pos_dog = (size_bg_width / 2) - (size_dog_width / 2)
y_pos_dog = (size_bg_height - size_dog_height) - 30

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(60)  # 1초에 60프레임
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False
            if event.key == pygame.K_UP:
                to_y = -2
            elif event.key == pygame.K_DOWN:
                to_y = 2
            elif event.key == pygame.K_RIGHT:
                to_x = 2
            elif event.key == pygame.K_LEFT:
                to_x = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0

    x_pos_dog += to_x
    y_pos_dog += to_y

    background.blit(image_bg, (0, 0))
    background.blit(image_dog, (x_pos_dog, y_pos_dog))

    pygame.display.update()

pygame.quit()
