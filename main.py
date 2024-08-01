import pygame
from board import Board
from AI import AI

pygame.init()

# Create Screen
WIDTH = 800
HEIGHT  = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Chess Game")

# function to draw text to the screen
def draw_text(text, font, colour, x_pos, y_pos):
    image = font.render(text, True, colour)
    screen.blit(image, (x_pos, y_pos))

# Create font and text colour
FONT =  pygame.font.SysFont("georgia", 35)
TEXT_COLOUR = (100, 45, 0)

# Keeps game running
running = True

# Intial player colour white and board colour brown
b = Board("brown", "white")

b.setupBoard(None)

# Intial computer level is zero
comp = AI(0)


while running:

    # Draw and fill the screen
    screen.fill((255, 255, 165))
    b.drawBoard(screen)

    # Draw rectangles for buttons
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 200, 75))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 75, 200, 75))
    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect(0, 150, 200, 75))
    pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(0, 225, 200, 75))

    # Draw level difficulty buttons to screen
    draw_text("0", FONT, TEXT_COLOUR, 25, 400)
    draw_text("1", FONT, TEXT_COLOUR, 125, 400)
    draw_text("2", FONT, TEXT_COLOUR, 25, 475)
    draw_text("3", FONT, TEXT_COLOUR, 125, 475)
    draw_text("4", FONT, TEXT_COLOUR, 25, 550)
    draw_text("5", FONT, TEXT_COLOUR, 125, 550)

    clickedX, clickedY = pygame.mouse.get_pos()
        
    # Output winning colour if the board state is checkmate
    if b.isCheckmate():
        if b.getTurn() != "white":
            draw_text("White Wins!", FONT, TEXT_COLOUR, 0, 320)
        else:
            draw_text("Black Wins!", FONT, TEXT_COLOUR, 0, 320)

        b.setupBoard(None)

    # Output Stalemate if board state is stalemate
    if b.isStalemate():
        draw_text("Stalemate!", FONT, TEXT_COLOUR, 0, 320)

        b.setupBoard(None)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()

        if (event.type == pygame.MOUSEBUTTONDOWN):

            if clickedX > 200:


                b.boardClicker(clickedX, clickedY)


            elif clickedY < 75:
                # Change Player Colour to white
                boardColour  = b.getBoardColour()
                b = Board(boardColour, "white")
                b.setupBoard(None)

            elif clickedY < 150:
                # Change Player Colour to black
                boardColour = b.getBoardColour()
                b = Board(boardColour, "black")
                b.setupBoard(None)

            elif clickedY < 225:
                # Change Board Colour to brown
                playerColour = b.getPlayerColour()
                b = Board("brown", playerColour)
                b.setupBoard(None)

            elif clickedY < 300:
                # Change Board Colour to gray
                playerColour = b.getPlayerColour()
                b = Board("gray", playerColour)
                b.setupBoard(None)

            elif clickedY < 450 and clickedX < 100:
                # Random moves
                comp = AI(0)

            elif clickedY < 450 and clickedX < 200:
                # Depth level 1
                comp = AI(1)

            elif clickedY < 525 and clickedX < 100:
                # Depth level 2
                comp = AI(2)
            
            elif clickedY < 525 and clickedX < 200:
                # Depth level 3
                comp = AI(3)

            elif clickedY < 600 and clickedX < 100:
                # Depth level 4
                comp = AI(4)

            elif clickedY < 600 and clickedX < 200:
                # Depth level 5
                comp = AI(5)

    # Computer's move
    if b.getPlayerColour() != b.getTurn():

        move = comp.bestMove(b)

        b.movePiece(move)



    pygame.display.update()
    clock.tick(24)
