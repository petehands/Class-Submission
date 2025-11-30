ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(str(i) for i in range(COLS)))
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * (COLS * 4 + 1))

def drop_piece(board, col, piece):
    for row in reversed(board):
        if row[col] == " ":
            row[col] = piece
            return True
    return False  # Column full

def check_win(board, piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Check diagonal up-right
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def board_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def play_game():
    board = create_board()
    turn = 0  # 0 = Player X, 1 = Player O
    pieces = ["X", "O"]

    while True:
        print_board(board)
        piece = pieces[turn]
        print(f"Player {piece}'s turn.")

        try:
            col = int(input("Choose a column (0-6): "))
            if not (0 <= col < COLS):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number 0-6.")
            continue

        if not drop_piece(board, col, piece):
            print("Column full! Try a different one.")
            continue

        if check_win(board, piece):
            print_board(board)
            print(f" Player {piece} WINS!")
            break

        if board_full(board):
            print_board(board)
            print("It's a DRAW!")
            break

        turn = 1 - turn #switch plater

if __name__ == "__main__":
    play_game()