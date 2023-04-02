from threading import Thread as t

class Piece(object):
    def __init__(self, color, pos, abbrev):
        self.pos = pos
        self.moves = []
        self.protecting = []
        self.pins = []
        self.checks = []
        self.check_extends = []
        self.color = color
        self.abbrev = abbrev
        self.promoted = False

    def move_straight(self, board, limit=8):
        i, j = self.pos
        count = 0
        pin = False
        pin_set = [self.pos]
        check = False
        check_set = [self.pos]
        for i_ in range(i+1, 8):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
                pin_set.append((i_, j))
                check_set.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                if isinstance(board[i_][j], King):
                    check = True
                    for i__ in range(i_+1, 8):
                        if isinstance(board[i__][j], Blank):
                            self.check_extends.append((i__, j))
                        else:
                            break
                    break
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for i_ in range(i-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i_][j], Blank):
                self.moves.append((i_, j))
                pin_set.append((i_, j))
                check_set.append((i_, j))
            elif board[i_][j].color != self.color:
                self.moves.append((i_, j))
                if isinstance(board[i_][j], King):
                    check = True
                    for i__ in range(i_-1, -1, -1):
                        if isinstance(board[i__][j], Blank):
                            self.check_extends.append((i__, j))
                        else:
                            break
                    break
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for j_ in range(j+1, 8):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
                pin_set.append((i, j_))
                check_set.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                if isinstance(board[i][j_], King):
                    check = True
                    for j__ in range(j_+1, 8):
                        if isinstance(board[i][j__], Blank):
                            self.check_extends.append((i, j__))
                        else:
                            break
                    break
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for j_ in range(j-1, -1, -1):
            if count == limit:
                break
            if isinstance(board[i][j_], Blank):
                self.moves.append((i, j_))
                pin_set.append((i, j_))
                check_set.append((i, j_))
            elif board[i][j_].color != self.color:
                self.moves.append((i, j_))
                if isinstance(board[i][j_], King):
                    check = True
                    for j__ in range(j_-1, -1, -1):
                        if isinstance(board[i][j__], Blank):
                            self.check_extends.append((i, j__))
                        else:
                            break
                    break
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
        if check:
            self.checks.append(check_set)

    def move_diagonal(self, board, limit=8):
        i, j = self.pos
        pin = False
        pin_set = [self.pos]
        check = False
        check_set = [self.pos]
        count = 0
        for inc in range(1, min(8-i, 8-j)):
            if count == limit:
                break
            if isinstance(board[i+inc][j+inc], Blank):
                self.moves.append((i+inc, j+inc))
                pin_set.append((i+inc, j+inc))
                check_set.append((i+inc, j+inc))
            elif board[i+inc][j+inc].color != self.color:
                self.moves.append((i+inc, j+inc))
                if isinstance(board[i+inc][j+inc], King):
                    check = True
                    for inc_ in range(inc + 1, min(8-i, 8-j)):
                        if isinstance(board[i+inc_][j+inc_], Blank):
                            self.check_extends.append((i+inc_, j+inc_))
                        else:
                            break
                    break
                pin_set.append((i+inc, j+inc))
                for inc_ in range(inc + 1, min(8-i, 8-j)):
                    if isinstance(board[i+inc_][j+inc_], King) and board[i+inc_][j+inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i+inc_][j+inc_], Piece) and not isinstance(board[i+inc_][j+inc_], Blank):
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for inc in range(1, min(8-i, j+1)):
            if count == limit:
                break
            if isinstance(board[i+inc][j-inc], Blank):
                self.moves.append((i+inc, j-inc))
                pin_set.append((i+inc, j-inc))
                check_set.append((i+inc, j-inc))
            elif board[i+inc][j-inc].color != self.color:
                self.moves.append((i+inc, j-inc))
                if isinstance(board[i+inc][j-inc], King):
                    check = True
                    for inc_ in range(inc + 1, min(8-i, j+1)):
                        if isinstance(board[i+inc_][j-inc_], Blank):
                            self.check_extends.append((i+inc_, j-inc_))
                        else:
                            break
                    break
                pin_set.append((i+inc, j-inc))
                for inc_ in range(inc + 1, min(8-i, j+1)):
                    if isinstance(board[i+inc_][j-inc_], King) and board[i+inc_][j-inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i+inc_][j-inc_], Piece) and not isinstance(board[i+inc_][j-inc_], Blank):
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for inc in range(1, min(i+1, 8-j)):
            if count == limit:
                break
            if isinstance(board[i-inc][j+inc], Blank):
                self.moves.append((i-inc, j+inc))
                pin_set.append((i-inc, j+inc))
                check_set.append((i-inc, j+inc))
            elif board[i-inc][j+inc].color != self.color:
                self.moves.append((i-inc, j+inc))
                if isinstance(board[i-inc][j+inc], King):
                    check = True
                    for inc_ in range(inc + 1, min(i+1, 8-j)):
                        if isinstance(board[i-inc_][j+inc_], Blank):
                            self.check_extends.append((i-inc_, j+inc_))
                        else:
                            break
                    break
                pin_set.append((i-inc, j+inc))
                for inc_ in range(inc + 1, min(i+1, 8-j)):
                    if isinstance(board[i-inc_][j+inc_], King) and board[i-inc_][j+inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i-inc_][j+inc_], Piece) and not isinstance(board[i-inc_][j+inc_], Blank):
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
        if check:
            self.checks.append(check_set)
        check = False
        check_set = [self.pos]
        count = 0
        for inc in range(1, min(i+1, j+1)):
            if count == limit:
                break
            if isinstance(board[i-inc][j-inc], Blank):
                self.moves.append((i-inc, j-inc))
                pin_set.append((i-inc, j-inc))
                check_set.append((i-inc, j-inc))
            elif board[i-inc][j-inc].color != self.color:
                self.moves.append((i-inc, j-inc))
                if isinstance(board[i-inc][j-inc], King):
                    check = True
                    for inc_ in range(inc + 1, min(i+1, j+1)):
                        if isinstance(board[i-inc_][j-inc_], Blank):
                            self.check_extends.append((i-inc_, j-inc_))
                        else:
                            break
                    break
                pin_set.append((i-inc, j-inc))
                for inc_ in range(inc + 1, min(i+1, j+1)):
                    if isinstance(board[i-inc_][j-inc_], King) and board[i-inc_][j-inc_].color != self.color:
                        pin = True
                        break
                    elif isinstance(board[i-inc_][j-inc_], Piece) and not isinstance(board[i-inc_][j-inc_], Blank):
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
        if check:
            self.checks.append(check_set)
    
    def clean_moves(self):
        self.moves = [pos for pos in self.moves if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7]
    
    def update_pos(self, pos):
        self.pos = pos

    def return_moves(self):
        return self.moves

    def check_for_checks(self):
        return len(self.checks) > 0
    

