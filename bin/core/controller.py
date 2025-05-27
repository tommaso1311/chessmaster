from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtGui import QAction

from bin.core.chess_game import ChessGame

from bin.ui.main_window import MainWindow
from bin.ui.chess_board import ChessBoardWidget

class Controller:
    def __init__(self, args):
        # Core
        self.chess_game = None # will be initialized when loading a PGN file
        empty_board_svg = ChessGame.get_empty_board_svg()
        
        # UI - Main Window
        self.app = QApplication(args)
        self.main_window = MainWindow(svg_data=empty_board_svg)
        self.create_menu_bar()

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
        self.main_window.refresh_chessboard_widget(svg)

    def runapp(self):
        self.main_window.show()
        self.app.exec()
