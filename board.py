from pieces import *
import random
from square import Square

class Board():

    def __init__(self, board_colour, player_colour):
        # Board as an empty 8x8 matrix - 0 represent empty square
        self.board = [[0 for i in range(0, 8)] for j in range(0, 8)]

        self.previous_board = []

        self.squares = []

        # Board setup if player is white
        self.player_white_start_pos = [

            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        # Board setup is player is black
        self.player_black_start_pos = [
            ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ]
        # King-square table
        self.king_space_player = [
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
            [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
            [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
            [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
            [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
        ]

        king_space_compt = self.king_space_player.copy()
        king_space_compt.reverse()
        self.king_space_compt = king_space_compt

        # Queen-square table
        self.queen_space_player = [
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
            [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
        ]

        queen_space_compt = self.queen_space_player.copy()
        queen_space_compt.reverse()
        self.queen_space_compt = queen_space_compt


        # Rook-square table
        self.rook_space_player = [
            [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
            [0.0,   0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
        ]

        rook_space_compt = self.rook_space_player.copy()
        rook_space_compt.reverse()
        self.rook_space_compt = rook_space_compt

        # Bishop-square table
        self.bishop_space_player = [
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
            [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
            [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
            [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
            [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
            [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
            [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
        ]

        bishop_space_compt = self.bishop_space_player.copy()
        bishop_space_compt.reverse()
        self.bishop_space_compt = bishop_space_compt

        # Knight-square table
        self.knight_space_player = [
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
            [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
            [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
            [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
            [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
            [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
            [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
            [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
        ]

        knight_space_compt = self.knight_space_player.copy()
        knight_space_compt.reverse()
        self.knight_space_compt = knight_space_compt

        # Pawn-square table
        self.pawn_space_player = [
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
            [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
            [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
            [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
            [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
            [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
            [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
            [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
        ]

        pawn_space_compt = self.pawn_space_player.copy()
        pawn_space_compt.reverse()
        self.pawn_space_compt = pawn_space_compt

        self.board_colour = board_colour

        self.player_colour = player_colour

        self.turn = 'white'

        self.moves = []

        self.piece_selected = None

    def setupBoard(self, other_board):

        square = None
        for i in range(0, 8):
            for j in range(0, 8):  

                # Choose board template           
                if other_board is None:
                    if self.player_colour == "white":
                        square = self.player_white_start_pos[i][j]
                    elif self.player_colour == "black": 
                        square = self.player_black_start_pos[i][j]

                else:
                    square =  other_board[i][j]

                # Corresponding ascii value for each square
                if square == 'R':
                    self.board[i][j] = Rook("white", j, i)
                elif square == 'B':
                    self.board[i][j] = Bishop("white", j, i)
                elif square == 'N':
                    self.board[i][j] = Knight("white", j, i)
                elif square == 'Q':
                    self.board[i][j] = Queen("white", j, i)
                elif square == 'K':
                    self.board[i][j] = King("white", j, i)
                elif square == 'P':
                    self.board[i][j] = Pawn("white", j, i)
                elif square == 'r':
                    self.board[i][j] = Rook("black", j, i)
                elif square == 'b':
                    self.board[i][j] = Bishop("black", j, i)
                elif square == 'n':
                    self.board[i][j] = Knight("black", j, i)
                elif square == 'q':
                    self.board[i][j] = Queen("black", j, i)
                elif square == 'k':
                    self.board[i][j] = King("black", j, i)
                elif square == 'p':
                    self.board[i][j] = Pawn("black", j, i)
                elif square == '.':
                    self.board[i][j] = 0

    def evaluate(self):
        
        # Placeholder for each piece and evaluation starts at 0 
        piece = None
        eval = 0

        for i in range(0, 8):
            for j in range(0, 8):

                if self.board[i][j] != 0:

                    piece = self.board[i][j]

                    if self.player_colour == "white":

                        # if playing as white, positive points for white pieces and positions on board
                        if piece.getColour() == "white":
                            if piece.getType() == "pawn":
                                eval += self.pawn_space_player[i][j]
                            elif piece.getType() == "bishop":
                                eval += self.bishop_space_player[i][j]
                            elif piece.getType() == "knight":
                                eval += self.knight_space_player[i][j]
                            elif piece.getType() == "rook":
                                eval += self.rook_space_player[i][j]
                            elif piece.getType() == "queen":
                                eval += self.queen_space_player[i][j]
                            elif piece.getType() == "king":
                                eval += self.king_space_player[i][j]

                            eval += piece.getValue()
                        # if playing as white, negative points for black pieces and positions on board, reverse board for calc
                        else:
                            if piece.getType() == "pawn":
                                eval -= self.pawn_space_compt[i][j]
                            elif piece.getType() == "bishop":
                                eval -= self.bishop_space_compt[i][j]
                            elif piece.getType() == "knight":
                                eval -= self.knight_space_compt[i][j]
                            elif piece.getType() == "rook":
                                eval -= self.rook_space_compt[i][j]
                            elif piece.getType() == "queen":
                                eval -= self.queen_space_compt[i][j]
                            elif piece.getType() == "king":
                                eval -= self.king_space_compt[i][j]

                            eval -= piece.getValue()

                    else:
                        # if playing as black, negative points for white pieces and positions on board, reverse board for calc 
                        if piece.getColour() == "white":
                            if piece.getType() == "pawn":
                                eval -= self.pawn_space_compt[i][j]
                            elif piece.getType() == "bishop":
                                eval -= self.bishop_space_compt[i][j]
                            elif piece.getType() == "knight":
                                eval -= self.knight_space_compt[i][j]
                            elif piece.getType() == "rook":
                                eval -= self.rook_space_compt[i][j]
                            elif piece.getType() == "queen":
                                eval -= self.queen_space_compt[i][j]
                            elif piece.getType() == "king":
                                eval -= self.king_space_compt[i][j]

                            eval -= piece.getValue()
                        # if playing as white, negative points for black pieces and positions on board
                        else:
                            if piece.getType() == "pawn":
                                eval += self.pawn_space_player[i][j]
                            elif piece.getType() == "bishop":
                                eval += self.bishop_space_player[i][j]
                            elif piece.getType() == "knight":
                                eval += self.knight_space_player[i][j]
                            elif piece.getType() == "rook":
                                eval += self.rook_space_player[i][j]
                            elif piece.getType() == "queen":
                                eval += self.queen_space_player[i][j]
                            elif piece.getType() == "king":
                                eval += self.king_space_player[i][j]

                            eval += piece.getValue()

        return eval                            
    
    def boardClicker(self, clickedX, clickedY):

        self.getValidMoves()

        # Inverse function to get square coordinates
        x = (clickedX-200)//75
        y = (clickedY//75)

        can_move = False
        selectedMove = None

        if self.piece_selected is not None:
            for piece_move in self.piece_selected.getValidMoves(self):
                if (piece_move.getOPos() == self.piece_selected.getPos()) and (piece_move.getNPos() == (x, y)):

                    for move in self.moves:
                        if (move.getOPos() == piece_move.getOPos()) and (move.getNPos() == piece_move.getNPos()):
                            
                            can_move = True
                            selectedMove = move
                            break

        else:
            for move in self.moves:
                if move.getOPos() == (x, y):
                    can_move = True


        # Iterate throught squares to get square with clicked coordinates
        for square in self.squares:
            if square.getPosition() == (x, y) and (can_move):

                # If there is a piece on that square
                if (square.getPieceOnSquare() is not None) and (self.player_colour == self.turn):

                    # Select a piece
                    if (self.turn == square.getPieceOnSquare().getColour()) and (self.piece_selected is None):
                        self.piece_selected = square.getPieceOnSquare()
                        square.setPieceOnSquare(None)

                    # Capture a piece 
                    elif (self.piece_selected is not None) and (square.getPieceOnSquare().getColour() != self.piece_selected.getColour()):
                        self.movePiece(selectedMove)
                        self.piece_selected = None

                # Move to empty square
                elif (self.player_colour == self.turn) and (self.piece_selected is not None):
                    self.movePiece(selectedMove)
                    self.piece_selected = None

    def drawBoard(self, the_screen):

        # Temporay placeholder for each square
        square = None

        # Draw 64 squares to represent 8x8 board
        for i in range(0, 8):
            for j in range(0,8):
                # Square colour is dependent on the player's colour, board colour and coordinates
                square = Square(self.board_colour, (j, i), self.player_colour)
                # Blit square onto screen with formula
                the_screen.blit(square.getSquare(), ((75*i)+200, (75*j)))
                # Add square to square list
                self.squares.append(square)

        # Draw pieces to the screen by looping through the board
        for i in range(0, 8):
            for j in range(0, 8):
                # Check if a piece is on that square
                if self.board[i][j] != 0:
                    # Blit piece onto screen with formula
                    the_screen.blit(self.board[i][j].getImage(), ((75*j)+200, (75*i)))
                    # Add piece onto corresponding square
                    for s in self.squares:
                        if s.getPosition() == (j,i):
                            s.setPieceOnSquare(self.board[i][j])

    def isInCheck(self):

        king_pos = None
        in_check = False
        moves = []

        # Find king position
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] != 0:
                    if (self.board[i][j].getType() == "king") and (self.board[i][j].getColour() == self.turn):
                        king_pos = (j, i)

        # Flip turn to see opponents move
        piece = None

        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j]!= 0:
                    piece = self.board[i][j]
                    if piece.getColour() != self.turn:
                        moves = piece.getValidMoves(self)
                        # If endpoint for any move is the same position as king, then king is in check
                        for move in moves:
                            if move.getNPos() == king_pos:
                                in_check = True

        return in_check

    def isCheckmate(self):
        self.getValidMoves()

        # If no legal moves
        if (len(self.moves) == 0):
             # and is in check
             if (self.isInCheck() == True):
                # then checkmate
                return True
        # Otherwise false
        else:
            return False

    def isStalemate(self):
        self.getValidMoves()
        is_stalemate = False
        white_pieces = []
        black_pieces = []

        # Clauses for the insufficient material clause
        insufficient_material_scenerios = [
            (['king'], ['king']),
            (['king'], ['king', 'knight']),
            (['king'], ['bishop', 'king']),
            (['bishop', 'king'], ['king', 'knight']),
            (['bishop', 'king'], ['bishop', 'king']),
            (['king', 'knight'], ['king', 'knight'])
        ]

        # If no moves are possible and not in check, then stalemate is true
        if (len(self.moves) == 0):
             if (self.isInCheck() == False):
                is_stalemate = True

        # Get pieces on board
        piece = None
        for i in range(0, 8):
            for j in range(0, 8):
                piece = self.board[i][j]
                if piece != 0:
                    if piece.getColour() == "white":
                        white_pieces.append(piece.getType())
                    else:
                        black_pieces.append(piece.getType())

        temp_w = white_pieces.copy()
        temp_w.sort()
        white_pieces = temp_w
        temp_b = black_pieces.copy()
        temp_b.sort()
        black_pieces = temp_b.copy()

        pieces = (white_pieces, black_pieces)

        # See if current board state matches insufficient material clauses
        for scenerio in insufficient_material_scenerios:
            if (pieces == scenerio) or (pieces == scenerio[::-1]):
                is_stalemate = True


        return is_stalemate

    def getMoves(self):

        # Gets all possible moves for player whos turn it is
        piece = None
        moves = []
        piece_moves = []
        self.moves = []

        for i in range(0, 8):
            for j in range(0, 8):
                piece = self.board[i][j]
                if piece != 0:
                    # Only get moves if piece colour is the same as turn
                    if piece.getColour() == self.turn:
                        # Add every move of that piece onto list
                        piece_moves = piece.getValidMoves(self)
                        for move in piece_moves:
                            moves.append(move)

        return moves

    def getValidMoves(self):
        valid_moves = []
        moves = self.getMoves()

        for move in moves:
                
            # temporaily store positions
            piece_in_n_pos = self.board[move.getNPos()[1]][move.getNPos()[0]]
            piece_in_o_pos = self.board[move.getOPos()[1]][move.getOPos()[0]]

            # replace new position with new piece and old position with 0
            self.board[move.getNPos()[1]][move.getNPos()[0]] = piece_in_o_pos
            self.board[move.getOPos()[1]][move.getOPos()[0]] = 0

            # if board state is not in check add move to list
            if self.isInCheck() == False:
                valid_moves.append(move)

            # return board to original state
            self.board[move.getOPos()[1]][move.getOPos()[0]] = piece_in_o_pos
            self.board[move.getNPos()[1]][move.getNPos()[0]] = piece_in_n_pos

        self.moves = valid_moves

        return self.moves 

    def saveBoard(self):
        # Create blank board
        saved = [[0 for i in range(0, 8)] for j in range(0, 8)]

        piece = None

        # PLace pieces of current board onto saved board
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] != 0:
                    piece = self.board[i][j]
                    saved[i][j] = piece

        # Add saved board to list
        self.previous_board.append(saved)

    def movePiece(self, move):

        # Select piece and set space to blank
        piece = self.board[move.getOPos()[1]][move.getOPos()[0]]
        self.board[move.getOPos()[1]][move.getOPos()[0]] = 0

        # Move piece
        piece.setPos(move.getNPos())
        piece.setMovedTrue()
        self.board[move.getNPos()[1]][move.getNPos()[0]] = piece
        
        # Pawn promotion
        if (piece.getType() == "pawn") and ((piece.getPositionY() == 7) or (piece.getPositionY() == 0)):
            self.board[move.getNPos()[1]][move.getNPos()[0]] = Queen(piece.getColour(), piece.getPositionX(), piece.getPositionY())
        
        # If castle store, rook here
        castled_rook = None

        # Set square to blank
        for square in self.squares:
            if square.getPosition() == move.getOPos():
                square.setPieceOnSquare(None)
 
        # Set piece on square
        for square in self.squares:
            if square.getPosition() == move.getNPos():
                square.setPieceOnSquare(piece)


        # Check for castle and store rook
        if piece.getType() == "king":

            if move.getOPos() == (piece.getPositionX()-2, piece.getPositionY()):
                castled_rook = self.board[move.getNPos()[1]][7]

            elif move.getOPos() == (piece.getPositionX()+2, piece.getPositionY()):
                castled_rook = self.board[move.getNPos()[1]][0]

        # Set rook's square to blank if castled
        if castled_rook is not None:

            self.board[castled_rook.getPositionY()][castled_rook.getPositionX()] = 0
            
            for square in self.squares:
                if square.getPosition() == castled_rook.getPos():
                    square.setPieceOnSquare(None)
                    

            # Place rook on new square if castled
            if castled_rook.getPos() == (7, move.getNPos()[1]):
                castled_rook.setPos((piece.getPositionX()-1, piece.getPositionY()))
                castled_rook.setMovedTrue()
                self.board[piece.getPositionY()][piece.getPositionX()-1] = castled_rook

            else:
                castled_rook.setPos((piece.getPositionX()+1, piece.getPositionY()))
                castled_rook.setMovedTrue()
                self.board[piece.getPositionY()][piece.getPositionX()+1] = castled_rook

            for square in self.squares:
                if square.getPosition() == castled_rook.getPos():
                    square.setPieceOnSquare(castled_rook)


            
        self.turn = "white" if self.turn == "black" else "black"

    def unmakeMove(self):
        # Replace board with previous board and flip turn back
        board = self.previous_board[-1]
        board = self.ascii(board)
        self.setupBoard(board)
        self.previous_board.pop()
        self.turn = "white" if self.turn == "black" else "black"

    def playRandomMove(self):

        self.getValidMoves()
        move = random.choice(self.moves)
        
        self.movePiece(move)
        
    def getBoard(self):
        return self.board

    def getPlayerColour(self):
        return self.player_colour

    def getTurn(self):
        return self.turn

    def getBoardColour(self):
        return self.board_colour

    def ascii(self, board):

        # Decrypt board to ascii characters to 
        ascii = [['.' for i in range(0, 8)] for j in range(0, 8)]
        piece = None

        for i in range(0, 8):
            for j in range(0, 8):
                piece = board[i][j]
                if piece!= 0:
                    if piece.getType() == "pawn":
                        if piece.getColour() == "white":
                            ascii[i][j] = "P"
                        else:
                            ascii[i][j] = "p"
                    if piece.getType() == "knight":
                        if piece.getColour() == "white":
                            ascii[i][j] = "N"
                        else:
                            ascii[i][j] = "n"
                    if piece.getType() == "bishop":
                        if piece.getColour() == "white":
                            ascii[i][j] = "B"
                        else:
                            ascii[i][j] = "b"
                    if piece.getType() == "rook":
                        if piece.getColour() == "white":
                            ascii[i][j] = "R"
                        else:
                            ascii[i][j] = "r"
                    if piece.getType() == "queen":
                        if piece.getColour() == "white":
                            ascii[i][j] = "Q"
                        else:
                            ascii[i][j] = "q"
                    if piece.getType() == "king":
                        if piece.getColour() == "white":
                            ascii[i][j] = "K"
                        else:
                            ascii[i][j] = "k"
        return ascii
