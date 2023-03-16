import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("SONOL")

image_bg = pygame.image.load("image/bg.jpg")
image_banana = pygame.image.load("image/ba.png")
image_dog = pygame.image.load("image/dog.png")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_banana_width = image_banana.get_rect().size[0]
size_banana_height = image_banana.get_rect().size[1]

x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

size_dog_width = image_banana.get_rect().size[0]
size_dog_height = image_banana.get_rect().size[1]

x_pos_dog = (size_bg_width / 2) - (size_dog_width / 2)
y_pos_dog = (size_bg_height - size_dog_height) - 30

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.blit(image_bg, (0, 0))
    background.blit(image_dog, (x_pos_dog, y_pos_dog))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))

    pygame.display.update()

pygame.quit()
