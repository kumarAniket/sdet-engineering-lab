import random

from IPython.display import clear_output


def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input('Player 1 choose X or O: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def first_play():
    player_first = random.randint(0,1)
    if player_first == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def user_choice():
    while True:
        choice = input("Please enter a number (1-9): ")
        if choice.isdigit() and int(choice) in range(1, 10):
            return int(choice)
        print("Invalid input. Please enter an index (1-9)!!")

def player_choice(board):
    while True:
        position = user_choice()
        if space_check(board, position):
            return position
        print("That space is already occupied! Choose another.")

def place_marker(board,marker,position):
    board[position] = marker

def space_check(board,position):
    return board[position] == ' '

def full_board(board):
    for index in range(1,10):
        if space_check(board,index):
            return False
    return True

def win_check(board,marker):
    return ((board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (
                board[7] == board[8] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker) or (
                    board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (
                        board[3] == board[6] == board[9] == marker)
            )

def replay_game():
    replay = input("Do you want to play again? (y/n): ").lower()

    return replay == 'y'

if __name__ == '__main__':
    board = [' '] * 10

    print('Welcome to Tic Tac Toe!')
    player1_marker,player2_marker = player_input()
    turn = first_play().upper()

    print(f'{turn} will go first.')

    game_on = input("Ready to play? y or n: ").lower() == 'y'

    while game_on:
        display_board(board)
        current_marker = player1_marker if turn == 'PLAYER 1' else player2_marker

        print(f"{turn}'s turn ({current_marker}):")
        pos_index = player_choice(board)
        place_marker(board, current_marker, pos_index)

        if win_check(board, current_marker):
            display_board(board)
            print(f"Congratulations, {turn} won!")
            game_on = False
        elif full_board(board):
            display_board(board)
            print("Oops... We have a tie!!!")
            game_on = False
        else:
            turn = 'PLAYER 2' if turn == 'PLAYER 1' else 'PLAYER 1'

