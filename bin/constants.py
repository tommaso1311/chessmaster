from PySide6.QtCore import Qt
import platform
import os

system = platform.system()

MAIN_WINDOW_TITLE = 'Chessmaster'
MAIN_WINDOW_WIDTH = 800
MAIN_WINDOW_HEIGHT = 600

HIGHLIGHT_BACKGROUND_COLOR = Qt.yellow
HIGHTLIGHT_FOREGROUND_COLOR = Qt.black

EMPTY_BOARD_FEN = '8/8/8/8/8/8/8/8 w - - 0 1'

ENGINES_FOLDER = 'engines'
CHESS_MASTER_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINES_FOLDER_PATH = os.path.join(CHESS_MASTER_PATH, ENGINES_FOLDER)

STOCKFISH_ENGINE = {
    # 'Windows': 'stockfish-windows-x86-64-avx2.exe',
    'Linux': 'stockfish/stockfish-ubuntu-x86-64-avx2',
    # 'Darwin': 'stockfish-mac-x86-64'
}[system]
STOCKFISH_ENGINE_PATH = os.path.join(ENGINES_FOLDER_PATH, STOCKFISH_ENGINE)

ENGINE_TIME_LIMIT = 0.1  # seconds