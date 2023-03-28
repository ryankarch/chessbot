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
        
        while (new_fen.find(".") != -1):
            i = 0
            while (all(char == "." for char in new_fen[new_fen.find(".") : new_fen.find(".") + i])):
                i += 1
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
            self.white.calculate_moves(self.board_piece)
            # include something for check
            self.black.calculate_moves(self.board_piece)
        else:
            self.black.calculate_moves(self.board_piece)
            # include something for check
            self.white.calculate_moves(self.board_piece)
        if switch:
            self.switch_player()

        
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
        pass

if __name__ == "__main__":

    b = Board("rnbqk1nr/pppppppp/8/4b3/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    