import sys


from PyQt5.Qt import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class AppMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(520, 400)

        self.is_painting = False
        self.painter = QPainter(self)
        self.pushButton.clicked.connect(self.paint_circle)

    def paintEvent(self, event):
        if self.is_painting:
            self.painter.begin(self)
            self.painter.setBrush(QColor(255, 204, 0))
            d = randint(10, 150)
            x, y = randint(0, self.width() - d), randint(0, self.height() - d)
            self.painter.drawEllipse(x, y, d, d)
            self.painter.end()
        self.is_painting = False

    def paint_circle(self):
        self.is_painting = True
        self.repaint()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AppMainWindow()
    main_window.show()
    sys.exit(app.exec())
