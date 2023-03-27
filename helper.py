from board import Board

def get_cell_tuple(cell: str):
        # a b c d e f g h

        # 0 1 2 3 4 5 6 7

    return 8 - int(cell[1]), ord(cell[0]) - 97

def process_move(move, b: Board):
    piece = ''
    startpos = ''
    action = ''
    endpos = ''
    if 'x' in move:
        action = "takes piece on"
        move = move.replace('x', '')
        if len(move == 3) and move[0] in "abcdefg":
            endpos = move[1:]
            piece = "p"
            startpos = b.find_piece(piece, endpos)
        elif len(move) == 3:
            endpos = move[1:]
            piece = move[0]
            startpos = b.find_piece(piece, endpos)
        else:
            endpos = move[2:]
            piece = move[0]
            startpos = b.find_piece(piece, endpos, move[1])
    else:
        action = "moves to"
        if len(move) == 2:
            endpos = move
            piece = "p"
            startpos = b.find_piece(piece, endpos)
        else:
            endpos = move[2:]
            piece = move[0]
            startpos = b.find_piece(piece, endpos, move[1])

    return f"{piece} on {startpos} {action} {endpos}"
            
    

def rotate_board(b):
    return [x[::-1] for x in b[::-1]]

def rotate_moves(moves):
    if moves == []:
        return []
    if moves == None:
        return None
    return [(7 - x[0], 7 - x[1]) for x in moves]