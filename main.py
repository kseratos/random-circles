import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI import UIMainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class RandomCircles(QMainWindow, UIMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.circles = []  # Список для хранения информации о всех окружностях
        self.pushButton.clicked.connect(self.paint_random_circle)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for circle in self.circles:
            x, y, radius, color = circle
            qp.setBrush(color)
            qp.drawEllipse(x, y, radius, radius)
        qp.end()

    def paint_random_circle(self):
        x = random.randint(0, self.WIDTH)
        y = random.randint(0, self.LENGTH)
        radius = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()
    sys.exit(app.exec())
