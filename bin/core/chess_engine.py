import os
import requests
import zipfile
import io
import chess.engine

from bin.constants import ENGINES_FOLDER_PATH, STOCKFISH_ENGINE_PATH

class ChessEngine:
    def __init__(self, engine_path):
        try:
            self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Engine not found at {engine_path}. Please ensure the engine is installed.")
