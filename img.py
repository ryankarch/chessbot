from PIL import Image
from game import draw_board

PIECE_SIZE = 133

def draw_board(board: list) -> Image:
    final = Image.open("./assets/Board.jpg")
    pieces = {
                'p': Image.open("./assets/PawnB.png"),
                'r': Image.open("./assets/RookB.png"),
                'n': Image.open("./assets/KnightB.png"),
                'b': Image.open("./assets/BishopB.png"),
                'q': Image.open("./assets/QueenB.png"),
                'k': Image.open("./assets/KingB.png"),
                'P': Image.open("./assets/PawnW.png"),
                'R': Image.open("./assets/RookW.png"),
                'N': Image.open("./assets/KnightW.png"),
                'B': Image.open("./assets/BishopW.png"),
                'Q': Image.open("./assets/QueenW.png"),
                'K': Image.open("./assets/KingW.png")
            }

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            
            if piece != ".":
                final.paste(pieces[piece], (PIECE_SIZE*j, PIECE_SIZE*i), pieces[piece])
    
    return final


if __name__ == "__main__":
    pass