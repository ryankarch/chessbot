from helper import rotate_board


class Piece(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.moves = []
        self.color = color
        promoted = False


class Pawn(Piece):    
    def get_moves(self, board):
        pass
        

class Rook(Piece):    
    def get_moves(self, board):
        pass


class Bishop(Piece):    
    def get_moves(self, board):
        pass


class Knight(Piece):    
    def get_moves(self, board):
        pass


class Queen(Piece):    
    def get_moves(self, board):
        pass


class King(Piece):    
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