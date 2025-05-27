from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from itertools import zip_longest

class NonInteractiveTableWidget(QTableWidget):
    def mousePressEvent(self, event):
        pass

    def keyPressEvent(self, event):
        pass

    def mouseDoubleClickEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

class PgnViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        self.table_widget = NonInteractiveTableWidget()
        layout.addWidget(self.table_widget)

    def load_moves_from_list(self, moves, highlighted_move=0):
        self.table_widget.clear()
        self.table_widget.setFocusPolicy(Qt.NoFocus)
        # self.table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Set the number of rows and columns based on white moves
        white_moves = moves[0::2]
        black_moves = moves[1::2]
        num_rows = len(white_moves)

        # Set the table dimensions
        self.table_widget.setRowCount(num_rows)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["White", "Black"])
        self.table_widget.verticalHeader().setMinimumWidth(25)
        self.table_widget.horizontalHeader().setStretchLastSection(True)

        for row in range(num_rows):
            header_item = QTableWidgetItem(f"{row + 1}.")
            header_item.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setVerticalHeaderItem(row, header_item)

        for row, zipped_moves in enumerate(zip_longest(white_moves, black_moves, fillvalue="")):
            for i, move in enumerate(zipped_moves):
                move_item = QTableWidgetItem(move)
                move_item.setFlags(move_item.flags() & ~Qt.ItemIsEditable)
                self.table_widget.setItem(row, i, move_item)

        highlighted_row = highlighted_move // 2 if highlighted_move < len(moves) else -1
        highlighted_col = 0 if highlighted_move % 2 == 0 else 1
        highlighted_item = self.table_widget.item(highlighted_row, highlighted_col)
        if highlighted_item:
            self.table_widget.setCurrentCell(highlighted_row, highlighted_col)
