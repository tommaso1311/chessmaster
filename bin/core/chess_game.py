import chess
import chess.svg
import chess.pgn

class ChessGame:
    def __init__(self, game):
        self._game = game

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

    @classmethod
    def from_pgn_file(cls, pgn_filename):
        with open(pgn_filename, "r") as pgn_file:
            game = chess.pgn.read_game(pgn_file)
        return cls(game=game)

    def get_svg(self):
        return chess.svg.board(board=self._game.board())

    def get_moves_list(self):
        moves = []
        temp_board = self._game.board()
        for move in self._game.mainline_moves():
            moves.append(temp_board.san(move))
            temp_board.push(move)
        return moves