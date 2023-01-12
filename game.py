from PIL import Image

PIECE_SIZE = 133

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