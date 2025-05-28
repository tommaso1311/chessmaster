from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QPushButton
from PySide6.QtCore import Qt
from itertools import zip_longest

from bin.constants import HIGHLIGHT_BACKGROUND_COLOR, HIGHTLIGHT_FOREGROUND_COLOR

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
        self.table_widget = self.create_empty_table(n_rows=0)

        layout.addWidget(self.table_widget)

    def create_empty_table(self, n_rows):
        table_widget = NonInteractiveTableWidget()

        # Disable focus, editing, and scrollbar
        table_widget.setFocusPolicy(Qt.NoFocus)
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Disattiva completamente la selezione
        table_widget.setSelectionMode(QAbstractItemView.NoSelection)

        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["White", "Black"])

        # Horizontal header
        header_h = table_widget.horizontalHeader()
        header_h.setStretchLastSection(True)
        header_h.setSectionResizeMode(QHeaderView.Fixed)
        header_h.setSectionsClickable(False)
        
        # Vertical header
        header_v = table_widget.verticalHeader()
        header_v.setMinimumWidth(25)
        header_v.setSectionResizeMode(QHeaderView.Fixed)
        header_v.setSectionsClickable(False)

        return table_widget

    def load_moves_from_list(self, moves, highlighted_move):
        # Set the number of rows and columns based on white moves
        white_moves = moves[0::2]
        black_moves = moves[1::2]
        num_rows = len(white_moves)

        # Set the table rows
        self.table_widget.setRowCount(num_rows)
        
        for row in range(num_rows):
            header_item = QTableWidgetItem(f"{row + 1}.")
            header_item.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setVerticalHeaderItem(row, header_item)

        for row, zipped_moves in enumerate(zip_longest(white_moves, black_moves, fillvalue="")):
            for i, move in enumerate(zipped_moves):
                move_item = QTableWidgetItem(move)
                move_item.setFlags(move_item.flags() & ~Qt.ItemIsEditable)
                self.table_widget.setItem(row, i, move_item)

        # Highlight the specified move
        if highlighted_move is not None:
            self.highlight_move(highlighted_move)

    def highlight_move(self, highlighted_move):
        num_rows = self.table_widget.rowCount()
        highlighted_row = highlighted_move // 2 if highlighted_move < num_rows * 2 else -1
        highlighted_col = 0 if highlighted_move % 2 == 0 else 1
        highlighted_item = self.table_widget.item(highlighted_row, highlighted_col)

        if highlighted_item:
            highlighted_item.setBackground(HIGHLIGHT_BACKGROUND_COLOR)
            highlighted_item.setForeground(HIGHTLIGHT_FOREGROUND_COLOR)

class PgnNavigationButtonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)

        self.prev_button = QPushButton("←")
        self.next_button = QPushButton("→")

        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
