board = [
  ["_", "_", "_"],
  ["_", "_", "_"],
  ["_", "_", "_"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}", end="")
        print()

print_board(board)

def quit(user_input):
    if user_input == "q": 
        print("Thanks for playing")
        return True
    else: return False

while True:
    user_input = input("Please enter a position using numbers from 1 to 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    