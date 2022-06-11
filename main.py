def draw_board():
    pass


def spawn_number():
    pass


def specify_direction():
    return True


def shift_numbers():
    pass


def combine_numbers():
    pass


def check_if_board_full():
    return True


def check_if_adjacent_num():
    return True


def present_endgame():
    pass


if __name__ == '__main__':
    draw_board()
    spawn_number()
    spawn_number()
    while True:
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
