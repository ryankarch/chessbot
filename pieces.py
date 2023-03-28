class Piece(object):
    def __init__(self, color, pos, abbrev):
        self.pos = pos
        self.moves = []
        self.color = color
        self.abbrev = abbrev
        promoted = False

    def move_straight(self, board, limit=8):
        i, j = self.pos
        count = 0
        for i_ in range(i+1, 8):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                break
            else:
                break
            count += 1
        count = 0
        for i_ in range(i-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                break
            else:
                break
            count += 1
        count = 0
        for j_ in range(j+1, 8):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                break
            else:
                break
            count += 1
        count = 0
        for j_ in range(j-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                break
            else:
                break
            count += 1

    def move_diagonal(self, board, limit=8):
        i, j = self.pos
        count = 0
        for inc in range(1, min(8-i, 8-j)):
            if count == limit:
                break
            if isinstance(board[i+inc][j+inc], Blank):
                self.moves.append((i+inc, j+inc))
            elif board[i+inc][j+inc].color != self.color:
                self.moves.append((i+inc, j+inc))
                break
            else:
                break
            count += 1
        count = 0
        for inc in range(1, min(8-i, j+1)):
            if count == limit:
                break
            if isinstance(board[i+inc][j-inc], Blank):
                self.moves.append((i+inc, j-inc))
            elif board[i+inc][j-inc].color != self.color:
                self.moves.append((i+inc, j-inc))
                break
            else:
                break
            count += 1
        count = 0
        for inc in range(1, min(i+1, 8-j)):
            if count == limit:
                break
            if isinstance(board[i-inc][j+inc], Blank):
                self.moves.append((i-inc, j+inc))
            elif board[i-inc][j+inc].color != self.color:
                self.moves.append((i-inc, j+inc))
                break
            else:
                break
            count += 1
        count = 0
        for inc in range(1, min(i+1, j+1)):
            if count == limit:
                break
            if isinstance(board[i-inc][j-inc], Blank):
                self.moves.append((i-inc, j-inc))
            elif board[i-inc][j-inc].color != self.color:
                self.moves.append((i-inc, j-inc))
                break
            else:
                break
            count += 1
    
    def clean_moves(self):
        self.moves = [pos for pos in self.moves if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7]
    
    def check_for_checks(self, board):
        for move in self.moves:
            if isinstance(board[move[0]][move[1]], King):
                self.moves.remove(move)
                return True
        return False
    

class Pawn(Piece):
    def get_moves(self, board):
        move_dir = 1 if self.color == 'w' else -1
        i, j = self.pos
        if isinstance(board[i-(1*move_dir)][j], Blank):
            self.moves.append((i-(1*move_dir), j))
            if isinstance(board[i-(2*move_dir)][j], Blank) and (i == 6 and self.color == 'w' or i == 1 and self.color == 'b'):
                self.moves.append((i-(2*move_dir), j))
        try:
            if not isinstance(board[i-(1*move_dir)][j-1], Blank) and board[i-(1*move_dir)][j-1].color != self.color:
                self.moves.append((i-(1*move_dir), j-1))
        except:
            pass
        try:
            if not isinstance(board[i-(1*move_dir)][j+1], Blank) and board[i-(1*move_dir)][j+1].color != self.color:
                self.moves.append((i-(1*move_dir), j+1))
        except:
            pass
        
        self.clean_moves()
        return self.moves
        

class Rook(Piece):
    def get_moves(self, board):
        self.move_straight(board)
        return self.moves


class Bishop(Piece):
    def get_moves(self, board):
        self.move_diagonal(board)
        return self.moves


class Knight(Piece):
    def get_moves(self, board):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) + abs(j) == 3:
                    try:
                        if isinstance(board[self.pos[0]+i][self.pos[1]+j], Blank) or board[self.pos[0]+i][self.pos[1]+j].color != self.color:
                            self.moves.append((self.pos[0]+i, self.pos[1]+j))
                    except:
                        pass
        self.clean_moves()
        return self.moves


class Queen(Piece):
    def get_moves(self, board):
        self.move_straight(board)
        self.move_diagonal(board)
        return self.moves


class King(Piece):
    def get_moves(self, board):
        self.move_straight(board, limit=1)
        self.move_diagonal(board, limit=1)
        return self.moves


class Blank(Piece):
    def __init__(self, pos):
        self.pos = pos
        self.moves = []
        self.color = None
    
    def get_moves(self, _):
        return []


class Player(object):
    def __init__(self, color):
        self.__piece_conversion = {'p':Pawn, 'r':Rook, 'n':Knight, 'b':Bishop, 'q':Queen, 'k':King}
        self.in_check = False
        self.color = color
        self.pieces = {'p':[], 'r':[], 'n':[], 'b':[], 'q':[], 'k':[]}
        self.id = -1

    def setid(self, id):
        self.id = id


    def create_piece(self, piece: str, pos):
        piece = piece.lower()
        p = self.__piece_conversion[piece](self.color, pos, piece)
        self.pieces[piece].append(p)
        return p


    def remove_piece(self, piece: Piece):
        self.pieces[piece.abbrev].remove(piece)


    def get_moves(self, type_=''):
        if type_:
            return {x : x.moves for x in self.pieces[type_]}
        else:
            return {y: {x : x.moves for x in self.pieces[y]} for y in self.pieces}


    def load_positions(self):
        pos = []
        for piece_name in self.pieces:
            for piece in self.pieces[piece_name]:
                pos.append(piece.pos)
        return pos

    def calculate_moves(self, board):
        for piece_name in self.pieces:
            for piece in self.pieces[piece_name]:
                piece.get_moves(board)