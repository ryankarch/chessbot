from PIL import Image
from board import Board

PIECE_SIZE = 133
PIECES = {
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

def draw_board(b: Board) -> None:
    board = b.board
    player = b.rules["move"]

    if not board or len(board) != 8:
        Image.open("./assets/BoardError.jpg").save("./assets/RunningBoard.jpg")
        return

    final = Image.open("./assets/Board.jpg")

    if player == "b":
        board = [x[::-1] for x in board[::-1]]
        final = final.rotate(180)

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            
            if piece != ".":
                final.paste(PIECES[piece], (PIECE_SIZE*j + 30, PIECE_SIZE*i + 30), PIECES[piece])
    
    final.save("./assets/RunningBoard.jpg")


if __name__ == "__main__":
    pass