class Pawn(Piece):
    def get_moves(self, board, paths=[], checks=[]):
        self.moves = []
        self.protecting = []
        self.checks = []
        self.check_extends = []
        move_dir = 1 if self.color == 'w' else -1
        i, j = self.pos
        if isinstance(board[i-(1*move_dir)][j], Blank):
            self.moves.append((i-(1*move_dir), j))
            if isinstance(board[i-(2*move_dir)][j], Blank) and (i == 6 and self.color == 'w' or i == 1 and self.color == 'b'):
                self.moves.append((i-(2*move_dir), j))
        try:
            if not (i-(1*move_dir) < 0 or i-(1*move_dir) > 7 or j-1 < 0):
                if not isinstance(board[i-(1*move_dir)][j-1], Blank):
                    if board[i-(1*move_dir)][j-1].color != self.color:
                        if isinstance(board[i-(1*move_dir)][j-1], King):
                            self.checks.append([self.pos])
                        else:
                            self.moves.append((i-(1*move_dir), j-1))
                    else:
                        self.protecting.append((i-(1*move_dir), j-1))
        except:
            pass
        try:
            if not (i-(1*move_dir) < 0 or i-(1*move_dir) > 7 or j+1 > 7):
                if not isinstance(board[i-(1*move_dir)][j+1], Blank):
                    if board[i-(1*move_dir)][j+1].color != self.color:
                        if isinstance(board[i-(1*move_dir)][j+1], King):
                            self.checks.append([self.pos])
                        else:
                            self.moves.append((i-(1*move_dir), j+1))
                    else:
                        self.protecting.append((i-(1*move_dir), j+1))
        except:
            pass
        
        self.clean_moves()
        if checks:
            check_set = {x for x in checks[0]}
            if len(checks) > 1:
                for path in checks[1:]:
                    check_set = check_set & {x for x in path}
            self.moves = list((set(self.moves) & check_set))
        for pin_set in paths:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks()
        

class Rook(Piece):
    def get_moves(self, board, paths=[], checks=[]):
        self.moves = []
        self.protecting = []
        self.pins = []
        self.checks = []
        self.check_extends = []
        self.move_straight(board)
        if checks:
            check_set = {x for x in checks[0]}
            if len(checks) > 1:
                for path in checks[1:]:
                    check_set = check_set & {x for x in path}
            self.moves = list((set(self.moves) & check_set))
        for pin_set in paths:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks()


