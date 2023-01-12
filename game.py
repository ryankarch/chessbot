class Board(object):
    def __init__(self, fen:str):
        self.fen = fen
        self.board = []
        self.rules = {}

        self.parse_fen()

    def parse_fen(self):
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
        
        if all(len(r) == 8 for r in self.board) and len(self.board) == 8:
            return self.board
        else:
            return []

    def update_fen(self):
        pass
    # populate 2d list using fen string

    def get_valid_moves(board: list[list]):
        pass


if __name__ == "__main__":
    pass

# draw_board(....)
# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1