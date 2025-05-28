from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel

class EngineWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        self.engine_button = QPushButton("Enable Stockfish")
        self.engine_button.setCheckable(True)
        self.best_move_label = QLabel("Best move: N/A")
        
        layout.addWidget(self.engine_button)
        layout.addWidget(self.best_move_label)
        layout.addStretch()
    
    def set_best_move(self, best_move):
        self.best_move_label.setText(f"Best move: {best_move}")