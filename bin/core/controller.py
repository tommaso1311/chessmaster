from PySide6.QtWidgets import QApplication, QFileDialog
# from PySide6.QtGui import QAction

from bin.core.chess_game import ChessGame

from bin.ui.main_window import MainWindow
from bin.ui.chess_board import ChessBoardWidget

class Controller:
    def __init__(self, args):
        # Core
        self.chess_game = ChessGame(game=None) # empty game
        empty_svg_data = self.chess_game.get_svg() # empty chessboard
        # empty_move_set = self.chess_game.get_san_moves_list() # empty move set

        # UI - Main Window
        self.app = QApplication(args)
        self.main_window = MainWindow()

        # UI - Menu Bar
        self.main_window.load_game_from_pgn_action.triggered.connect(self.load_game_from_pgn)

        # UI - Buttons
        self.main_window.prev_button.clicked.connect(self.prev_move)
        self.main_window.next_button.clicked.connect(self.next_move)

        # UI - Widgets Refresh
        self.main_window.refresh_chessboard_widget(empty_svg_data)
        self.main_window.refresh_pgn_viewer_widget(self.chess_game.san_moves_list, highlighted_move=None)

    def load_game_from_pgn(self):
        pgn_filename, _ = QFileDialog.getOpenFileName(self.main_window, "Load PGN file", "", "PGN file (*.pgn)")
        if not pgn_filename:
            return

        self.chess_game = ChessGame.from_pgn_file(pgn_filename)

        if self.chess_game.san_moves_list:
            print("Loading first move!")
            self.chess_game.move_forward()

        self.main_window.refresh_chessboard_widget(self.chess_game.get_svg())
        self.main_window.refresh_pgn_viewer_widget(self.chess_game.san_moves_list, highlighted_move=self.chess_game.current_move_index)

    def runapp(self):
        self.main_window.show()
        self.app.exec()

    def prev_move(self):
        self.chess_game.move_backward()
        self.main_window.refresh_chessboard_widget(self.chess_game.get_svg())
        self.main_window.refresh_pgn_viewer_widget(self.chess_game.san_moves_list, highlighted_move=self.chess_game.current_move_index)
        
        print(f"Current move index: {self.chess_game.current_move_index}")
        
    def next_move(self):
        self.chess_game.move_forward()
        self.main_window.refresh_chessboard_widget(self.chess_game.get_svg())
        self.main_window.refresh_pgn_viewer_widget(self.chess_game.san_moves_list, highlighted_move=self.chess_game.current_move_index)
        print(f"Current move index: {self.chess_game.current_move_index}")