from math import inf as infinity
from random import choice

board = []
for i in range(9):
    board.append("_")
human = +1
computer = -1
freeSlot = 9
index = 0
winner = False


def check_winner(tic_tac_board, player_num):
    # 3 rows
    # 3 columns
    # 2 diagonals
    win_state = [
        [tic_tac_board[0], tic_tac_board[1], tic_tac_board[2]],
        [tic_tac_board[3], tic_tac_board[4], tic_tac_board[5]],
        [tic_tac_board[6], tic_tac_board[7], tic_tac_board[8]],

        [tic_tac_board[0], tic_tac_board[3], tic_tac_board[6]],
        [tic_tac_board[1], tic_tac_board[4], tic_tac_board[7]],
        [tic_tac_board[2], tic_tac_board[5], tic_tac_board[8]],

        [tic_tac_board[0], tic_tac_board[4], tic_tac_board[8]],
        [tic_tac_board[2], tic_tac_board[4], tic_tac_board[6]],
    ]

    if player_num == computer:
        playerMark = 'X'
    else:
        playerMark = 'O'

    if [playerMark, playerMark, playerMark] in win_state:
        return True
    else:
        return False


# Function to heuristic evaluation of board.
def evaluate(tic_tac_board):
    if check_winner(tic_tac_board, computer):
        score = +1
    elif check_winner(tic_tac_board, human):
        score = -1
    else:
        score = 0

    return score


def game_over(tic_tac_board):
    return check_winner(tic_tac_board, human) or check_winner(tic_tac_board, computer)


# Get all empty cells in board
def get_empty_cells(tic_tac_board):
    cells = []

    for x, cell in enumerate(tic_tac_board):
        if cell == '_':
            cells.append(x)

    return cells


def minimax(state, depth, tic_tac_player):
    if tic_tac_player == computer:
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, score]

    for cell in get_empty_cells(state):
        x = cell
        if tic_tac_player == computer:
            state[x] = "X"
        else:
            state[x] = "O"
        score = minimax(state, depth - 1, -tic_tac_player)
        state[x] = "_"
        score[0] = x

        if tic_tac_player == computer:
            if score[1] > best[1]:
                best = score  # max value
        else:
            if score[1] < best[1]:
                best = score  # min value

    return best


def check_valid_move(tic_tac_board, move):
    while True:
        if 0 <= move <= 8:
            if move in get_empty_cells(tic_tac_board):
                return move
            else:
                print("Location filled, please enter correct location!")
                move = ord(input())
                move -= 48
        else:
            print("Invalid location, please enter correct location!")
            move = ord(input())
            move -= 48
            move -= 1


def ai_turn():
    depth = len(get_empty_cells(board))
    if depth == 0 or game_over(board):
        return

    print('AI turn.')
    # Fill random box on board if board is empty else use minimax to find correct option
    if depth == 9:
        x = choice(get_empty_cells(board))
    else:
        move = minimax(board, depth, computer)
        x = move[0]
    print("AI chose: ", x + 1)
    board[x] = 'X'


def print_board(tic_tac_board):
    count = 0
    for row in range(3):
        print("-----------------")
        print(" | {left} || {middle} || {right} |".format(left=tic_tac_board[count], middle=tic_tac_board[count + 1]
                                                          , right=tic_tac_board[count + 2]))
        count += 3
    print("-----------------")


player = computer
print_board(board)
first = ''
while first != 'Y' and first != 'N':
    try:
        first = input('Human first to start?[y/n]: ').upper()
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()
    except (KeyError, ValueError):
        print('Bad choice')

while not winner and freeSlot != 0:
    if player == computer and first == 'N':
        ai_turn()
    elif player == human:
        print("Player " + str(player) + " turn, choose from (1-9)")
        index = ord(input())
        index -= 48
        index -= 1
        index = check_valid_move(board, index)
        board[index] = 'O'
        if first == 'Y':
            first = 'N'
    print_board(board)
    winner = check_winner(board, player)

    if not winner:
        freeSlot -= 1
        player = human if player == computer else computer

if winner:
    if player == computer:
        print("AI wins!")
    else:
        print("Human wins!")
elif not winner:
    print("Draw!")
