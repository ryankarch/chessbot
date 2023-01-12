import time

class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.board = []
        self.rules = {}

        self.parse_fen()

    def parse_fen(self):

        # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        self.board.append([])
        row = 0
        for key in self.fen:
            if key.isalpha():
                self.board[row].append(key)
            if key == "/":
                self.board.append([])
                row += 1
            if key.isdigit():
                for _ in range(int(key)):
                    self.board[row].append(".")
            if key == " ":
                break

        # if all(len(r) == 8 for r in self.board) and len(self.board) == 8:
        #     return self.board
        # else:
        #     return []
    def parse_fen_2(self):

        string = self.fen.split()
        self.rules = string[1]
        rows = string[0].split("/")

        for i,row in enumerate(rows):
            self.board.append([])
            for cell in row:
                if cell.isalpha():
                    self.board[i].append(cell)
                else:
                    for _ in range(int(cell)):
                        self.board[i].append(".")

    def update_fen(self):
        pass
    # populate 2d list using fen string

    def get_valid_moves(board: list[list]):
        pass


if __name__ == "__main__":
    b = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    start = time.time()
    for _ in range(100000):
        b.parse_fen()
    total = time.time() - start
    print(f"parse_fen took {total} seconds to run")

    start = time.time()
    for _ in range(100000):

        b.parse_fen_2()
    total = time.time() - start
    print(f"parse_fen_2 took {total} seconds to run")
