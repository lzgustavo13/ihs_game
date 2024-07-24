import pygame, sys, random
from pygame.math import Vector2
import os
from fcntl import ioctl

HEX_0 = 0xC0
HEX_1 = 0xF9
HEX_2 = 0xA4
HEX_3 = 0xB0
HEX_4 = 0x99
HEX_5 = 0x92
HEX_6 = 0x82
HEX_7 = 0xF8
HEX_8 = 0x80
HEX_9 = 0x90
HEX_A = 0x88
HEX_B = 0x83
HEX_C = 0xC6
HEX_D = 0xA1
HEX_E = 0x86
HEX_F = 0x8E

PB = 24930
SW = 24929
DIS_L = 24931
DIS_R = 24932
LED_R = 24933
LED_G = 24934

class IO:
    def __init__(self) -> None:
        self.fd = os.open('/dev/mydev', os.O_RDWR)
        self.dev = SW

    def __del__(self):
        os.close(self.fd)

    def get_SW(self, pos):
        ioctl(self.fd, SW)
        sw_pos = (0x1<<pos)
        os.read(self.fd, 4)
        ret_sw = os.read(self.fd, 4)
        return 1 if (sw_pos & int.from_bytes(ret_sw, 'little')) > 0 else 0
    
    def get_PB(self, pos):
        ioctl(self.fd, PB)
        pb_pos = (1<<pos)
        os.read(self.fd, 4)
        ret_pb = os.read(self.fd, 4)
        data_ret = 1 if (pb_pos & int.from_bytes(ret_pb, 'little')) > 0 else 0
        return data_ret

    def put_LD(self, val):
        ioctl(self.fd, LED_R)
        os.write(self.fd, val.to_bytes(4, 'little'))

    def put_ar_LD(self, list_pos):
        ioctl(self.fd, LED_R)
        data = 0
        for num in list_pos:
            data = (1 << num) | data
        os.write(self.fd, data.to_bytes(4, 'little'))

    def put_DP(self, pos, ar_num):
        if pos == 0:
            ioctl(self.fd, DIS_R)
        else:
            ioctl(self.fd, DIS_L)

        data = 0
        for num in ar_num:
            data = self.__aux_DP(data, num, 8)
        os.write(self.fd, data.to_bytes(4, 'little'))

    def __aux_DP(self, data, num, ind):
        data = data << ind
        if num == '0':
            data = data | HEX_0
        elif num == '1':
            data = data | HEX_1
        elif num == '2':
            data = data | HEX_2
        elif num == '3':
            data = data | HEX_3
        elif num == '4':
            data = data | HEX_4
        elif num == '5':
            data = data | HEX_5
        elif num == '6':
            data = data | HEX_6
        elif num == '7':
            data = data | HEX_7
        elif num == '8':
            data = data | HEX_8
        elif num == '9':
            data = data | HEX_9
        elif num == 'A':
            data = data | HEX_A
        elif num == 'B':
            data = data | HEX_B
        elif num == 'C':
            data = data | HEX_C
        elif num == 'D':
            data = data | HEX_D
        elif num == 'E':
            data = data | HEX_E
        elif num == 'F':
            data = data | HEX_F
        return data

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()
io = IO()  # Instanciação da classe IO

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()

    # Verificação dos botões físicos
    if io.get_PB(3) == 0:  # Botão 3 - Mover para cima
        if main_game.snake.direction.y != 1:
            main_game.snake.direction = Vector2(0, -1)
    if io.get_PB(0) == 0:  # Botão 0 - Mover para a direita
        if main_game.snake.direction.x != -1:
            main_game.snake.direction = Vector2(1, 0)
    if io.get_PB(2) == 0:  # Botão 2 - Mover para baixo
        if main_game.snake.direction.y != -1:
            main_game.snake.direction = Vector2(0, 1)
    if io.get_PB(1) == 0:  # Botão 1 - Mover para a esquerda
        if main_game.snake.direction.x != 1:
            main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(30)
