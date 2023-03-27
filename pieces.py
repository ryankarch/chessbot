from helper import rotate_board


class Piece(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.moves = []
        self.color = color
        promoted = False

    def clean_moves(self):
        self.moves = [pos for pos in self.moves if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7]

class Pawn(Piece):    
    def get_moves(self, board):
        move_dir = 1 if self.color == 'w' else -1
        i, j = self.pos
        if isinstance(board[i-(1*move_dir)][j], Blank):
            self.moves.append((i-(1*move_dir), j))
            if isinstance(board[i-(2*move_dir)][j], Blank) and (i == 6 and self.color == 'w' or i == 1 and self.color == 'b'):
                self.moves.append((i-(2*move_dir), j))
        if not isinstance(board[i-(1*move_dir)][j-1], Blank) and board[i-(1*move_dir)][j-1].color != self.color and not isinstance(board[i-(1*move_dir)][j-1], King):
            self.moves.append((i-(1*move_dir), j-1))
        if not isinstance(board[i-(1*move_dir)][j+1], Blank) and board[i-(1*move_dir)][j+1].color != self.color and not isinstance(board[i-(1*move_dir)][j+1], King):
            self.moves.append((i-(1*move_dir), j+1))
        
        self.clean_moves()
        

class Rook(Piece):    
    def get_moves(self, board):
        i, j = self.pos
        for i_ in range(i+1, 8):
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
            elif board[i_][j].color != self.color and not isinstance(board[i_][j], King):
                self.moves.append((i_, j))
                break
            else:
                break
        for i_ in range(i-1, 0, -1):
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
            elif board[i_][j].color != self.color and not isinstance(board[i_][j], King):
                self.moves.append((i_, j))
                break
            else:
                break
        for j_ in range(j+1, 8):
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
            elif board[i][j_].color != self.color and not isinstance(board[i][j_], King):
                self.moves.append((i, j_))
                break
            else:
                break
        for j_ in range(j-1, 0, -1):
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
            elif board[i][j_].color != self.color and not isinstance(board[i][j_], King):
                self.moves.append((i, j_))
                break
            else:
                break


class Bishop(Piece):    
    def get_moves(self, board):
        i, j = self.pos
        for inc in range(1, min(8-i, 8-j)):
            if isinstance(board[i+inc][j+inc], Blank):
                self.moves.append((i+inc, j+inc))
            elif board[i+inc][j+inc].color != self.color and not isinstance(board[i+inc][j+inc], King):
                self.moves.append((i+inc, j+inc))
                break
            else:
                break
        for inc in range(1, min(8-i, j)):
            if isinstance(board[i+inc][j-inc], Blank):
                self.moves.append((i+inc, j-inc))
            elif board[i+inc][j-inc].color != self.color and not isinstance(board[i+inc][j-inc], King):
                self.moves.append((i+inc, j-inc))
                break
            else:
                break
        for inc in range(1, min(i, 8-j)):
            if isinstance(board[i-inc][j+inc], Blank):
                self.moves.append((i-inc, j+inc))
            elif board[i-inc][j+inc].color != self.color and not isinstance(board[i-inc][j+inc], King):
                self.moves.append((i-inc, j+inc))
                break
            else:
                break
        for inc in range(1, min(i, j)):
            if isinstance(board[i-inc][j-inc], Blank):
                self.moves.append((i-inc, j-inc))
            elif board[i-inc][j-inc].color != self.color and not isinstance(board[i-inc][j-inc], King):
                self.moves.append((i-inc, j-inc))
                break
            else:
                break


class Knight(Piece):    
    def get_moves(self, board):
        pass


class Queen(Piece):    
    def get_moves(self, board):
        pass


class King(Piece):    
    def get_moves(self, board):
        pass


class Blank(Piece):
    def __init__(self, pos):
        self.pos = pos
        self.moves = []
        self.color = None
    
    def get_moves(self, board):
        pass


class Player(object):
    def __init__(self, color):
        self.__piece_conversion = {'p':Pawn, 'r':Rook, 'n':Knight, 'b':Bishop, 'q':Queen, 'k':King}
        self.in_check = False
        self.color = color
        self.pieces = []


    def create_piece(self, piece: str, pos):
        piece = piece.lower()
        p = self.__piece_conversion[piece](self.color, pos)
        self.pieces.append(p)
        return p


    def remove_piece(self, piece: Piece):
        self.pieces.remove(piece)


    def load_positions(self):
            pos = []
            for piece in self.pieces:
                pos.append(piece.pos)