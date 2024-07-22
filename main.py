import random
import pygame







class Snake():
    def __init__(self) -> None:
        self.colour = (0, 0, 0)
        self.player_pos = (0,0)
        self.dt = 0
        self.lenght = 1
        self.size = 20
        self.issquare = False
        self.index = None

    def get_issquare(self):
        return self.issquare
    
    def get_position(self):
        return self.player_pos


    def set_pos_snake(self,pos,index):
        self.player_pos = pos
        self.index = index


    def draw_snake(self,screen):
        rect = pygame.Rect(int(self.player_pos[0]), int(self.player_pos[1]), self.size,self.size)
        pygame.draw.rect(screen,self.colour,rect)

    def keys(self):
        return pygame.key.get_pressed()
    
    def key_up(self,board):
        temp1 = self.player_pos[0]
        temp2 = self.player_pos[1]
        self.player_pos = (temp1, temp2 - 41)
        # Retrieve the board once

        board.change_board("up",self.index)
        self.index[1] -= 1

    def key_down(self,board):
        temp1 = self.player_pos[0]
        temp2 = self.player_pos[1]
        self.player_pos = (temp1, temp2 + 41)
        board.change_board("down",self.index)

        self.index[1] += 1
  
  
    def key_left(self,board):
        temp1 = self.player_pos[0]
        temp2 = self.player_pos[1]
        self.player_pos = (temp1 - 41, temp2)
        board.change_board("left",self.index)
        self.index[0] -= 1


    def key_right(self,board):
        temp1 = self.player_pos[0]
        temp2 = self.player_pos[1]
        self.player_pos = (temp1 + 41, temp2)
        board.change_board("right",self.index)

        self.index[0] += 1

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
        self.issquare = True

    def create_square(self):
        rect = pygame.Rect(int(self.position[0]), int(self.position[1]), self.size,self.size)
        pygame.draw.rect(self.screen,self.colour_empty,rect)


    def get_issquare(self):
        return self.issquare

    def get_filled(self):
        return self.filled
    
    def set_filled(self,val):
        self.filled = val

    def get_position(self):
        return self.position


 
class Board():
    def __init__(self,screen):
        self.board = []
        self.height = 15
        self.width = 15
        self.screen = screen
        self.snake = Snake()
        self.create_grid()
        self.set_snake()

    
    def get_board(self):
        return self.board
    

    def change_board(self,direction,index):
        if direction == "up":
            # Use temporary variables to perform the swap
            temp = self.board[index[0]][index[1]]
            self.board[index[0]][index[1]] = self.board[index[0] - 1][index[1]]
            self.board[index[0] - 1][index[1]] = temp

        elif direction == "down":
            temp = self.board[index[0]][index[1]]
            self.board[index[0]][index[1]] = self.board[index[0] + 1][index[1]]
            self.board[index[0] + 1][index[1]] = temp

        elif direction == "left":
            temp = self.board[index[0]][index[1]]
            self.board[index[0]][index[1]] = self.board[index[0]][index[1] - 1]
            self.board[index[0]][index[1] - 1] = temp

        elif direction == "right":
            temp = self.board[index[0]][index[1]]
            self.board[index[0]][index[1]] = self.board[index[0]][index[1] + 1]
            self.board[index[0]][index[1] + 1] = temp



            

    def get_snake(self):
        return self.snake

    def set_snake(self):
        pos = self.board[3][3].get_position()
        self.snake.set_pos_snake(pos,[3,3])
        self.board[3][3] = self.snake

    def create_grid(self):
        row1= 0 
        col1= 0
        for row in range(self.height):
            lst= []
            for col in range(self.width):
                x = Square((row1,col1),self.screen)
                row1 += 41
                lst.append(x)
            row1 = 0
            self.board.append(lst)
            col1 += 41
        

    def display_grid(self):
        for row in self.board:
            for column in row:
                if column.get_issquare():
                    column.create_square()
                else:
                    column.draw_snake(self.screen)




class apple():
    def __init__(self) -> None:
        self.colour = (255, 0, 0)
        self.position = None
                

                
            

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

board = Board(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    board.display_grid()

    #print(board.get_board())
    ##board.get_snake().draw_snake(screen)

    keys = board.get_snake().keys()

    if keys[pygame.K_w]:
        board.get_snake().key_up(board)
    if keys[pygame.K_s]:
        board.get_snake().key_down(board)
    if keys[pygame.K_a]:
        board.get_snake().key_left(board)
    if keys[pygame.K_d]:
        board.get_snake().key_right(board)
        
    pygame.display.flip()

    board.get_snake().dt = clock.tick(10)

    print()




pygame.quit()

