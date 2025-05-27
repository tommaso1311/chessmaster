from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from itertools import zip_longest

class PgnViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

    def load_moves_from_list(self, moves):
        self.table_widget.clear()

        # Set the number of rows and columns based on white moves
        white_moves = moves[0::2]
        black_moves = moves[1::2]
        num_rows = len(white_moves)

        # Set the table dimensions
        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["White", "Black"])
        self.table_widget.verticalHeader().setMinimumWidth(20)
        self.table_widget.horizontalHeader().setStretchLastSection(True)

        for row in range(num_rows):
            header_item = QTableWidgetItem(f"{row + 1}.")
            header_item.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setVerticalHeaderItem(row, header_item)

        for row, (w_move, b_move) in enumerate(zip_longest(white_moves, black_moves, fillvalue="")):
            self.table_widget.setItem(row, 0, QTableWidgetItem(w_move))
            self.table_widget.setItem(row, 1, QTableWidgetItem(b_move))
