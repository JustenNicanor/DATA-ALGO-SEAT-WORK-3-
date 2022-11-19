board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
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
    if not isnum(user_input):
        return False
    else: return True

def isnum(userinput):
    if not userinput.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is taken already.")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row,col)


while True:
    print_board(board)
    user_input = input("Please enter a position using numbers from 1 to 9 or enter \"q\" to quit: ")
    if quit(user_input): break
    if not checkinput(user_input):
        print("Please try Again.")
        continue
    user_input = int(user_input) -1
    coords = coordinates(user_input)
    board[0][0] = "x"
    if istaken(coords, board):
        print("Please try again.")
        continue
