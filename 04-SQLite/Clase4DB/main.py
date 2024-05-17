from PyQt6.QtWidgets import QApplication, QWidget
import sys

class VentanaVacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle("Mi primera ventana")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVacia()
    sys.exit(app.exec())