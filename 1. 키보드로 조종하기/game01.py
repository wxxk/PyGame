import pygame

pygame.init()  # 처음에 적어주고 시작

# 게임의 가로 세로의 창의 크기를 지정하고 창을 만들어줌 (가로, 세로)
background = pygame.display.set_mode((480, 360))

# 창의 제목 - 없어도 잘 작동(선택사항)
pygame.display.set_caption("SONOL")

# 게임의 창을 계속 실행하기 위해 while문 필요
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 게임에서 발생한 이벤트가 QUIT면
            play = False  # play를 False로 만들어서 while문을 탈출
pygame.quit()  # pygame 종료
