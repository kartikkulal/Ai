name = input("enter your name:")
usn = input("enter your usn:")
print(name, usn)

board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def is_draw():
    return " " not in board


def play_game():
    player = "X"

    while True:
        display_board()

        position = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position!")
            continue

        if board[position] != " ":
            print("Position already occupied!")
            continue

        board[position] = player

        if check_winner(player):
            display_board()
            print(f"Player {player} wins!")
            break

        if is_draw():
            display_board()
            print("It's a draw!")
            break

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"


play_game()