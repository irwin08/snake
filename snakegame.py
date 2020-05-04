import pygame
import snake as snek

class SnakeGame:

    board = []

    snake = None

    gameover = False

    def generate_board(self, size=20):
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(0)
            self.board.append(row)

        self.snake = snek.Snake(self.board)

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end="")
            print() #newline

    def move_snake(self, direction):
        self.gameover = self.snake.move(direction)
