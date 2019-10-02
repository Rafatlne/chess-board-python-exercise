rowTopBot = "-----------------------------------------"
middleRows = "----+"
column = "| "
x = "   "
bPawns = "BP "
wPawns = "WP "
allPieces = {}
row = "  a    b    c    d    e    f    g    h"
position = ['A','B','C','D','E','F','G','H']
bPieces = ['BR ','BN ','BB ','BQ ','BK ','BB ','BN ','BR ']
wPieces = ['WR ','WN ','WB ','WQ ' ,'WK ','WB ','WN ','WR ' ]

# This function will make dictionary  of pieces
def make():
    for i in range(1,9):
        if (i == 2):
            for j in range(0,8):
                allPieces[position[j] + str(i)] = wPawns
        elif (i == 1):
            for j in range(0,8):
                allPieces[position[j] + str(i)] = wPieces[j]
        elif (i == 8):
            for j in range(0,8):
                allPieces[position[j] + str(i)] = bPieces[j]
        elif (i == 7):
            for j in range(0,8):
                allPieces[position[j] + str(i)] = bPawns
        else:
            for j in range(0,8):
                allPieces[position[j] + str(i)] = x

# This function will print the row of top and bottom
def makerowTopBot():
    print(rowTopBot)

# This function will print the middlerows
def middleRowsPrint():
    print(' ',end='')
    for i in range(8):
        print(middleRows,end = '')
    print('')

# This function will print the column and pieces of chess
def columnPrint(indx):
    for i in range(8):
        print(column,end = '')
        print(allPieces[position[i] + str(indx)],end='')
    print(column, end='')
    print(indx)
# This function will initiate chess board
def makeChessBoard():
    j = 8
    for i in range(0,17):
        if (i == 0):
            makerowTopBot()
        elif ( i == 16):
            makerowTopBot()
            print(row)
        elif(i % 2 == 0):
            middleRowsPrint()
        else:
            columnPrint(j)
            if( j < 1):
                j = 8
            else:
                j = j - 1

#This function will take input and change the position of pieces      
def takeInput():
    i = 1
    while(1):
        if(i % 2 == 0):
            print("BLACK TURN")
            piecesName = input("Tell me your piece: ")
            currentPos = input("Current position of your piece: ")
            positionAt = input("Tell me next position of your piece: ")
            editDict(currentPos.upper(),positionAt.upper(),piecesName.upper())
            
        else:
            print("WHITE TURN")
            piecesName = input("Tell me your piece: ")
            currentPos = input("Current position of your piece: ")
            positionAt = input("Next position of your piece: ")
            editDict(currentPos.upper(),positionAt.upper(),piecesName.upper())
        i = i + 1

# This function will modify the dictionary of the pieces
def editDict(currentPos,positionAt, piecesName):
    allPieces[currentPos] = x
    allPieces[positionAt] = piecesName + ' '
    makeChessBoard() 
       

if __name__ == "__main__":
    make()
    makeChessBoard()
    takeInput()
    