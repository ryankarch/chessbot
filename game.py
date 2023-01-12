import time

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.rules = {}
        self.board = []

        self.load_board_from_fen()

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

        if self.rules["move"] == 'b':
            self.board = self.board[::-1]

        # print(self.fen)
        # print(self.board)
        # print(self.rules)

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
    # populate 2d list using fen string

    def get_valid_moves(self, piece: str):
        pass

def get_cell_tuple(cell: str):
        # a b c d e f g h

        # 0 1 2 3 4 5 6 7

    return 8 - int(cell[1]), ord(cell[0]) - 97



if __name__ == "__main__":
    b = Board("3rkb1r/p5p1/7q/p1p2p2/7P/1PB1N1K1/P2Q4/3R3b w k - 0 28")
    print(b.board)
    b.load_fen_from_board()
    print(get_cell_tuple("h1"))
    b.load_board_from_fen()
    print(b.fen)

