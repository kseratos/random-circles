from PyQt5.QtWidgets import QMainWindow, QPushButton


class UIMainWindow(object):
    def setupUI(self: QMainWindow):
        self.LENGTH = 800
        self.WIDTH = 600
        self.setGeometry(100, 100, self.LENGTH, self.WIDTH)
        self.setWindowTitle("Git и случайные окружности")
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Сгенерировать окружность")
        self.pushButton.setGeometry(300, 450, 200, 100)