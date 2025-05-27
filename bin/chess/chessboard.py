from PySide6.QtWidgets import QWidget
from PySide6.QtSvgWidgets import QSvgWidget
import os

from bin.constants import ASSETS_FOLDER, CHESSBOARD_SVG

class ChessBoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Percorso al file SVG
        svg_path = os.path.join(ASSETS_FOLDER, CHESSBOARD_SVG)

        # Crea un widget SVG e carica il file
        self.svg_widget = QSvgWidget(svg_path, self)
        self.svg_widget.setGeometry(0, 0, 600, 600)  # o usa layout più avanti