class Bishop(Piece):
    def get_moves(self, board, paths=[], checks=[]):
        self.moves = []
        self.protecting = []
        self.pins = []
        self.checks = []
        self.check_extends = []
        self.move_diagonal(board)
        if checks:
            check_set = {x for x in checks[0]}
            if len(checks) > 1:
                for path in checks[1:]:
                    check_set = check_set & {x for x in path}
            self.moves = list((set(self.moves) & check_set))
        for pin_set in paths:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks()


class Knight(Piece):
    def get_moves(self, board, paths=[], checks=[]):
        self.moves = []
        self.protecting = []
        self.checks = []
        self.check_extends = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) + abs(j) == 3 and self.pos[0]+i >= 0 and self.pos[0]+i <= 7 and self.pos[1]+j >= 0 and self.pos[1]+j <= 7:
                    try:
                        if isinstance(board[self.pos[0]+i][self.pos[1]+j], Blank):
                            self.moves.append((self.pos[0]+i, self.pos[1]+j))
                        else:
                            if board[self.pos[0]+i][self.pos[1]+j].color == self.color:
                                self.protecting.append((self.pos[0]+i, self.pos[1]+j))
                            elif board[self.pos[0]+i][self.pos[1]+j].color != self.color:
                                if isinstance(board[self.pos[0]+i][self.pos[1]+j], King):
                                    self.checks.append([self.pos])
                                else:
                                    self.moves.append((self.pos[0]+i, self.pos[1]+j))
                    except:
                        pass
        self.clean_moves()
        if checks:
            check_set = {x for x in checks[0]}
            if len(checks) > 1:
                for path in checks[1:]:
                    check_set = check_set & {x for x in path}
            self.moves = list((set(self.moves) & check_set))
        for pin_set in paths:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks()


class Queen(Piece):
    def get_moves(self, board, paths=[], checks=[]):
        self.moves = []
        self.protecting = []
        self.pins = []
        self.checks = []
        self.check_extends = []
        self.move_straight(board)
        self.move_diagonal(board)
        if checks:
            check_set = {x for x in checks[0]}
            if len(checks) > 1:
                for path in checks[1:]:
                    check_set = check_set & {x for x in path}
            self.moves = list((set(self.moves) & check_set))
        for pin_set in paths:
            if self.pos in pin_set:
                self.moves = list((set(self.moves) & set(pin_set)) - set(self.pos))
                break
        return self.check_for_checks()


class King(Piece):
    def get_moves(self, board, unsafe={}, checks=[]):
        self.moves = []
        self.protecting = []
        self.move_straight(board, limit=1)
        self.move_diagonal(board, limit=1)
        self.moves = list(set(self.moves) - set(unsafe))
        return self.check_for_checks()


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

    def can_move(self):
        for piece_type in self.pieces:
            for piece in self.pieces[piece_type]:
                if len(piece.return_moves()) != 0:
                    return True
        return False

    def get_protected(self):
        pos = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pos += x.protecting
        return pos

    def get_extend_check(self):
        pos = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pos += x.check_extends
        return pos
    
    def get_pinned(self):
        pins = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pins += x.pins
        return pins
    
    def get_checks(self):
        checks = []
        for p in self.pieces:
            for x in self.pieces[p]:
                checks += x.checks
        return checks
    
    def get_possible(self):
        pos = []
        for p in self.pieces:
            for x in self.pieces[p]:
                pos += x.moves
        return pos

    def get_unsafe(self):
        return self.get_protected() + self.get_possible() + self.get_extend_check()

    def load_positions(self):
        pos = []
        for piece_name in self.pieces:
            for piece in self.pieces[piece_name]:
                pos.append(piece.pos)
        return pos

    def calculate_moves(self, board):
        threads = []
        for piece_name in self.pieces:
            for x in self.pieces[piece_name]:
                threads.append(t(target=x.get_moves, args=(board,)))
                threads[-1].run()
        for thread in threads:
            while thread.is_alive():
                pass
        return len(self.get_checks()) != 0

    def calculate_moves_second(self, board, opponent):
        threads = []
        for piece_name in self.pieces:
            for x in self.pieces[piece_name]:
                if isinstance(x, King):
                    threads.append(t(target=x.get_moves, args=(board, opponent.get_unsafe())))
                    threads[-1].run()
                else:
                    threads.append(t(target=x.get_moves, args=(board, opponent.get_pinned(), opponent.get_checks())))
                    threads[-1].run()
        for thread in threads:
            while thread.is_alive():
                pass