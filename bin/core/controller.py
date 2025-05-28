from PySide6.QtWidgets import QApplication, QFileDialog

from bin.core.chess_game import ChessGame
from bin.core.chess_engine import ChessEngine
from bin.constants import STOCKFISH_ENGINE_PATH

from bin.ui.main_window import MainWindow
from bin.ui.chess_board import ChessBoardWidget

class Controller:
    def __init__(self, args):
        # Core - Chess Game
        self.chess_game = ChessGame(game=None) # empty game
        empty_svg_data = self.chess_game.get_svg() # empty chessboard
        
        # Core - Chess Engine
        self.chess_engine = ChessEngine(STOCKFISH_ENGINE_PATH)

        # UI - Main Window
        self.app = QApplication(args)
        self.main_window = MainWindow()

        # UI - Menu Bar
        self.main_window.load_game_from_pgn_action.triggered.connect(self.load_game_from_pgn)

        # UI - Buttons
        self.main_window.pgn_navigation_buttons_widget.prev_button.clicked.connect(self.prev_move)
        self.main_window.pgn_navigation_buttons_widget.next_button.clicked.connect(self.next_move)
        self.main_window.stockfish_widget.engine_button.toggled.connect(self.toggle_engine)

        # UI - Widgets Refresh
        self.refresh_main_window()

    def refresh_main_window(self):
        # get svg data
        svg_data = self.chess_game.get_svg()
        
        # check if is a valid game and highlight current move
        san_moves_list = self.chess_game.san_moves_list
        current_move_index = self.chess_game.current_move_index
        
        # get engine best move
        best_move = self.chess_engine.get_best_move(self.chess_game.board)

        # Refresh UI widgets
        self.main_window.refresh_chessboard_widget(svg_data)
        self.main_window.refresh_pgn_viewer_widget(san_moves_list, highlighted_move=current_move_index)
        self.main_window.refresh_engine_widget(best_move)

    def load_game_from_pgn(self):
        pgn_filename, _ = QFileDialog.getOpenFileName(self.main_window, "Load PGN file", "", "PGN file (*.pgn)")
        if not pgn_filename:
            return

        self.chess_game = ChessGame.from_pgn_file(pgn_filename)
        self.refresh_main_window()

    def prev_move(self):
        self.chess_game.move_backward()
        self.refresh_main_window()
        
    def next_move(self):
        self.chess_game.move_forward()
        self.refresh_main_window()

    def toggle_engine(self):
        if self.chess_game.san_moves_list and self.main_window.stockfish_widget.engine_button.isChecked():
            self.chess_engine.toggle_engine(True)
        else:
            self.chess_engine.toggle_engine(False)
        self.refresh_main_window()

    def runapp(self):
        self.app.aboutToQuit.connect(self.engine_shutdown)

        self.main_window.show()
        self.app.exec()

    def engine_shutdown(self):
        self.chess_engine.shutdown()
