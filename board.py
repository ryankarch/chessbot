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


if __name__ == "__main__":

    b = Board("rnbqk1nr/pppppppp/8/4b3/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    