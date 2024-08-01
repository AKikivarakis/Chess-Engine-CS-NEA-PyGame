import pygame
from move import Move

class Piece():

    def __init__(self, colour, positionX, positionY, pieceType, value):
        self.colour = colour
        self.positionX  = positionX
        self.positionY = positionY
        self.pieceType = pieceType
        self.value = value
        self.validMoves = []
        self.moved = False
        self.image = None

    def addMove(self, move):
        self.validMoves.append(move)

    def getColour(self):
        return self.colour

    def getType(self):
        return self.pieceType

    def getPositionX(self):
        return self.positionX

    def getPositionY(self):
        return self.positionY

    def getPos(self):
        return (self.positionX, self.positionY)

    def getValue(self):
        return self.value

    def getImage(self):
        return self.image

    def getMoved(self):
        return self.moved

    def checkStaights(self, board):

        move = None

        # Get South
        for i in range(self.positionY+1, 8):
            if board.getBoard()[i][self.positionX] == 0:
                move = Move(self.getPos(), (self.positionX, i))
                self.addMove(move)
            elif board.getBoard()[i][self.positionX].getColour() != self.colour:
                move = Move(self.getPos(), (self.positionX, i))
                self.addMove(move)
                break
            else:
                break

        # Get East
        for i in range(self.positionX+1, 8):
            if board.getBoard()[self.positionY][i] == 0:
                move = Move(self.getPos(), (i, self.positionY))
                self.addMove(move)
            elif board.getBoard()[self.positionY][i].getColour() != self.colour:
                move = Move(self.getPos(), (i, self.positionY))
                self.addMove(move)
                break
            else:
                break

        # Get West
        for i in range(self.positionX-1, -1, -1):
            if board.getBoard()[self.positionY][i] == 0:
                move = Move(self.getPos(), (i, self.positionY))
                self.addMove(move)
            elif board.getBoard()[self.positionY][i].getColour()!= self.colour:
                move = Move(self.getPos(), (i, self.positionY))
                self.addMove(move)
                break
            else:
                break

        # Get North
        for i in range(self.positionY-1, -1, -1):
            if board.getBoard()[i][self.positionX] == 0:
                move = Move(self.getPos(), (self.positionX, i))
                self.addMove(move)
            elif board.getBoard()[i][self.positionX].getColour()!= self.colour:
                move = Move(self.getPos(), (self.positionX, i))
                self.addMove(move)
                break
            else:
                break          

    def checkDiagonals(self, board):

        move = None

        # Get South-East
        for i in range(1,8):
            if self.positionX+i < 8 and self.positionY+i < 8:
                if board.getBoard()[self.positionY+i][self.positionX+i] == 0:
                    move = Move(self.getPos(), (self.positionX+i, self.positionY+i))
                    self.addMove(move)
                elif board.getBoard()[self.positionY+i][self.positionX+i].getColour() != self.colour:
                    move = Move(self.getPos(), (self.positionX+i, self.positionY+i))
                    self.addMove(move)
                    break
                else:
                    break
            else:
                break

        # Get South-West
        for i in range(1,8):
            if self.positionX-i >= 0 and self.positionY+i < 8:
                if board.getBoard()[self.positionY+i][self.positionX-i] == 0:
                    move = Move(self.getPos(), (self.positionX-i, self.positionY+i))
                    self.addMove(move)
                elif board.getBoard()[self.positionY+i][self.positionX-i].getColour()!= self.colour:
                    move = Move(self.getPos(), (self.positionX-i, self.positionY+i))
                    self.addMove(move)
                    break
                else:
                    break
            else:
                break

        # Get North-East
        for i in range(1,8):
            if self.positionX+i < 8 and self.positionY-i >= 0:
                if board.getBoard()[self.positionY-i][self.positionX+i] == 0:
                    move = Move(self.getPos(), (self.positionX+i, self.positionY-i))
                    self.addMove(move)
                elif board.getBoard()[self.positionY-i][self.positionX+i].getColour()!= self.colour:
                    move = Move(self.getPos(), (self.positionX+i, self.positionY-i))
                    self.addMove(move)
                    break
                else:
                    break
            else:
                break

        # Get North-West
        for i in range(1,8):
            if self.positionX-i >= 0 and self.positionY-i >= 0:
                if board.getBoard()[self.positionY-i][self.positionX-i] == 0:
                    move = Move(self.getPos(), (self.positionX-i, self.positionY-i))
                    self.addMove(move)
                elif board.getBoard()[self.positionY-i][self.positionX-i].getColour()!= self.colour:
                    move = Move(self.getPos(), (self.positionX-i, self.positionY-i))
                    self.addMove(move)
                    break
                else:
                    break
            else:
                break

    def getValidMoves(self, board):
        return self.validMoves

    def setMovedTrue(self):
        self.moved = True

    def setPos(self, pos):
        self.positionX = pos[0]
        self.positionY = pos[1]


