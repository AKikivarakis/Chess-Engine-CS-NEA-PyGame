import random

class AI ():

    def __init__(self, depth):
        self.depth = depth

    def playRandomMove(self, board):

        # Choose random move and return it

        moves = board.getValidMoves()

        move = random.choice(moves)
        
        return move

    def minimax(self, depth, board, alpha=-100000000000, beta=100000000000):

        # Break is depth is 0 or game has ended
        if depth == 0 or board.isCheckmate() or board.isStalemate():
            return (-board.evaluate(), None)



        moves = board.getValidMoves()

        if board.turn != board.player_colour: 
            best_move = None
            maxScore = -100000000000

            # Look at every move
            for move in moves:

                board.saveBoard()
                
                # Move a piece and call functioin again
                board.movePiece(move)

                score = self.minimax(depth - 1, board, alpha, beta)

                board.unmakeMove()

                # Calculate alpha
                alpha = max(alpha, score[0])

                # Break if maximising is greater than minimising
                if beta <= alpha:
                    break

                if score[0] >= maxScore:
                    maxScore = score[0]
                    best_move = move

            # Return best move for maximiser
            return (maxScore, best_move)

        else:
            best_move = None
            minScore = 100000000000

            for move in moves:

                board.saveBoard()

                # Move a piece and call functioin again
                board.movePiece(move)

                score = self.minimax(depth - 1, board, alpha, beta)

                board.unmakeMove()
                
                # Calculate beta
                beta = min(beta, score[0])
                
                if score[0] <= minScore:
                    minScore = score[0]
                    best_move = move
                    
                # Break if maximising is greater than minimising
                if beta <= alpha:
                    break
            
            # Return best move for minimiser
            return (minScore, best_move)

    def bestMove(self, board):
        # If depth is 0, then play random move
        if self.depth == 0:
            return self.playRandomMove(board)
        
        # Otherwise play minimax with depth
        else:
            depth = self.depth
            best_move = self.minimax(depth, board)[1]

        return best_move
