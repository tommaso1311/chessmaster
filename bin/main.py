import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QAction
import chess.pgn

from bin.ui.chessboard import ChessboardWidget
from bin.logic.chess_game import ChessGame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chessmaster")

        self.game = ChessGame()
        self.chessboard_widget = ChessboardWidget()
        self.setCentralWidget(self.chessboard_widget)

        self._create_menu_bar()
        self.refresh_chessboard()

    def _create_menu_bar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        open_action = QAction("Load game...", self)
        open_action.triggered.connect(self.load_pgn)
        file_menu.addAction(open_action)
    
    def load_pgn(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load PGN file", "", "PGN file (*.pgn)")
        if not filename:
            return

        with open(filename, "r") as pgn_file:
            game = chess.pgn.read_game(pgn_file)
            if game:
                self.game.load_game(game)
                self.refresh_chessboard()

    def refresh_chessboard(self):
        svg = self.game.get_svg()
        self.chessboard_widget.update_from_svg(svg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
