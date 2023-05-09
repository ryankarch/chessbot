from Engine import Engine, Pieces


def get_cell_row_or_col(cell: str):
    if cell.isnumeric():
        return 8 - int(cell[0]), -1
    else:
        return -1, ord(cell[0]) - 97

def get_cell_tuple(cell: str):
        # a b c d e f g h

        # 0 1 2 3 4 5 6 7

    return 8 - int(cell[1]), ord(cell[0]) - 97

def check_valid(move):
    if move == "resign": 
        return True
    if any(x not in "abcdefgh12345678x+QKNRB" for x in move):
        return False
    if len(move) > 2 and not move[0].isupper() and 'x' not in move:
        return False
    return True

def process_move(move, e: Engine):
    piece = ''
    startpos = ''
    endpos = ''
    if move.startswith("x"):
        return None
    if 'x' in move:
        move = move.replace('x', '')
        if len(move) == 3 and move[0] in "abcdefgh":
            endpos = get_cell_tuple(move[1:])
            piece = "p"
            startpos = e.find_piece(piece, endpos)
        elif len(move) == 3:
            endpos = get_cell_tuple(move[1:])
            piece = move[0].lower()
            startpos = e.find_piece(piece, endpos)
        else:
            endpos = get_cell_tuple(move[2:])
            piece = move[0].lower()
            startpos = e.find_piece(piece, endpos, get_cell_row_or_col(move[1]))
        if isinstance(e.board_piece[endpos[0]][endpos[1]], Pieces.Blank) and not (isinstance(e.board_piece[startpos[0]][endpos[1]], Pieces.Pawn) and e.board_piece[startpos[0]][endpos[1]].en_passant):
            startpos = None
    else:
        if len(move) == 2:
            endpos = get_cell_tuple(move)
            piece = "p"
            startpos = e.find_piece(piece, endpos)
        elif len(move) == 3:
            endpos = get_cell_tuple(move[1:])
            piece = move[0].lower()
            startpos = e.find_piece(piece, endpos)
        else:
            endpos = get_cell_tuple(move[2:])
            piece = move[0].lower()
            startpos = e.find_piece(piece, endpos, get_cell_row_or_col(move[1]))
    if startpos == None:
        return ""
    return (startpos, endpos)
            
    

def rotate_board(b):
    return [x[::-1] for x in b[::-1]]

def rotate_moves(moves):
    if moves == []:
        return []
    if moves == None:
        return None
    return [(7 - x[0], 7 - x[1]) for x in moves]