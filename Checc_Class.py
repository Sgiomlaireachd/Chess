def convertIndex(matrix,index):
    return matrix[8 - int(index[1])][ord(index[0]) - 97]

class Piece:
    def __init__(self,pos,team):
        self.pos = pos
        self.team = team
        self.oldpos = self.pos

    def checkPosition(self,pos:str,board:list,team):
        elem = convertIndex(board,pos)
        if elem == '.':
            return 1
        elif isinstance(elem, Piece):
            if elem.team == team:
                print("Same team")
                return 0
            else:
                print("Another team")
                return 2

class Knight(Piece):

    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        xchange = abs(ord(newpos[0]) - ord(self.pos[0]))
        ychange = abs(int(newpos[1]) - int(self.pos[1]))
        if ychange == 2 and xchange == 1 or ychange == 1 and xchange == 2:
            if self.checkPosition(newpos,board,self.team) == 0:
                return False
            else:
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♞"
        else:
            return "♘"
class Rook(Piece):

    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        changex = ord(newpos[0]) - ord(self.pos[0])
        changey = int(newpos[1]) - int(self.pos[1])
        print("newpos:", newpos)
        print("self_pos:",self.pos)
        print(changex,changey)
        xchange = abs(changex)
        ychange = abs(changey)
        if xchange > 0 and ychange == 0 or xchange == 0 and ychange > 0:
            if ychange > 0:
                print("INSIDE!")
                if changey < 0:
                    print("INSIDE_Y<0")
                    for i in range(0, ychange-1):
                        print("iter")
                        s = self.pos[0]
                        s+= str(int(self.pos[1]) - (i+1))
                        print("s:", s)
                        if isinstance(convertIndex(board, s), Piece):
                            print("FALSE!")
                            return False
                else:
                    print("INSIDE_Y>0")
                    for i in range(0, ychange -1):
                        print("iter")
                        s = self.pos[0]
                        s += str(int(self.pos[1]) + (i+1))
                        print("s:",s)
                        print("object:",convertIndex(board,s))
                        if isinstance(convertIndex(board,s),Piece):
                            print("FALSE!")
                            return False
            if xchange > 0:
                print("ELSE!")
                for i in range(0,xchange - 1):
                    if changex < 0:
                        s = chr(ord(self.pos[0]) - (i + 1))
                    else:
                        s = chr(ord(self.pos[0]) + i + 1)
                    s+= self.pos[1]
                    if isinstance(convertIndex(board,s),Piece):
                        return False
            if self.checkPosition(newpos,board,self.team) == 0:
                return False
            else:
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♜"
        else:
            return "♖"
class Bishop(Piece):

    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        changex = ord(newpos[0]) - ord(self.pos[0])
        changey = int(newpos[1]) - int(self.pos[1])
        xchange = abs(changex)
        ychange = abs(changey)
        print(changex, changey)
        print(bool(changex), bool(changey))
        if xchange == ychange and xchange + ychange != 0:
            if changex > 0 and changey > 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) + i)
                    s += str(int(self.pos[1]) + i)
                    print("+ +")
                    print(s)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if changex > 0 and changey <= 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) + i+1)
                    s += str(int(self.pos[1]) - i-1)
                    print("+ -")
                    print(s)
                    if isinstance(convertIndex(board,s), Piece):
                        print("FALSE!")
                        return False
            if changex <= 0 and changey > 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) - i)
                    s += str(int(self.pos[1]) + i)
                    print("- +")
                    print(s)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if changex <= 0 and changey <= 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) - i)
                    s += str(int(self.pos[1]) - i)
                    print("- -")
                    print(s)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if self.checkPosition(newpos,board,self.team) == 0:
                return False
            else:
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♝"
        else:
            return "♗"
class King(Piece):
    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        changex = ord(newpos[0]) - ord(self.pos[0])
        changey = int(newpos[1]) - int(self.pos[1])
        xchange = abs(changex)
        ychange = abs(changey)
        if xchange < 2 and ychange < 2 and xchange + ychange != 0:
            if self.checkPosition(newpos,board,self.team) == 0:
                return False
            else:
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♚"
        else:
            return "♔"
class Queen(Piece):
    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        changex = ord(newpos[0]) - ord(self.pos[0])
        changey = int(newpos[1]) - int(self.pos[1])
        xchange = abs(changex)
        ychange = abs(changey)
        if (xchange == ychange and xchange + ychange != 0) or (xchange > 0 and ychange == 0 or xchange == 0 and ychange > 0):
            if changex > 0 and changey > 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) + i)
                    s += str(int(self.pos[1]) + i)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if changex > 0 and changey <= 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) + i)
                    s += str(int(self.pos[1]) - i)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if changex <= 0 and changey > 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) - i)
                    s += str(int(self.pos[1]) + i)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if changex <= 0 and changey <= 0:
                for i in range(1, xchange - 1):
                    s = chr(ord(self.pos[0]) - i)
                    s += str(int(self.pos[1]) - i)
                    if isinstance(convertIndex(board,s), Piece):
                        return False
            if ychange > 0 and xchange == 0:
                for i in range(0,ychange):
                    s = self.pos[0]
                    if ord(newpos[0]) - ord(self.pos[0]) < 0 or int(newpos[1]) - int(self.pos[1]) < 0:
                        s+= str(int(self.pos[1]) - i+1)
                    else:
                        s += str(int(self.pos[1]) + i+1)
                    if isinstance(convertIndex(board,s),Piece):
                        return False
            if xchange > 0 and ychange == 0:
                for i in range(0,xchange):
                    if ord(newpos[0]) - ord(self.pos[0]) < 0 or int(newpos[1]) - int(self.pos[1]):
                        s = chr(ord(self.pos[0]) - i+1)
                    else:
                        s = chr(ord(self.pos[0]) + i+1)
                    s+= self.pos[1]
                    if isinstance(convertIndex(board,s),Piece):
                        return False
            if self.checkPosition(newpos,board,self.team) == 0:
                return False
            else:
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♛"
        else:
            return "♕"
class Pawn(Piece):

    def move(self,newpos:str,board:list) -> bool:
        self.oldpos = self.pos
        changex = ord(newpos[0]) - ord(self.pos[0])
        changey = int(newpos[1]) - int(self.pos[1])
        print(changex,changey)
        if int(self.pos[1]) == 2 or int(self.pos[1]) == 7:
            maxstep = 2
        else:
            maxstep = 1
        if not self.team:
            maxstep *= -1
        print(maxstep)
        if self.checkPosition(newpos,board,self.team) == 0:
            return False
        elif self.checkPosition(newpos,board,self.team) == 2:
            if ((changex == 1 and changey == 1) or (changex == -1 and changey == 1)) and self.team:
                self.pos = newpos
                return True
            elif ((changex == -1 and changey == -1) or (changex == 1 and changey == -1)) and not self.team:
                self.pos = newpos
                return True
            else:
                return False
        else:
            if changex == 0 and abs(changey) <= abs(maxstep):
                print("INSIDE!")
                if abs(maxstep) > 1:
                    if self.team:
                        s = self.pos[0]
                        s+= str(int(self.pos[1]) + 1)
                        if isinstance(convertIndex(board,s), Piece):
                            return False
                    else:
                        s = self.pos[0]
                        s += str(int(self.pos[1]) - 1)
                        if isinstance(convertIndex(board, s), Piece):
                            return False
                self.pos = newpos
                return True
        return False
    def show(self):
        if self.team:
            return "♟"
        else:
            return "♙"



















