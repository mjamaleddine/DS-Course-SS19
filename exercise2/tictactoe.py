field = ["0","1","2","3","4","5","6","7","8"]
playerOneMarker = "X"
playerTwoMarker = "O"
draw = True

def showField():
    print(field[0],"|",field[1],"|",field[2])
    print(field[3],"|",field[4],"|",field[5])
    print(field[6],"|",field[7],"|",field[8])

def playerInput(player):
    if player == playerOneMarker:
        playerMarker = playerOneMarker
        playerName = "Player 1"
    elif player == playerTwoMarker:
        playerMarker = playerTwoMarker
        playerName = "Player 2"

    while True:
        fieldPosition = input(playerName+": Which field you want to place:")
        if validateInput(fieldPosition):
            field[int(fieldPosition)] = playerMarker
            break
        else:
            print("Sorry you did not enter a valid position. Please use one of the remaining Numbers!")
            continue
            
def validateInput(fieldPosition):
    if int(fieldPosition) > len(field) or int(fieldPosition) < 0:
        return False
    elif field[int(fieldPosition)] == "X" or field[int(fieldPosition)] == "O":
        return False
    return True

def checkWin(playerMarker):
    return((field[0] == playerMarker and field[1] == playerMarker and field[2] == playerMarker) or #top row
    (field[3] == playerMarker and field[4] == playerMarker and field[5] == playerMarker) or #mid row 
    (field[6] == playerMarker and field[7] == playerMarker and field[8] == playerMarker) or #bottom row 
    (field[0] == playerMarker and field[3] == playerMarker and field[6] == playerMarker) or #left column
    (field[1] == playerMarker and field[4] == playerMarker and field[7] == playerMarker) or #mid column
    (field[2] == playerMarker and field[5] == playerMarker and field[8] == playerMarker) or #right column
    (field[0] == playerMarker and field[4] == playerMarker and field[8] == playerMarker) or #diagonal1
    (field[2] == playerMarker and field[4] == playerMarker and field[6] == playerMarker)) #diagonal2

showField()
for i in range(9):
    if i % 2 == 0:
        playerInput(playerOneMarker)
        if checkWin(playerOneMarker):
            print("Player 1 has won! Congratulations!")
            draw = False
            break
    if i % 2 == 1:
        playerInput(playerTwoMarker)
        if checkWin(playerTwoMarker):
            print("Player 2 has won! Congratulations!")
            draw = False
            break
    showField()
if draw == True:
    print("The game ended in a draw! There were no winners :(")
