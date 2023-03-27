def get_cell_tuple(cell: str):
        # a b c d e f g h

        # 0 1 2 3 4 5 6 7

    return 8 - int(cell[1]), ord(cell[0]) - 97

def rotate_board(b):
    return [x[::-1] for x in b[::-1]]

def rotate_moves(moves):
    if moves == []:
        return []
    if moves == None:
        return None
    return [(7 - x[0], 7 - x[1]) for x in moves]