import pygame
import random
####################################################################################################################################
# 기본 초기화 (반드시 해야하는 것들)

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("똥 피하기") # 게임 이름 삽입

#FPS
clock = pygame.time.Clock()
####################################################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트 등)
background = pygame.image.load("C:/Users/pgh54/Desktop/CODE practice/PYTHON/make project/pygame_basic/background.png")


enemy = pygame.image.load("C:/Users/pgh54/Desktop/CODE practice/PYTHON/make project/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_to_y = 0.5

character = pygame.image.load("C:/Users/pgh54/Desktop/CODE practice/PYTHON/make project/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2 
character_y_pos = screen_height - character_height
character_to_x = 0
character_to_y = 0
character_speed = 0.06


# 폰트 정의
game_font = pygame.font.Font ( None, 40) #폰트 객체를 생성 (폰트, 크기)

#시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아들임



running =True 
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                character_to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭어를 아랫쪽으로
                character_to_y += character_speed

    if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += dt * character_to_x

    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos> screen_width - character_width:
        character_x_pos = screen_width - character_width


    enemy_y_pos += dt * enemy_to_y
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
        enemy_to_y += 0.01 


    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos





    # 4. 충돌 처리
    if character_rect.colliderect(enemy_rect): #colliderect는 충돌 검사 함수
        print("충돌했습니다." )
        running = False
    



    # 5. 화면에 그리기

    screen.blit(background, (0, 0)) #배경 그리기 / 대상과 좌표값을 가져야함
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 / 대상과 좌표값을 가져야함
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 1000으로 나누어 초 단위로 표시/ 기존에 ms 단위

    timer = game_font.render(str(int(elapsed_time)), True, (255,255,255))  #render 정보 / 순서대로 (출력할 글자, True, 색상)
    screen.blit(timer,(10,10))

    

    pygame.display.update() # 게임 화면을 다시 그리기
    
# 종료 직전 잠시 대기
pygame.time.delay(2000) #2초 정도 대기
    

#pygame 종료
pygame.quit()