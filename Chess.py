import Checc_Class as C
def convertIndex(matrix,index):
    return matrix[8 - int(index[1])][ord(index[0]) - 97]
def Print(matrix):
    c = 8
    s = "a"
    for i in matrix:
        print(c, end="| ")
        c-=1
        for j in i:
            if isinstance(j,C.Piece):
                print(j.show(),end=" ")
            else:
                print(j,end=" ")
        print()
        if  c == 0:
            print("   ",end="")
            for k in range(8):
                print(chr(ord(s) + k),end=" ")
def rightPick(pick,teamtoggle,board):
    if (ord(pick[0]) >= 97 and ord(pick[0]) <= 104) and (int(pick[1]) >= 1 and int(pick[1]) <= 8):
        if isinstance(convertIndex(board,pick), C.Piece):
            if convertIndex(board,pick).team == teamtoggle:
                return True
    return False
def onTheBoard(board,king):
    for i in board:
        if king in i:
            return True
    return False

board = []
for i in range(8):
    b = []
    for j in range (8):
        b.append(".")
    board.append(b)
# First layer | Black
board[0][0] = C.Rook("a8",0)
board[0][1] = C.Knight("b8",0)
board[0][2] = C.Bishop("c8",0)
board[0][3] = C.Queen("d8",0)
board[0][4] = C.King("e8",0)
board[0][5] = C.Bishop("f8",0)
board[0][6] = C.Knight("g8",0)
board[0][7] = C.Rook("h8",0)
# Second layer | Black
for i in range(8):
    s = chr(ord("a") + i)
    s += "7"
    board[1][i] = C.Pawn(s,0)
#First layer | White
for i in range(8):
    s = chr(ord("a") + i)
    s += "2"
    board[6][i] = C.Pawn(s, 1)
#Second layer | White
board[7][0] = C.Rook("a1",1)
board[7][1] = C.Knight("b1",1)
board[7][2] = C.Bishop("c1",1)
board[7][3] = C.Queen("d1",1)
board[7][4] = C.King("e1",1)
board[7][5] = C.Bishop("f1",1)
board[7][6] = C.Knight("g1",1)
board[7][7] = C.Rook("h1",1)
Print(board)

whiteKing = board[7][4]
blackKing = board[0][4]

teamToggle = True
mistake = False
while(onTheBoard(board,whiteKing) and onTheBoard(board,blackKing)):
    mistake = False
    if(teamToggle):
        print("\n~~WHITE~~")
    else:
        print("\n~~BLACK~~:")

    pick = input("pick:")
    if rightPick(pick,teamToggle,board):
        figure = convertIndex(board,pick)
        pos = input("move:")
        if figure.move(pos,board):
            board[8 - int(figure.oldpos[1])][ord(figure.oldpos[0]) - 97] = '.'
            board[8 - int(figure.pos[1])][ord(figure.pos[0]) - 97] = figure
        else:
            mistake = True
            print("wrong move.")
    else:
        mistake = True
        print("wrong pick.")
    Print(board)
    if not mistake:
        teamToggle = not teamToggle