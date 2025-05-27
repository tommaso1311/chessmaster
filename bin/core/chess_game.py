import chess
import chess.svg

class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    # def load_game(self, game):
    #     self._board = game.board()

    # def reset(self):
    #     self._board.reset()

    # def move_san(self, move):
    #     self.board.push_san(move)

    # def move_uci(self, move):
    #     self.board.push_uci(move)
    
    @staticmethod
    def get_empty_board_svg():
        empty_board = chess.Board(None)
        empty_board_svg = chess.svg.board(board=empty_board)
        return empty_board_svg

    def get_svg(self):
        return chess.svg.board(board=self._board)
