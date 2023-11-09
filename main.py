import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        eval = minimax(board, 0, False)
        board[i][j] = ' '

        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for player X, False for player O

    while True:
        print_board(board)

        if player_turn:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = False
            else:
                print("Cell already occupied. Try again.")
                continue
        else:
            print("AI's move:")
            row, col = get_best_move(board)
            board[row][col] = 'O'
            player_turn = True

        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
