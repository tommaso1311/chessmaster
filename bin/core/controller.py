from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtGui import QAction

from bin.core.chess_game import ChessGame

from bin.ui.main_window import MainWindow
from bin.ui.chess_board import ChessBoardWidget

class Controller:
    def __init__(self, args):
        # Core
        self.chess_game = ChessGame(game=None) # empty game
        empty_svg_data = self.chess_game.get_svg() # empty chessboard
        empty_move_set = self.chess_game.get_moves_list() # empty move set

        # UI - Main Window
        self.app = QApplication(args)
        self.main_window = MainWindow()
        self.create_menu_bar()

        self.main_window.refresh_chessboard_widget(empty_svg_data)
        self.main_window.refresh_pgn_viewer_widget(empty_move_set, highlighted_move=None)

    def create_menu_bar(self):
        menubar = self.main_window.menuBar()
        file_menu = menubar.addMenu("File")

        # File Menu
        load_game_from_pgn_action = QAction("Load game (.pgn)", self.main_window)
        load_game_from_pgn_action.triggered.connect(self.load_game_from_pgn)
        file_menu.addAction(load_game_from_pgn_action)

    def load_game_from_pgn(self):
        pgn_filename, _ = QFileDialog.getOpenFileName(self.main_window, "Load PGN file", "", "PGN file (*.pgn)")
        if not pgn_filename:
            return

        self.chess_game = ChessGame.from_pgn_file(pgn_filename)
        svg = self.chess_game.get_svg()
        moves = self.chess_game.get_moves_list()

        self.main_window.refresh_chessboard_widget(svg)
        self.main_window.refresh_pgn_viewer_widget(moves, highlighted_move=0)

    def runapp(self):
        self.main_window.show()
        self.app.exec()
