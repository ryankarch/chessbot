def draw_board(FEN: str) -> list[list]:

    string = FEN.split()
    rules = string[1]
    board = string[0].split("/")

    rep = []
    for i,row in enumerate(board):
        rep.append([])
        for cell in row:
            if cell.isalpha():
                rep[i].append(cell)
            else:
                for _ in range(int(cell)):
                    rep[i].append(".")
    
    if all(len(r) == 8 for r in rep) and len(rep) == 8:
        return rep
    else:
        return []
    # populate 2d list using fen string

if __name__ == "__main__":
    board = draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")