import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from bin.ui.chessboard import ChessboardWidget
from bin.logic.chess_engine import ChessGame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chessmaster")

        self.game = ChessGame()
        self.widget = ChessboardWidget()

        self.setCentralWidget(self.widget)
        self.refresh_view()

    def refresh_view(self):
        svg = self.game.get_svg()
        self.widget.update_from_svg(svg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec())
