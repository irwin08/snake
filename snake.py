

class Snake:

    def __init__(self, board):
        self.board = board
    
    coords_list = [[0,0]]
    pos = [0,0]
    snake_len = 5

    # 0 = don't move; 1 = up; 2 = right; 3 = down; 4 = left;
    direction = 0
    
    def move(self, direction):

        error = False

        self.direction = direction
        
        new_pos = [0,0]
        coord_x = self.pos[0]
        coord_y = self.pos[1]

        if direction == 0:
            coord_x = coord_x
            coord_y = coord_y
        elif direction == 1:
            coord_x = coord_x - 1
            coord_y = coord_y
        elif direction == 2:
            coord_x = coord_x
            coord_y = coord_y + 1
        elif direction == 3:
            coord_x = coord_x + 1
            coord_y = coord_y
        elif direction == 4:
            coord_x = coord_x
            coord_y = coord_y - 1

        new_pos = [coord_x, coord_y]

        # check if in board
        if not ((new_pos[0] >= 0) and (new_pos[0] < len(self.board)) and (new_pos[1] >= 0) and (new_pos[1] < len(self.board[0]))):
            error = True
        
        if self.snake_len == len(self.coords_list):
            self.coords_list.pop(0)

            # check if eating self
            if new_pos in self.coords_list[:len(self.coords_list)-1] and not (self.direction == 0):
                error = True
            
            self.coords_list.append(new_pos)

        elif self.snake_len > len(self.coords_list):

            if new_pos in self.coords_list[:len(self.coords_list)-1] and not (self.direction == 0):
                error = True
            self.coords_list.append(new_pos)

        self.pos = new_pos
        
        return error
