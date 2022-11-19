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

def quit(userinput):
    if userinput == "q": 
        print("Thanks for playing")
        return True
    else: return False

def checkinput(user_input):
    isnum(user_input)
    

def isnum(userinput):
    if not userinput.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

while True:
    user_input = input("Please enter a position using numbers from 1 to 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    if not checkinput(user_input):
        print("Please try Again.")
        continue
