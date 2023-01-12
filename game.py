from PIL import Image

PIECE_SIZE = 133

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

def generate_board(board: list) -> Image:
    final = Image.open("./assets/Board.jpg")
    pieces = {
                'p': Image.open("./assets/PawnB.jpg"),
                'r': Image.open("./assets/RookB.jpg"),
                'k': Image.open("./assets/KnightB.jpg"),
                'b': Image.open("./assets/BishopB.jpg"),
                'q': Image.open("./assets/QueenB.jpg"),
                'k': Image.open("./assets/KingB.jpg")
            
            }

    for i in range(8):
        for j in range(8):
            continue
    pass

if __name__ == "__main__":
    board = draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print(board)