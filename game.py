import time

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.rules = {}
        self.board = []

        self.convert_fen_to_board()

    def convert_fen_to_board(self):

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
        self.rules["castle"] = set(list(rules[1]))
        self.rules["enpassant"] = rules[2]

        # print(self.fen)
        # print(self.board)
        # print(self.rules)

    def convert_board_to_fen(self):
        pass
    # populate 2d list using fen string

    def get_valid_moves(self, piece: str):
        pass

def get_cell_tuple(cell: str):
        # a b c d e f g h

        # 0 1 2 3 4 5 6 7

    return 8 - int(cell[1]), ord(cell[0]) - 97



if __name__ == "__main__":
    b = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    b.convert_fen_to_board()
    print(get_cell_tuple("h1"))

