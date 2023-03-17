import pygame

# 초기화 및 디스플레이 설정
pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("UniverseGame")

# 이미지 불러오기
image_bg = pygame.image.load("universe/moon.jpg")
image_dog = pygame.image.load("universe/dog.png")
image_rocket = pygame.image.load("universe/rocket.png")
image_star = pygame.image.load("universe/star.png")
image_ball = pygame.image.load("universe/ball.png")

# 이미지의 가로, 세로 크기 구하기
size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_dog_width = image_dog.get_rect().size[0]
size_dog_height = image_dog.get_rect().size[1]

size_rocket_width = image_rocket.get_rect().size[0]
size_rocket_height = image_rocket.get_rect().size[1]

size_star_width = image_star.get_rect().size[0]
size_star_height = image_star.get_rect().size[1]

size_ball_width = image_ball.get_rect().size[0]
size_ball_height = image_ball.get_rect().size[1]

# 이미지의 x, y 좌표 구하기
x_pos_dog = size_bg_width / 2 - size_dog_width / 2
y_pos_dog = size_bg_height - size_dog_height

x_pos_rocket = size_bg_width / 2 - size_rocket_width / 2
y_pos_rocket = 0

x_pos_star = size_bg_width / 2 - size_star_width / 2
y_pos_star = size_bg_height - size_dog_height - size_star_height

x_pos_ball = size_bg_width / 2 - size_ball_width / 2
y_pos_ball = size_rocket_height


# while문 작동
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False

    # 이미지 그리기
    background.blit(image_bg, (0, 0))
    background.blit(image_dog, (x_pos_dog, y_pos_dog))
    background.blit(image_rocket, (x_pos_rocket, y_pos_rocket))
    background.blit(image_star, (x_pos_star, y_pos_star))
    background.blit(image_ball, (x_pos_ball, y_pos_ball))

    pygame.display.update()

pygame.quit()
