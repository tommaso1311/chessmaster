from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import QByteArray

class ChessboardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.svg_widget = QSvgWidget()
        self.layout.addWidget(self.svg_widget)

    def update_from_svg(self, svg_data):
        self.svg_widget.load(QByteArray(svg_data.encode('utf-8')))
