import chess
import chess.svg

class ChessGame:
    def __init__(self):
        self._board = chess.Board()

    def load_game(self, game):
        self._board = game.board()

    def reset(self):
        self._board.reset()

    def move_san(self, move):
        self.board.push_san(move)

    def move_uci(self, move):
        self.board.push_uci(move)
    
    def get_svg(self):
        return chess.svg.board(board=self._board)
