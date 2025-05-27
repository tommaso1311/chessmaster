from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget

class PgnViewerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

    def load_moves(self, moves: list[str]):
        self.list_widget.clear()
        self.list_widget.addItems(moves)
