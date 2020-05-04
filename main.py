import snakegame
import pygame
import sys


def draw_bordered_rect(screen, x, y, w, h, color):
    pygame.draw.rect(screen, BLACK, [x,y,w,h])
    pygame.draw.rect(screen, color, [x+4, y+4, w-8, h-8]) #probably should make this not hardcoded

def draw_grid(screen, my_game, block_size, margin, n, m):
    white = (200, 200,200)
    red = (200,0,0)
    green = (0,200,0)

    for row in range(n):
        for col in range(m):
            color = white
            if [row,col] in my_game.snake.coords_list:
                color = green
            pygame.draw.rect(screen, color, [(block_size + margin)*col + margin,
                                             (block_size + margin)*row + margin,
                                             block_size, block_size])

    
def main():

    window_width = 400
    window_height = 400

    block_size = 20

    n = window_height//block_size
    m = window_width//block_size

    margin = 5

    screen = pygame.display.set_mode((window_height, window_width))
    
    game = snakegame.SnakeGame()
    game.generate_board()

    
    direction = 0

    my_clock = pygame.time.Clock()

    while True:

        draw_grid(screen, game, block_size, margin, n, m)

        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = 1
                elif event.key == pygame.K_d:
                    direction = 2
                elif event.type == pygame.K_s:
                    direction = 3
                elif event.type == pygame.K_a:
                    direction = 4
                
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        game.move_snake(direction)

        pygame.display.update()

        my_clock.tick(10)



if __name__ == "__main__":
    main()
