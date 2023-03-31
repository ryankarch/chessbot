import pieces

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.rules = {}
        self.board_str = []
        self.board_piece = []
        self.white = pieces.Player("w")
        self.black = pieces.Player("b")

        self.load_board_from_fen()

    def update_check(self, result):
        if self.rules["move"] == 'w':
            king_pos = self.white.pieces["k"][0].pos
            self.board_str[king_pos[0]][king_pos[1]] = f"K{result}"
            king_pos = self.black.pieces["k"][0].pos
            self.board_str[king_pos[0]][king_pos[1]] = "k"
        else:
            king_pos = self.black.pieces["k"][0].pos
            self.board_str[king_pos[0]][king_pos[1]] = f"k{result}"
            king_pos = self.white.pieces["k"][0].pos
            self.board_str[king_pos[0]][king_pos[1]] = "K"

    def load_board_from_fen(self):

        self.board_str = []
        string = self.fen.split()
        
        rows = string[0].split("/")
        rules = string[1:]

        for i, row in enumerate(rows):
            self.board_str.append([])
            self.board_piece.append([])
            j = 0
            for cell in row:
                if cell.isalpha():
                    self.board_str[i].append(cell)
                    if cell.islower():
                        self.board_piece[i].append(self.black.create_piece(cell, (i, j)))
                    else:
                        self.board_piece[i].append(self.white.create_piece(cell, (i, j)))
                    j += 1
                else:
                    j += int(cell)
                    for _ in range(int(cell)):
                        self.board_str[i].append(".")
                        self.board_piece[i].append(pieces.Blank((i, j)))
        
        self.rules["move"] = rules[0]
        self.rules["castle"] = list(rules[1])
        self.rules["enpassant"] = rules[2]

    def load_fen_from_board(self):
        
        new_fen = []
        for row in self.board_str:
            new_fen.append("".join(row))

        new_fen = "/".join(new_fen)
        new_fen = new_fen.replace("+", "")
        
        while (new_fen.find(".") != -1):
            i = 0
            while (all(char == "." for char in new_fen[new_fen.find(".") : new_fen.find(".") + i])):
                i += 1
                if i == len(new_fen):
                    break
            i -= 1
            new_fen = new_fen[0 : new_fen.find(".")] + str(i) + new_fen[new_fen.find(".") + i :]
            
        new_fen += " " + self.rules["move"]
        new_fen += " " + "".join(self.rules["castle"]) + " " + self.rules["enpassant"]

        self.fen = new_fen

    def switch_player(self):
        if self.rules["move"] == "w":
            self.rules["move"] = "b"
        else:
            self.rules["move"] = "w"

    def advance_turn(self, switch=True):
        if self.rules["move"] == "w":
            self.white.in_check = False
            check = self.white.calculate_moves(self.board_piece)
            if check:
                self.black.in_check = True
            else:
                self.black.in_check = False
            self.black.calculate_moves_second(self.board_piece, self.white)
            if switch:
                self.switch_player()
            if self.black.in_check:
                if not self.black.can_move():
                    return "#"
                else:
                    return "+"
            else:
                return ''
        else:
            self.black.in_check = False
            check = self.black.calculate_moves(self.board_piece)
            if check:
                self.white.in_check = True
            else:
                self.white.in_check = False
            self.white.calculate_moves_second(self.board_piece, self.black)
            if switch:
                self.switch_player()
            if self.white.in_check:
                if not self.white.can_move():
                    return "#"
                else:
                    return "+"
            else:
                return ''
        

        
    def find_piece(self, piece, endpos, start=''):
        player = self.white if self.rules["move"] == 'w' else self.black
        possible_moves = player.get_moves(piece)
        for p in possible_moves:
            if endpos in possible_moves[p]:
                if start == '':
                    return p.pos
                elif p.pos[0] == start[0] or p.pos[1] == start[1]:
                    return p.pos
        return None
    
    def move(self, move):
        start, end = move
        piece = self.board_piece[start[0]][start[1]]
        other_player = self.black if self.rules["move"] == 'w' else self.white
        self.board_piece[start[0]][start[1]] = pieces.Blank(start)
        self.board_str[start[0]][start[1]] = "."
        if isinstance(self.board_piece[end[0]][end[1]], pieces.Piece):
            other_player.remove_piece(self.board_piece[end[0]][end[1]])
        self.board_piece[end[0]][end[1]] = piece
        self.board_str[end[0]][end[1]] = piece.abbrev.upper() if self.rules["move"] == 'w' else piece.abbrev.lower()
        piece.update_pos(end)
        self.load_fen_from_board()

if __name__ == "__main__":

    b = Board("rnbqk1nr/pppppppp/8/4b3/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    