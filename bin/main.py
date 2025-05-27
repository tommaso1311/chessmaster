import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from bin.chess.chessboard import ChessBoardWidget

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Chessmaster")
window.resize(600, 600)

chessboard = ChessBoardWidget()
window.setCentralWidget(chessboard)

window.show()

sys.exit(app.exec())
