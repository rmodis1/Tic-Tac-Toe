#Tic-Tac-Toe Game

import random

# Provide a welcome message
def welcome_message():
    print("Welcome to Tic Tac Toe!")

# Make the layout visually appealing
def display_sign():
    print("####################")
    print("#    Tic Tac Toe   #")
    print("####################")

# Create a 3x3 board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Create a function to take player input
def get_player_input(board):
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if pos < 0 or pos > 8:
                raise ValueError
            row, col = pos // 3, pos % 3
            if board[row][col] == ' ':
                return row, col
            else:
                print("This position is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Create a function to place the player's input on the board
def place_input_on_board(board, row, col, player):
    board[row][col] = player

# Create a function to display the board
def display_board(board):
    print("---------")
    for row in board:
        print('|'.join(row))
        print("---------")

# Create a function to check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Create a function to check if there is a winner
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

# Create a main function to run the game
def main():
    welcome_message()
    display_sign()

    while True:
        board = create_board()
        current_player = 'X'

        while True:
            display_board(board)
            if current_player == 'X':
                row, col = get_player_input(board)
            else:
                row, col = random.randint(0, 2), random.randint(0, 2)
                while board[row][col] != ' ':
                    row, col = random.randint(0, 2), random.randint(0, 2)
            
            place_input_on_board(board, row, col, current_player)

            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                display_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        
        if input("Do you want to play again? (y/n): ").lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()