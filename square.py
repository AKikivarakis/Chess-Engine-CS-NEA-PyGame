import pygame

class Square():

    def __init__(self, board_colour, square_pos, player_colour):

        # Load and scale up squares
        square_brown_dark = pygame.image.load('/images/square brown dark_1x.png').convert_alpha()
        square_brown_dark = pygame.transform.scale(square_brown_dark, (75, 75))
        square_brown_light = pygame.image.load('/images/square brown light_1x.png').convert_alpha()
        square_brown_light = pygame.transform.scale(square_brown_light, (75, 75))
        square_gray_dark = pygame.image.load('/images/square gray dark _1x.png').convert_alpha()
        square_gray_dark = pygame.transform.scale(square_gray_dark, (75, 75))
        square_gray_light = pygame.image.load('/images/square gray light _1x.png').convert_alpha()
        square_gray_light = pygame.transform.scale(square_gray_light, (75, 75))

        # Square position
        self.x = square_pos[0]
        self.y = square_pos[1]
        self.pos = square_pos

        if ((self.x % 2 == self.y % 2) and (player_colour == 'white'))  or ((self.x % 2 != self.y % 2) and (player_colour == 'black')):
            # Is light if sum of both coordinates are even and colour is white, or if sum is odd and colour is black
            if board_colour == "brown":
                self.square = square_brown_light
            elif board_colour == "gray":
                self.square = square_gray_light

        else:
            # Otherwise is dark
            if board_colour == "brown":
                self.square = square_brown_dark
            elif board_colour == "gray":
                self.square = square_gray_dark      

        self.piece_on_square = None

    def getSquare(self):
        return self.square

    def getPosition(self):
        return self.pos

    def getPieceOnSquare(self):
        return self.piece_on_square

    def setPieceOnSquare(self, piece):

        self.piece_on_square = piece
        
