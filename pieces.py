class Piece(object):
    def __init__(self, color, pos, abbrev):
        self.pos = pos
        self.moves = []
        self.protecting = []
        self.pins = []
        self.color = color
        self.abbrev = abbrev
        self.promoted = False

    def move_straight(self, board, limit=8):
        i, j = self.pos
        count = 0
        pin = False
        pin_set = [self.pos]
        for i_ in range(i+1, 8):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
                pin_set.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                pin_set.append((i_, j))
                for i__ in range(i_+1, 8):
                    if isinstance(board[i__][j], King) and board[i__][j].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i__][j], Piece) and not isinstance(board[i__][j], Blank):
                        break
                    pin_set.append((i__, j))
                break
            elif board[i_][j].color == self.color:
                self.protecting.append((i_, j))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for i_ in range(i-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
                pin_set.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                pin_set.append((i_, j))
                for i__ in range(i_-1, -1, -1):
                    if isinstance(board[i__][j], King) and board[i__][j].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i__][j], Piece) and not isinstance(board[i__][j], Blank):
                        break
                    pin_set.append((i__, j))
                break
            elif board[i_][j].color == self.color:
                self.protecting.append((i_, j))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for j_ in range(j+1, 8):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
                pin_set.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                pin_set.append((i, j_))
                for j__ in range(j_+1, 8):
                    if isinstance(board[i][j__], King) and board[i][j__].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i][j__], Piece) and not isinstance(board[i][j__], Blank):
                        break
                    pin_set.append((i, j__))
                break
            elif board[i][j_].color == self.color:
                self.protecting.append((i, j_))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for j_ in range(j-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
                pin_set.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                pin_set.append((i, j_))
                for j__ in range(j_-1, -1, -1):
                    if isinstance(board[i][j__], King) and board[i][j__].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i][j__], Piece) and not isinstance(board[i][j__], Blank):
                        break
                    pin_set.append((i, j__))
                break
            elif board[i][j_].color == self.color:
                self.protecting.append((i, j_))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)

    def move_diagonal(self, board, limit=8):
        i, j = self.pos
        pin = False
        pin_set = [self.pos]
        count = 0
        for inc in range(1, min(8-i, 8-j)):
            if count == limit:
                break
            if isinstance(board[i+inc][j+inc], Blank):
                self.moves.append((i+inc, j+inc))
                pin_set.append((i+inc, j+inc))
            elif board[i+inc][j+inc].color != self.color:
                self.moves.append((i+inc, j+inc))
                pin_set.append((i+inc, j+inc))
                for inc_ in range(inc + 1, min(8-i, 8-j)):
                    if isinstance(board[i+inc_][j+inc_], King) and board[i+inc_][j+inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i+inc][j+inc], Piece) and not isinstance(board[i+inc][j+inc], Blank):
                        break
                    pin_set.append((i+inc_, j+inc_))
                break
            elif board[i+inc][j+inc].color == self.color:
                self.protecting.append((i+inc, j+inc))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for inc in range(1, min(8-i, j+1)):
            if count == limit:
                break
            if isinstance(board[i+inc][j-inc], Blank):
                self.moves.append((i+inc, j-inc))
                pin_set.append((i+inc, j-inc))
            elif board[i+inc][j-inc].color != self.color:
                self.moves.append((i+inc, j-inc))
                pin_set.append((i+inc, j-inc))
                for inc_ in range(inc + 1, min(8-i, j+1)):
                    if isinstance(board[i+inc_][j-inc_], King) and board[i+inc_][j-inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i+inc][j-inc], Piece) and not isinstance(board[i+inc][j-inc], Blank):
                        break
                    pin_set.append((i+inc_, j-inc_))
                break
            elif board[i+inc][j-inc].color == self.color:
                self.protecting.append((i+inc, j-inc))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for inc in range(1, min(i+1, 8-j)):
            if count == limit:
                break
            if isinstance(board[i-inc][j+inc], Blank):
                self.moves.append((i-inc, j+inc))
                pin_set.append((i-inc, j+inc))
            elif board[i-inc][j+inc].color != self.color:
                self.moves.append((i-inc, j+inc))
                pin_set.append((i-inc, j+inc))
                for inc_ in range(inc + 1, min(i+1, 8-j)):
                    if isinstance(board[i-inc_][j+inc_], King) and board[i+inc_][j+inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i-inc][j+inc], Piece) and not isinstance(board[i-inc][j+inc], Blank):
                        break
                    pin_set.append((i-inc_, j+inc_))
                break
            elif board[i-inc][j+inc].color == self.color:
                self.protecting.append((i-inc, j+inc))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
        pin = False
        pin_set = [self.pos]
        count = 0
        for inc in range(1, min(i+1, j+1)):
            if count == limit:
                break
            if isinstance(board[i-inc][j-inc], Blank):
                self.moves.append((i-inc, j-inc))
                pin_set.append((i-inc, j-inc))
            elif board[i-inc][j-inc].color != self.color:
                self.moves.append((i-inc, j-inc))
                pin_set.append((i-inc, j-inc))
                for inc_ in range(inc + 1, min(i+1, j+1)):
                    if isinstance(board[i-inc_][j-inc_], King) and board[i+inc_][j+inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i-inc][j-inc], Piece) and not isinstance(board[i-inc][j-inc], Blank):
                        break
                    pin_set.append((i-inc_, j-inc_))
                break
            elif board[i-inc][j-inc].color == self.color:
                self.protecting.append((i-inc, j-inc))
                break
            else:
                break
            count += 1
        if pin:
            self.pins.append(pin_set)
    
    def clean_moves(self):
        self.moves = [pos for pos in self.moves if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7]
    
    def update_pos(self, pos):
        self.pos = pos

    def return_moves(self):
        return self.moves

    def check_for_checks(self, board):
        for move in self.moves:
            if isinstance(board[move[0]][move[1]], King):
                self.moves.remove(move)
                return True
        return False
    

