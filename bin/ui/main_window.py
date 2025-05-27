from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from bin.constants import MAIN_WINDOW_TITLE, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT
from bin.ui.chess_board import ChessBoardWidget
from bin.ui.pgn_viewer import PgnViewerWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # Initialize the main window with a title, a size, and a menu bar
        super().__init__(parent)
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.resize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)

        # Set up the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        # Create and add the chess board widget to the layout
        self.chess_board_widget = ChessBoardWidget()
        layout.addWidget(self.chess_board_widget, stretch=2)

        # Create and add the PGN viewer widget to the layout
        self.pgn_viewer_widget = PgnViewerWidget()
        layout.addWidget(self.pgn_viewer_widget, stretch=1)

    def refresh_chessboard_widget(self, svg_data):
        self.chess_board_widget.load_from_svg(svg_data)

    def refresh_pgn_viewer_widget(self, moves, highlighted_move):
        self.pgn_viewer_widget.load_moves_from_list(moves, highlighted_move)
