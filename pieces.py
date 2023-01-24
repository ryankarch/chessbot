class White(object):
    def __init__(self):
        self.in_check = False
        self.pos = {}
        self.moves = []

class Black(object):
    def __init__(self):
        self.in_check = False
        self.pos = {}
        self.moves = []

def load_positions(piece, board):
        
        for ri,row in enumerate(board):
            for ci,col in enumerate(row):
                if isinstance(piece, White):
                    if col.isupper():
                        try:
                            piece.pos[col].add((ri,ci))
                        except:
                            piece.pos[col] = set()
                            piece.pos[col].add((ri,ci))

                if isinstance(piece, Black):
                    if col.islower():
                        try:
                            piece.pos[col].add((ri,ci))
                        except:
                            piece.pos[col] = set()
                            piece.pos[col].add((ri,ci))