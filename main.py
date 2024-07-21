import random
import pygame







class Snake():
    def __init__(self) -> None:
        self.colour = (0, 0, 0)
        self.player_pos = pygame.Vector2(1280 / 2, 720 / 2)
        self.dt = 0
        self.lenght = 1


    def draw_square(self,screen):
        rect = pygame.Rect(int(self.player_pos.x), int(self.player_pos.y), self.size,self.size)
        pygame.draw.rect(screen,self.colour,rect)

    def keys(self):
        return pygame.key.get_pressed()
    
    def key_up(self):
        self.player_pos.y -= 300 * self.dt

    def key_down(self):
        self.player_pos.y += 300 * self.dt

    def key_left(self):
        self.player_pos.x -= 300 * self.dt

    def key_right(self):
        self.player_pos.x += 300 * self.dt

    def __setattr__(self,  name, value) -> None:
        super().__setattr__(name,value)


class Square():
    def __init__(self,position,screen):
        self.filled = False
        self.colour_filled = (0,0,0)
        self.colour_empty = (0, 128, 0)
        self.position = position
        self.screen = screen
        self.size = 40
        self.create_square()

    def create_square(self):
        rect = pygame.Rect(int(self.position[0]), int(self.position[1]), self.size,self.size)
        pygame.draw.rect(self.screen,self.colour_empty,rect)

    def change_square_filled(self):
        rect = pygame.Rect(int(self.position[0]), int(self.position[1]), self.size,self.size)
        pygame.draw.rect(self.screen,self.colour_filled,rect)

    def change_square_empty(self):
        rect = pygame.Rect(int(self.position[0]), int(self.position[1]), self.size,self.size)
        pygame.draw.rect(self.screen,self.colour_empty,rect)
        

    def get_filled(self):
        return self.filled
    
    def set_filled(self,val):
        self.filled = val


 
class Board():
    def __init__(self,screen):
        self.board = []
        self.height = 15
        self.width = 15
        self.screen = screen

    def create_grid(self):
        row1= 0 
        col1= 0
        for row in range(self.height):
            lst= []
            for col in range(self.width):
                x = Square((row1,col1),self.screen)
                row1 += 41
            row1 = 0
            self.board.append(lst)
            col1 += 41
        

    def display_grid(self):
        for row in self.board:
            for column in row:
                column.create_square(self.screen)
                

                
            

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

snake = Snake()
board = Board(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False

    screen.fill("purple")

    board.create_grid()
    board.display_grid()

    #snake.draw_square(screen)

    keys = snake.keys()

    if keys[pygame.K_w]:
        snake.key_up()
    if keys[pygame.K_s]:
        snake.key_down()
    if keys[pygame.K_a]:
        snake.key_left()
    if keys[pygame.K_d]:
        snake.key_right()
        
    pygame.display.flip()

    snake.dt = clock.tick(60) / 1000


pygame.quit()

