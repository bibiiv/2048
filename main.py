import random

# Generating the storage for the 4x4 board
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def draw_board():
    """
    Drawing the board to make it visible to the player:
    """
    for row in board:
        # Adding border to each element
        printable_row = "| "
        # Concatenating the element with its border
        for element in row:
            printable_row += str(element)
            printable_row += " | "
        print(printable_row)


def spawn_number():
    """
    Creating the sequence that spawns numbers for each turn
    """
    # Creating a list of the empty elements on the board
    empty_elements = []
    # For each row
    for i in range(len(board)):
        # For each column
        for j in range(len(board[0])):
            # If the value of the element == 0
            if board[i][j] == 0:
                # they are added to the empty elements list
                empty_elements.append([i, j])
    # Out of this empty elements list, a pair is chosen
    random_row, random_col = random.choice(empty_elements)
    # Generate random number - 2 or 4
    spawned_number = random.choices([2, 4], [9, 1])[0]
    # Set the random number to the random empty spot
    board[random_row][random_col] = spawned_number


def specify_direction():
    return True


def shift_numbers():
    pass


def combine_numbers():
    pass


def check_if_board_full():
    return False


def check_if_adjacent_num():
    return True


def present_endgame():
    pass


if __name__ == '__main__':
    spawn_number()
    spawn_number()
    while True:
        draw_board()
        while True:
            direction = specify_direction()
            if direction:
                break
        shift_numbers()
        combine_numbers()
        shift_numbers()
        if check_if_board_full():
            if check_if_adjacent_num():
                continue
            else:
                break
        else:
            spawn_number()

    present_endgame()
