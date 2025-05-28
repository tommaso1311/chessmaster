from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PySide6.QtGui import QAction

from bin.constants import MAIN_WINDOW_TITLE, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT
from bin.ui.chess_board import ChessBoardWidget
from bin.ui.pgn_viewer import PgnViewerWidget
from bin.ui.engine_widget import EngineWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # Initialize the main window with a title, a size, and a menu bar
        super().__init__(parent)
        self.setWindowTitle(MAIN_WINDOW_TITLE)
        self.resize(MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT)

        # Create Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # File menu actions
        self.load_game_from_pgn_action = QAction("Load game (.pgn)", self)
        file_menu.addAction(self.load_game_from_pgn_action)

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

        # Stockfish Engine Widget
        self.stockfish_widget = EngineWidget()
        right_layout.addWidget(self.stockfish_widget)

        # PGN Viewer
        self.pgn_viewer_widget = PgnViewerWidget()
        right_layout.addWidget(self.pgn_viewer_widget)

        # Buttons
        self.prev_button = QPushButton("←")
        self.next_button = QPushButton("→")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)

        right_layout.addLayout(button_layout)

        main_layout.addWidget(right_container, stretch=1)

    def refresh_chessboard_widget(self, svg_data):
        self.chess_board_widget.load_from_svg(svg_data)

    def refresh_pgn_viewer_widget(self, moves, highlighted_move):
        self.pgn_viewer_widget.load_moves_from_list(moves, highlighted_move)

    def refresh_engine_widget(self, best_move):
        self.stockfish_widget.best_move_label.setText(f"Best move: {best_move}")
        self.stockfish_widget.engine_button.setChecked(best_move != "N/A")
