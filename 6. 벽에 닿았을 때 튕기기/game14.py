import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

fps = pygame.time.Clock()

image_bg = pygame.image.load("image/bg.jpg")
image_banana = pygame.image.load("image/ba.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

x_speed_banana = 1
y_speed_banana = 1

play = True
while play:
    deltaTime = fps.tick(600)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

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
        y_pos_banana = size_bg_height - size_banana_height
        y_speed_banana = -y_speed_banana

    background.blit(image_bg, (0, 0))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))
    pygame.display.update()

pygame.quit()
