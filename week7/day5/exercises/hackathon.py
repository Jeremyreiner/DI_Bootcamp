import numpy as np
import random
import time
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

dead_cell = 0
live_cell = 1

def begining_state(w, h):
    rand_board =  np.array(np.random.randint(0,1, (w*h)))
    start_state = rand_board.reshape(w, h)
    start_state[4][2] = live_cell
    start_state[4][3] = live_cell
    start_state[4][4] = live_cell
    start_state[5][1] = live_cell
    start_state[5][2] = live_cell
    start_state[5][3] = live_cell
    return start_state

def board_state_d(w, h):
    d_state = np.array(np.random.randint(0,1, (w*h)))
    dead_board = d_state.reshape(w, h)
    return dead_board

def random_board_state(w, h):
    board_state = board_state_d(w, h)
    for x in range(0, board_width(board_state)):
        for y in range(0, board_height(board_state)):
            random_number = random.random()
            if random_number > 0.5:
                cell_state = live_cell
            else:
                cell_state = dead_cell
            board_state[x][y] = cell_state
    return board_state

def board_width(board_state):
    return len(board_state)

def board_height(board_state):
    return len(board_state[0])

def prettyfy(board_state):
    display = {
        dead_cell: chr(9608),
        live_cell: chr(9618)
    }
    new_board= []
    for x in range(0, board_height(board_state)):
        line = ''
        for y in range(0, board_width(board_state)):
            line += display[board_state[x][y]] * 2
        new_board.append(line)
        nd_2d_arry = np.array('\n'.join(new_board))
    return nd_2d_arry


def next_c_value(cell_coords, board_state):
    width = board_width(board_state)
    height = board_height(board_state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    for neighbor_r in range((x - 1), (x + 1)+ 1):
        ''' 
        This loop checks the possibility that: 
        -current location is on or off the board
        -current location is current iteration
        -adds a count to live_cell neighbors 
        '''

        if neighbor_r < 0 or neighbor_r >= width: 
            continue

        for neighbor_c in range((y - 1), (y + 1) + 1):

            if neighbor_c < 0 or neighbor_c >= height: 
                continue

            elif neighbor_r == x and neighbor_c == y: 
                continue

            elif board_state[neighbor_r][neighbor_c] == live_cell:
                n_live_neighbors += 1
            

    if board_state[x][y] == live_cell:
        if n_live_neighbors <2:
            return dead_cell
        elif n_live_neighbors ==3 or n_live_neighbors ==2:
            return live_cell
        else:
            return dead_cell

    if board_state[x][y] == dead_cell:
        if n_live_neighbors == 3:
            return live_cell
        else:
            return dead_cell


def next_board_state(previous_state):
    width = board_width(previous_state)
    height = board_height(previous_state)
    next_state = board_state_d(width, height)
    '''
    next_board_state takes into count the rules
    of the actual game and returns the next iteration of the
    cell block either alive or dead. Recreating the 
    next iteration of the board
    '''
    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_c_value((x,y), previous_state)
    return next_state

def run_game(start_state):
    current_b = start_state
    print(prettyfy(current_b)) 
    print('\n')
    while True:
        next_b = next_board_state(current_b)
        print(prettyfy(next_b))
        print('\n')
        time.sleep(3)
        current_b = next_b

run_game(begining_state(20,20))





