board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
best_moves = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"],
              ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
scores = {"O": 1,
          "X": -1,
          "tie": 0
          }
ai = "O"
human = "X"


def check_best_move():
    best_score = -1
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                temp = board[i][j]
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = temp
                if score > best_score:
                    best_score = score
                    move = (i, j)
    add_to_bm(board[move[0]][move[1]], ai)
    print("\nComputer's turn is:", board[move[0]][move[1]])
    board[move[0]][move[1]] = ai


def equals(a, b, c):
    return a == b and b == c and (a == "X" or a == "O")


def check_winner():
    winner = None
    # Horizontal
    for i in range(3):
        if equals(board[i][0], board[i][1], board[i][2]):
            winner = board[i][0]
    # Vertical
    for i in range(3):
        if equals(board[0][i], board[1][i], board[2][i]):
            winner = board[0][i]
    # Diagonal
    if equals(board[0][0], board[1][1], board[2][2]):
        winner = board[0][0]
    if equals(board[2][0], board[1][1], board[0][2]):
        winner = board[2][0]

    open_spots = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                open_spots += 1
    if winner is None and open_spots == 0:
        return "tie"
    else:
        return winner


def minimax(board, depth, is_max):
    result = check_winner()
    if result is not None:
        return scores[result]

    if is_max:
        best_score = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] != "X" and board[i][j] != "O":
                    temp = board[i][j]
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = temp
                    best_score = max(score, best_score)

        return best_score
    else:
        best_score = 1
        for i in range(3):
            for j in range(3):
                if board[i][j] != "X" and board[i][j] != "O":
                    temp = board[i][j]
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    board[i][j] = temp
                    best_score = min(score, best_score)
        return best_score


def print_board():
    print("|---|---|---|")
    print("|", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("|-----------|")
    print("|", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("|-----------|")
    print("|", board[2][0], "|", board[2][1], "|", board[2][2], "|")
    print("|---|---|---|")


def add_to_bm(pos, sym):
    for i in range(8):
        for j in range(3):
            if best_moves[i][j] == str(pos):
                best_moves[i][j] = str(sym)


def check_win():
    arr1, arr2 = ["X", "X", "X"], ["O", "O", "O"]
    for winner in best_moves:
        if winner == arr1:
            print("\nYou are win! Thanks for playing.")
            print_board()
            return False
        if winner == arr2:
            print("\nComputer win! Thanks for playing.")
            print_board()
            return False

    c = 0
    for move in board[0:3]:
        for i in move:
            if i == "X" or i == "O":
                c += 1
    if c == 9:
        print("It's Tie")
        print_board()
        return False
    return True


def main():
    print("Welcome to Tic Tac Toe.\n--------------------------------")
    print_board()
    print("X's will play first")
    while True:
        try:
            num_input = int(input("\nEnter a slot number to place X in: "))
            if num_input < 1 or num_input > 9:
                print("\nInvalid input; re-enter slot number: ")
                continue
        except:
            print("\nInvalid input; re-enter slot number: ")
            continue
        i = (num_input - 1) // 3
        j = num_input - i * 3 - 1
        if board[i][j] != "X" and board[i][j] != "O":
            board[i][j] = human
            add_to_bm(num_input, human)
            if check_win():
                check_best_move()
                if check_win():
                    print_board()
            else:
                break

        else:
            print("\nSlot already taken; re-enter slot number: ")


main()