class Pawn(Piece):

    def __init__(self, colour, positionX, positionY):
        super().__init__(colour, positionX, positionY, "pawn", 10)

        if self.colour == "white":
            image = pygame.image.load('/images/w_pawn_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_pawn_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        self.direction = None

    def getValidMoves(self, board):

        self.validMoves = []

        move = None

        if board.getPlayerColour() == self.colour:
            self.direction = -1
        else:
            self.direction = 1

        # The pawn can move one space forward
        if board.getBoard()[self.positionY+self.direction][self.positionX] == 0:

            move =  Move((self.positionX, self.positionY), (self.positionX, self.positionY+self.direction))
            self.addMove(move)

        # The pawn can move two spaces forward when unmoved
        if (board.getBoard()[self.positionY+self.direction][self.positionX] == 0) and (board.getBoard()[self.positionY+2*self.direction][self.positionX] == 0) and (self.moved == False):
            move =  Move((self.positionX, self.positionY), (self.positionX, self.positionY+2*self.direction))
            self.addMove(move)
        
        # The pawn can capture diagonally to the right
        if ((self.positionX + 1) < 8):
            if board.getBoard()[self.positionY+self.direction][self.positionX+1]!= 0:
                if board.getBoard()[self.positionY+self.direction][self.positionX+1].getColour()!= self.colour:
                    move = Move((self.positionX, self.positionY), (self.positionX+1, self.positionY+self.direction))
                    self.addMove(move)

        # The pawn can capture diagonally to the left
        if ((self.positionX - 1) > 0):
            if board.getBoard()[self.positionY+self.direction][self.positionX-1]!= 0:
                if board.getBoard()[self.positionY+self.direction][self.positionX-1].getColour()!= self.colour:
                    move = Move((self.positionX, self.positionY), (self.positionX-1, self.positionY+self.direction))
                    self.addMove(move)

        return self.validMoves

class Knight(Piece):
    
    def __init__(self, colour, positionX, positionY):
        super().__init__(colour, positionX, positionY, "knight", 30)

        if self.colour == "white":
            image = pygame.image.load('/images/w_knight_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_knight_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

    def getValidMoves(self, board):

        self.validMoves = []

        move = None

        # Moves for the knight
        possible_moves = [
            (self.positionX+2, self.positionY+1),
            (self.positionX+2, self.positionY-1),
            (self.positionX-2, self.positionY+1),
            (self.positionX-2, self.positionY-1),
            (self.positionX+1, self.positionY+2),
            (self.positionX+1, self.positionY-2),
            (self.positionX-1, self.positionY+2),
            (self.positionX-1, self.positionY-2)
        ]

        for move in possible_moves:

            # If move on board
            if (move[0] < 8) and (move[1] < 8) and (move[0] >= 0) and (move[1] >= 0):
                # If move is on piece of opposite colour allow capture
                if board.getBoard()[move[1]][move[0]] != 0:
                    if board.getBoard()[move[1]][move[0]].getColour() != self.colour:
                        m = Move(self.getPos(), (move))
                        self.addMove(m)
                # Move to empty square
                else:
                    m = Move(self.getPos(), (move))
                    self.addMove(m)

        return self.validMoves

class Bishop(Piece):

    def __init__(self, colour, positionX, positionY):
        super().__init__(colour, positionX, positionY, "bishop", 30.01)

        if self.colour == "white":
            image = pygame.image.load('/images/w_bishop_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_bishop_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

    def getValidMoves(self, board):

        self.validMoves = []

        # Bishops move diagonally
        self.checkDiagonals(board)
        return self.validMoves

class Rook(Piece):

    def __init__(self, colour, positionX, positionY):
        super().__init__(colour, positionX, positionY, "rook", 50)

        if self.colour == "white":
            image = pygame.image.load('/images/w_rook_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_rook_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))



    def getValidMoves(self, board):

        self.validMoves = []

        # Rook can move straight
        self.checkStaights(board)     
        return self.validMoves

class Queen(Piece):

    def __init__(self, colour, positionX, positionY):
        super().__init__(colour, positionX, positionY, "queen", 90)

        if self.colour == "white":
            image = pygame.image.load('/images/w_queen_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_queen_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

    def getValidMoves(self, board):

        self.validMoves = []

        # The queen moves on straights and along diagonals
        self.checkStaights(board)
        self.checkDiagonals(board)

        return self.validMoves

class King(Piece):

    def __init__(self, colour, positionX, positionY):
        # value of king is winning the game so king value is infinity
        super().__init__(colour, positionX, positionY, "king", 999999)

        if self.colour == "white":
            image = pygame.image.load('/images/w_king_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

        else:
            image = pygame.image.load('/images/b_king_1x.png')
            self.image = pygame.transform.scale(image, (75, 75))

    def getValidMoves(self, board):

        move = None
        self.validMoves = []

        # Moves for the king
        possible_moves= [
            (self.positionX+1, self.positionY),
            (self.positionX+1, self.positionY+1),
            (self.positionX+1, self.positionY-1),
            (self.positionX, self.positionY+1),
            (self.positionX-1, self.positionY),
            (self.positionX-1, self.positionY+1),
            (self.positionX-1, self.positionY-1),
            (self.positionX, self.positionY-1)
        ]

        for move in possible_moves:

            # If move on board
            if (move[0] < 8) and (move[1] < 8) and (move[0] >= 0) and (move[1] >= 0):
                # If move is on piece of opposite colour allow capture
                if board.getBoard()[move[1]][move[0]] != 0:
                    if board.getBoard()[move[1]][move[0]].getColour() != self.colour:
                        m = Move(self.getPos(), (move))
                        self.addMove(m)
                # Move to empty square
                else:
                    m = Move(self.getPos(), (move))
                    self.addMove(m)

            # Check for castled moves
            self.canCastle(board)

        return self.validMoves

    def canCastle(self, board):

        # Variables for castle flags and pieces
        piece = None
        castleLeft = None
        castleRight = None
        leftRook = None
        rightRook = None

        # Find corresponding rook on the board
        for i in range(0, 8):
            for j in range(0, 8):
                piece = board.getBoard()[i][j]
                if piece != 0:

                    # Check if piece is a rook, if it is the same colour, if it hasn't moved and the king hasn't moved
                    if (piece.getColour() == self.colour) and (piece.getMoved() == False) and (piece.getType() == "rook") and (self.moved == False):

                        # Check which direction the king can castle based on the position of the rook
                        if piece.getPositionX() < self.positionX:
                            # Set left rook flag to true if left rook is found
                            castleLeft = True
                            leftRook = piece

                        if piece.getPositionX() > self.positionX:
                            # Set right rook flag to true if right rook is found
                            castleRight = True
                            rightRook = piece

        # Check if squares between left rook and king are  blank, else the king can't castle
        if castleLeft:
            for i in range(leftRook.getPositionX()+1, self.positionX):
                if board.getBoard()[self.positionY][i] != 0:
                    castleLeft = False

        # Check if squares between right rook and king are  blank, else the king can't castle
        if castleRight:
            for i in range(self.positionX+1, rightRook.getPositionX()):
                if board.getBoard()[self.positionY][i]!= 0:
                    castleRight = False

        # If flag for left rook is true, then add minus two spaces in x direction to moves list
        if castleLeft:
            self.addMove(Move(self.getPos(), (self.positionX-2, self.positionY)))

        # If flag for right rook is true, then add two spaces in x direction to moves list
        if castleRight:
            self.addMove(Move(self.getPos(), (self.positionX+2, self.positionY)))
