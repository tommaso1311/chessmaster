# from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

# from bin.ui.chessboard import ChessboardWidget
# from bin.ui.pgn_viewer import PgnViewerWidget

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Chess PGN Viewer")

#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         layout = QHBoxLayout()
#         central_widget.setLayout(layout)

#         # Scacchiera a sinistra
#         self.chessboard = ChessboardWidget()
#         layout.addWidget(self.chessboard, stretch=3)

#         # Visualizzatore PGN a destra
#         self.pgn_viewer = PgnViewerWidget()
#         layout.addWidget(self.pgn_viewer, stretch=2)

#         # Carica mosse di esempio
#         example_moves = [
#             "1. e4 e5",
#             "2. Nf3 Nc6",
#             "3. Bc4 Bc5",
#             "4. c3 Nf6",
#             "5. 1-0"
#         ]
#         self.pgn_viewer.load_moves(example_moves)

#         self._create_menu_bar()
#         self.refresh_chessboard()

#     def _create_menu_bar(self):
#         menubar = self.menuBar()

#         file_menu = menubar.addMenu("File")

#         open_action = QAction("Load game...", self)
#         open_action.triggered.connect(self.load_pgn)
#         file_menu.addAction(open_action)
    
#     def load_pgn(self):
#         filename, _ = QFileDialog.getOpenFileName(self, "Load PGN file", "", "PGN file (*.pgn)")
#         if not filename:
#             return

#         with open(filename, "r") as pgn_file:
#             game = chess.pgn.read_game(pgn_file)
#             if game:
#                 self.game.load_game(game)
#                 self.refresh_chessboard()

#     def refresh_chessboard(self):
#         svg = self.game.get_svg()
#         self.chessboard_widget.update_from_svg(svg)

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from bin.constants import MAIN_WINDOW_TITLE, MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT
from bin.ui.chess_board import ChessBoardWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None, svg_data=None):
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
        layout.addWidget(self.chess_board_widget)

        # Load the initial chessboard SVG
        self.refresh_chessboard_widget(svg_data)

    def refresh_chessboard_widget(self, svg_data):
        self.chess_board_widget.load_from_svg(svg_data)
