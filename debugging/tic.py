#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("-" * 11)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            prompt = f"Player {current_player}, enter row and col (0-2) separated by space: "
            user_input = input(prompt).split()
            
            if len(user_input) != 2:
                print("Please enter TWO numbers.")
                continue
                
            row, col = map(int, user_input)
            
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
                
            board[row][col] = current_player
            
            if check_winner(board):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break
            
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
            
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()