class Pawn(Piece):
    def get_moves(self, board, pins=[]):
        self.protecting = []
        move_dir = 1 if self.color == 'w' else -1
        i, j = self.pos
        if isinstance(board[i-(1*move_dir)][j], Blank):
            self.moves.append((i-(1*move_dir), j))
            if isinstance(board[i-(2*move_dir)][j], Blank) and (i == 6 and self.color == 'w' or i == 1 and self.color == 'b'):
                self.moves.append((i-(2*move_dir), j))
        try:
            if not isinstance(board[i-(1*move_dir)][j-1], Blank):
                if board[i-(1*move_dir)][j-1].color != self.color:
                    self.moves.append((i-(1*move_dir), j-1))
                else:
                    self.protecting.append((i-(1*move_dir), j-1))
        except:
            pass
        try:
            if not isinstance(board[i-(1*move_dir)][j+1], Blank):
                if board[i-(1*move_dir)][j+1].color != self.color:
                    self.moves.append((i-(1*move_dir), j+1))
                else:
                    self.protecting.append((i-(1*move_dir), j+1))
        except:
            pass
        
        self.clean_moves()
        for pin_set in pins:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks(board)
        

class Rook(Piece):
    def get_moves(self, board, pins=[]):
        self.protecting = []
        self.pins = []
        self.move_straight(board)
        for pin_set in pins:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks(board)


class Bishop(Piece):
    def get_moves(self, board, pins=[]):
        self.protecting = []
        self.pins = []
        self.move_diagonal(board)
        for pin_set in pins:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks(board)


class Knight(Piece):
    def get_moves(self, board, pins=[]):
        self.protecting = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) + abs(j) == 3:
                    try:
                        if isinstance(board[self.pos[0]+i][self.pos[1]+j], Blank):
                            self.moves.append((self.pos[0]+i, self.pos[1]+j))
                        else:
                            if board[self.pos[0]+i][self.pos[1]+j].color == self.color:
                                self.protecting.append((self.pos[0]+i, self.pos[1]+j))
                    except:
                        pass
        self.clean_moves()
        for pin_set in pins:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks(board)


class Queen(Piece):
    def get_moves(self, board, pins=[]):
        self.protecting = []
        self.pins = []
        self.move_straight(board)
        self.move_diagonal(board)
        for pin_set in pins:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks(board)


class King(Piece):
    def get_moves(self, board, unsafe={}):
        self.protecting = []
        self.move_straight(board, limit=1)
        self.move_diagonal(board, limit=1)
        self.moves = list(set(self.moves) - set(unsafe))
        return self.check_for_checks(board)


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
        try:
            self.pieces[piece.abbrev].remove(piece)
        except:
            pass

    def get_moves(self, type_=''):
        if type_:
            return {x : x.return_moves() for x in self.pieces[type_]}
        else:
            return {y: {x : x.return_moves() for x in self.pieces[y]} for y in self.pieces}

    def get_protected(self):
        pos = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pos += x.protecting
        return pos
    
    def get_pinned(self):
        pins = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pins += x.pins
        return pins
    
    def get_possible(self):
        pos = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pos += x.moves
        return pos

    def get_unsafe(self):
        return self.get_protected() + self.get_possible()

    def load_positions(self):
        pos = []
        for piece_name in self.pieces:
            for piece in self.pieces[piece_name]:
                pos.append(piece.pos)
        return pos

    def calculate_moves(self, board):
        checks = []
        for piece_name in self.pieces:
            if any(x.get_moves(board) for x in self.pieces[piece_name]):
                checks.append(True)
        return any(checks)

    def calculate_moves_second(self, board, opponent, check):
        if check:
            pass
        # king = list(filter(lambda x: isinstance(x, King), self.pieces['k']))[0]
        for piece_name in self.pieces:
            for x in self.pieces[piece_name]:
                if isinstance(x, King):
                    x.get_moves(board, opponent.get_unsafe())
                else:
                    x.get_moves(board, opponent.get_pinned())