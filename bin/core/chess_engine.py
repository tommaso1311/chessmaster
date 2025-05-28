import chess.engine

from bin.constants import ENGINE_TIME_LIMIT

class ChessEngine:
    def __init__(self, engine_path):
        try:
            self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Engine not found at {engine_path}. Please ensure the engine is installed.")

        self._is_enabled = False

    def toggle_engine(self, enabled):
        self._is_enabled = enabled

    def get_best_move(self, board, time_limit=ENGINE_TIME_LIMIT):
        if self._is_enabled:
            time_limit = chess.engine.Limit(time=ENGINE_TIME_LIMIT)
            result = self.engine.play(board, time_limit)
            move_san = board.san(result.move)
            return move_san
        else:
            return "N/A"

    def shutdown(self):
        if self.engine:
            self.engine.quit()
            self.engine = None
        else:
            raise RuntimeError("Engine is not running or has already been shut down.")
    