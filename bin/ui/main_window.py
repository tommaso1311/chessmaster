from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

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
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Create and add the chess board widget to the left
        self.chess_board_widget = ChessBoardWidget()
        main_layout.addWidget(self.chess_board_widget, stretch=2)

        # Create and add the PGN viewer widget to the right
        right_container = QWidget()
        right_layout = QVBoxLayout()
        right_container.setLayout(right_layout)

        # Buttons
        self.prev_button = QPushButton("←")
        self.next_button = QPushButton("→")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        right_layout.addLayout(button_layout)

        # PGN Viewer
        self.pgn_viewer_widget = PgnViewerWidget()
        right_layout.addWidget(self.pgn_viewer_widget, stretch=1)

        main_layout.addWidget(right_container, stretch=1)

        # Connect buttons to slots (you'll implement these)
        self.prev_button.clicked.connect(self.prev_move)
        self.next_button.clicked.connect(self.next_move)

    def refresh_chessboard_widget(self, svg_data):
        self.chess_board_widget.load_from_svg(svg_data)

    def refresh_pgn_viewer_widget(self, moves, highlighted_move):
        self.pgn_viewer_widget.load_moves_from_list(moves, highlighted_move)

    def prev_move(self):
        print("Previous move button clicked")
    
    def next_move(self):
        print("Next move button clicked")
