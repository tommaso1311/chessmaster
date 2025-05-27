import chess
import chess.svg
import chess.pgn

from bin.constants import EMPTY_BOARD_FEN

class ChessGame:
    def __init__(self, game=None):
        if game is None:
            game = self._create_empty_game()
        self.game = game
    
    @classmethod
    def _create_empty_game(cls):
        empty_board = chess.Board(EMPTY_BOARD_FEN)
        game = chess.pgn.Game()
        game.setup(empty_board)
        return game

    @classmethod
    def from_pgn_file(cls, pgn_filename):
        with open(pgn_filename, "r") as pgn_file:
            game = chess.pgn.read_game(pgn_file)
        return cls(game=game)

    def get_svg(self):
        return chess.svg.board(board=self.game.board())

    def get_moves_list(self):
        moves = []
        temp_board = self.game.board()
        for move in self.game.mainline_moves():
            moves.append(temp_board.san(move))
            temp_board.push(move)
        return moves