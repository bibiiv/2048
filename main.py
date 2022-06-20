import random

DIRECTIONS = ["w", "a", "s", "d"]

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
    while True:
        direction = input("Please select direction for your move!")
        if direction.lower() in DIRECTIONS:
            return direction
        else:
            print("Not a valid input! Please select w, s, a or d!")


def shift_numbers_left(row):
    """Makes the left shift movement"""
    # Creates an empty list for the modified row
    shifted_row = []
    for element in row:
        # for every element in the row
        if element != 0:
            # gets the non-zero element
            shifted_row.append(element)
            # adds them to the list first
    while len(shifted_row) < 4:
        # while the lenght of the row is less than 4,
        # the row is filled with zeroes
        shifted_row.append(0)
    return shifted_row


def shift_numbers_right(row):
    """ Makes the right shift movement"""
    # creates an empty list for the modified row
    shifted_row = []
    # counts how many zeroes are present
    zeroes = row.count(0)
    # adds the zeroes to the empty list
    for _ in range(zeroes):
        shifted_row.append(0)
    # adds the non-zero numbers to the list
    for element in row:
        if element != 0:
            shifted_row.append(element)
    return shifted_row


def shift_numbers(direction):
    if direction == "w":
        pass
    if direction == "a":
        for i in range(len(board)):
            board[i] = shift_numbers_left(board[i])
    if direction == "s":
        pass
    if direction == "d":
        for i in range(len(board)):
            board[i] = shift_numbers_right(board[i])
    for row in board:
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
            specified_direction = specify_direction()
            if specified_direction:
                break
        shift_numbers(specified_direction)
        combine_numbers()
        shift_numbers(specified_direction)
        if check_if_board_full():
            if check_if_adjacent_num():
                continue
            else:
                break
        else:
            spawn_number()

    present_endgame()
