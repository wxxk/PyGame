import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

fps = pygame.time.Clock()

image_bg = pygame.image.load("image/bg.jpg")
image_banana = pygame.image.load("image/ba.png")
image_dog = pygame.image.load("image/dog.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

size_dog_width = image_dog.get_rect().size[0]
size_dog_height = image_dog.get_rect().size[1]

x_pos_dog = (size_bg_width / 2) - (size_dog_width / 2)
y_pos_dog = size_bg_height - size_dog_height

x_speed_banana = 1
y_speed_banana = 1

to_x = 0

point = 0
font_point = pygame.font.SysFont(None, 30)

font_gameover = pygame.font.SysFont(None, 80)
font_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))

size_text_width = font_gameover.get_rect().size[0]
size_text_height = font_gameover.get_rect().size[1]

x_pos_text = (size_bg_width / 2) - (size_text_width / 2)
y_pos_text = (size_bg_height / 2) - (size_text_height / 2)

play = True
while play:
    deltaTime = fps.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x = 1
            if event.key == pygame.K_LEFT:
                to_x = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_LEFT:
                to_x = 0

    if x_pos_dog < 0:
        x_pos_dog = 0
    elif x_pos_dog > size_bg_width - size_dog_width:
        x_pos_dog = size_bg_width - size_dog_width
    else:
        x_pos_dog += to_x

    x_pos_banana += x_speed_banana
    y_pos_banana += y_speed_banana

    if x_pos_banana <= 0:
        x_pos_banana = 0
        x_speed_banana = -x_speed_banana
    elif x_pos_banana >= size_bg_width - size_banana_width:
        x_pos_banana = size_bg_width - size_banana_width
        x_speed_banana = -x_speed_banana

    if y_pos_banana <= 0:
        y_pos_banana = 0
        y_speed_banana = -y_speed_banana
    elif y_pos_banana >= size_bg_height - size_banana_height:
        background.blit(font_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(2000)
        play = False

    rect_banana = image_banana.get_rect()
    rect_banana.left = x_pos_banana
    rect_banana.top = y_pos_banana

    rect_bog = image_dog.get_rect()
    rect_bog.left = x_pos_dog
    rect_bog.top = y_pos_dog

    if rect_bog.colliderect(rect_banana):
        x_speed_banana = -x_speed_banana
        y_speed_banana = -y_speed_banana
        point += 1

    background.blit(image_bg, (0, 0))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))
    background.blit(image_dog, (x_pos_dog, y_pos_dog))

    text_point = font_point.render(str(point), True, (0, 0, 0))
    background.blit(text_point, (10, 10))
    pygame.display.update()

pygame.quit()
