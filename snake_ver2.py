import pygame
import sys
import random

class Fruit():
    def __init__(self):
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number -1)

        self.pos = pygame.math.Vector2(self.x,self.y)


    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.x * cell_size),int(self.y * cell_size),cell_size,cell_size)
        screen.blit(apple_image,fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)



class Snake():
    def __init__(self):
        self.body = [pygame.math.Vector2(7,10),pygame.math.Vector2(6,10),pygame.math.Vector2(5,10)]
        self.direction = pygame.math.Vector2(1,0)


        self.head_up = pygame.image.load("Snake-game\sprites\head_up.png")
        self.head_down = pygame.image.load("Snake-game\sprites\head_down.png")
        self.head_left = pygame.image.load("Snake-game\sprites\head_left.png")
        self.head_right = pygame.image.load("Snake-game\sprites\head_right.png")
        
        self.tail_up = pygame.image.load(r"Snake-game\sprites\tail_up.png")
        self.tail_down = pygame.image.load(r"Snake-game\sprites\tail_down.png")
        self.tail_left = pygame.image.load(r"Snake-game\sprites\tail_left.png")
        self.tail_right = pygame.image.load(r"Snake-game\sprites\tail_right.png")

        self.body_vertical = pygame.image.load(r"Snake-game\sprites\body_vertical.png")
        self.body_horizontal = pygame.image.load(r"Snake-game\sprites\body_horizontal.png")

        self.body_bl = pygame.image.load(r"Snake-game\sprites\body_bottomleft.png")
        self.body_br = pygame.image.load(r"Snake-game\sprites\body_bottomright.png")
        self.body_tl = pygame.image.load(r"Snake-game\sprites\body_topleft.png")
        self.body_tr = pygame.image.load(r"Snake-game\sprites\body_topright.png")



    def set_direction(self,val):
        self.direction = val
        


    def draw_snake(self):
        for index,val in enumerate(self.body):


            if index == 0:
                if self.direction.x == 1:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.head_right,rect)
                elif self.direction.x == -1:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.head_left,rect)
                elif self.direction.y == 1:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.head_down,rect)
                else:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.head_up,rect)
            
            elif index == (len(self.body) -1):
                vector = self.body[index] - self.body[index -1]
                if vector.x ==1 :
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.tail_right,rect)
                elif vector.x == -1:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.tail_left,rect)
                elif vector.y == 1:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.tail_down,rect)
                else:
                    rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                    screen.blit(self.tail_up,rect) 

            else:
                previous_block = self.body[index + 1] - self.body[index]
                next_block = self.body[index -1] - self.body[index]
                if previous_block.x == next_block.x:
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_vertical,rect)
                elif previous_block.y == next_block.y:
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_horizontal,rect)
                else:
                    if (previous_block.y == 1 and next_block.x == 1) or (previous_block.x == 1 and next_block.y == 1):
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_br,rect)
                    elif (previous_block.y == -1 and next_block.x == 1) or (previous_block.x == 1 and next_block.y == -1):
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_tr,rect)    
                    elif (previous_block.y == 1 and next_block.x == -1) or (previous_block.x == -1 and next_block.y == 1):
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_bl,rect)  
                    elif (previous_block.y == -1 and next_block.x == -1) or (previous_block.x == -1 and next_block.y == -1):
                        rect = pygame.Rect(int(self.body[index].x * cell_size),int(self.body[index].y * cell_size),cell_size,cell_size)
                        screen.blit(self.body_tl,rect)  



    #    for block in self.body:
    #        body_rect = pygame.Rect(int(block.x * cell_size),int(block.y *cell_size),cell_size,cell_size)
    #        pygame.draw.rect(screen,(0,0,0),body_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy
 



class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def snake_eat_fruit(self):
        snake_head = self.snake.body[0]
        snake_body = self.snake.body[1]
        fruit_vector = self.fruit.pos
        if snake_head.x == fruit_vector.x and snake_head.y == fruit_vector.y:
            self.fruit = None
            self.fruit = Fruit()
            self.snake.body.insert(1,pygame.math.Vector2(snake_body))



    def snake_eat_itself(self):
        print(self.snake.body)
        snake_body = self.snake.body
        snake_head = snake_body[0]
        count = 0
        for i in self.snake.body:
            if i == snake_head:
                count += 1
        if count > 1:
            self.game_over()
        

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cell_number:
            self.game_over()
        

                
            
    def draw_grass(self):
        grass_colour = (167,209,61)
        count =0
        while count != 21:
            for i in range(cell_number):
                grass_rect = pygame.Rect(int(i *cell_size), int(count *cell_size),cell_size,cell_size)
                if count % 2 == 0:
                    if i % 2 != 0:
                        pygame.draw.rect(screen,grass_colour,grass_rect)
                else:
                    if i % 2 == 0:
                        pygame.draw.rect(screen,grass_colour,grass_rect)
                if i == cell_number -1:
                    count += 1
        
            
        



    def update(self):
        self.snake.move_snake()

    def draw(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()



pygame.init()






cell_size = 40
cell_number =20


screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))
clock = pygame.time.Clock()


#test_surface = pygame.Surface((100,200))

main_game = Main()


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

apple_image = pygame.image.load("Snake-game\sprites\DS DSi - Dragon Quest 5 The Hand of the Heavenly Bride - 040 - Rotten Apple.png")

while True:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()
            main_game.snake_eat_fruit()
            main_game.snake_eat_itself()
            main_game.check_fail()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and main_game.snake.direction.y != 1:
                main_game.snake.set_direction(pygame.math.Vector2(0,-1))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and main_game.snake.direction.y != -1:
                main_game.snake.set_direction(pygame.math.Vector2(0,+1))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and main_game.snake.direction.x != -1:
                main_game.snake.set_direction(pygame.math.Vector2(1,0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and main_game.snake.direction.x != 1:
                main_game.snake.set_direction(pygame.math.Vector2(-1,0))


    screen.fill((175,215,70))
   # screen.blit(test_surface,(200,250))
    #test_surface.fill((255,0,0))
    main_game.draw()
    pygame.display.update()
    clock.tick(60)


    























