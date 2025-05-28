import chess
import chess.svg
import chess.pgn

from bin.constants import EMPTY_BOARD_FEN

class ChessGame:
    def __init__(self, game=None):
        # Initialize the game with a provided PGN game or create an empty game
        if game is None:
            game = self._create_empty_game()
        self.game = game
        self.board = self.game.board()
        self.san_moves_list = self._get_san_moves_list()

        self.current_move_index = -1

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
        return chess.svg.board(board=self.board)

    def _get_san_moves_list(self):
        moves = []
        board = self.game.board()
        for move in self.game.mainline_moves():
            moves.append(board.san(move))
            board.push(move)
        return tuple(moves)
    
    def move_forward(self):
        if self.current_move_index < len(self.san_moves_list) - 1:
            self.current_move_index += 1
            move = self.san_moves_list[self.current_move_index]
            self.board.push_san(move)
            return move
        return None
    
    def move_backward(self):
        if self.current_move_index > 0:
            move = self.san_moves_list[self.current_move_index - 1]
            self.board.pop()
            self.current_move_index -= 1
            return move
        return None
