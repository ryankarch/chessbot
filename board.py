import helper
import pieces

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.rules = {}
        self.board = []
        self.white = pieces.White()
        self.black = pieces.Black()

        self.load_board_from_fen()

        pieces.load_positions(self.white, self.board)
        pieces.load_positions(self.black, self.board)

        print(self.white.pos)
        print(self.black.pos)

    def load_board_from_fen(self):

        self.board = []
        string = self.fen.split()
        
        rows = string[0].split("/")
        rules = string[1:]

        for i,row in enumerate(rows):
            self.board.append([])
            for cell in row:
                if cell.isalpha():
                    self.board[i].append(cell)
                else:
                    for _ in range(int(cell)):
                        self.board[i].append(".")

        self.rules["move"] = rules[0]
        self.rules["castle"] = list(rules[1])
        self.rules["enpassant"] = rules[2]

    def load_fen_from_board(self):
        
        new_fen = []
        for row in self.board:
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

    b = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    