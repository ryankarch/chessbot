import time

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.rules = {}
        self.board = []

    def fen_to_board(self):

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

    def board_to_fen(self):
        pass
    # populate 2d list using fen string

    def get_valid_moves(board: list[list]):
        pass


if __name__ == "__main__":
    b = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

