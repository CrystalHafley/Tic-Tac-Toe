# Tic Tac Toe game in Python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # for a visual separator between rows

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [player, player, player] in win_conditions:
        return True
    return False

def get_move(player):
    while True:
        move = input(f"Player {player}, enter your move (row and column as r,c): ")
        try:
            row, col = move.split(',')
            row, col = int(row) - 1, int(col) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid move. Enter the row and column numbers separated by a comma.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    move_count = 0

    while move_count < 9:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
            move_count += 1

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return

            current_player = "O" if current_player == "X" else "X"
        else:
            print("This space is already taken. Choose another.")

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Would you like to play again? (y/n): ")
