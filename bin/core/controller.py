from PySide6.QtWidgets import QApplication

from bin.core.chess_game import ChessGame

from bin.ui.main_window import MainWindow
from bin.ui.chess_board import ChessBoardWidget

class Controller:
    def __init__(self, args):
        # Core
        empty_board_svg = ChessGame.get_empty_board_svg()
        self.chess_game = ChessGame()
        
        # UI - Main Window
        self.app = QApplication(args)
        self.main_window = MainWindow(svg_data=empty_board_svg)

        # self.main_window.refresh_chessboard_widget(empty_board_svg)

    # def get_svg(self):
    #     return self.chess_game.get_svg()

    # def refresh_chessboard(self):
    #     svg = self._get_svg()
    #     # self._main_window.setWindowTitle("Chess PGN Viewer")
    #     self._main_window.setCentralWidget(self._chess_game)
    #     self._chess_game.load_from_svg(svg)

    def runapp(self):
        self.main_window.show()
        self.app.exec()
