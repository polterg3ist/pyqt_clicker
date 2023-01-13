from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self, app):
        super(Window, self).__init__()

        self.screen = app.primaryScreen()
        self.size = self.screen.size()
        self.clicked = 0
        self.window_title = "AdaptiveClicker"

        self.screen_width = self.size.width()
        self.screen_height = self.size.height()

        self.window_width = 800
        self.window_height = 300

        self.window_start_pos_x = self.screen_width // 2 - self.window_width // 2
        self.window_start_pos_y = self.screen_height // 2 - self.window_height // 2

        self.setWindowTitle(self.window_title)
        self.setGeometry(self.window_start_pos_x, self.window_start_pos_y, self.window_width, self.window_height)

        self.main_text = MainText(self)
        self.button = Button(self)

    def resizeEvent(self, event):
        self.window_width = self.geometry().width()
        self.window_height = self.geometry().height()

        self.main_text.update_pos()
        self.button.update_pos()


class MainText:
    def __init__(self, window):
        self.window = window
        self.main_text = QtWidgets.QLabel(self.window)
        self.main_text.setText(f"Clicks: {self.window.clicked}")
        self.main_text.adjustSize()
        self.main_text_size = self.main_text.size()
        self.main_text_width = self.main_text_size.width()
        self.main_text_height = self.main_text_size.height()
        self.main_text_pos_x = (self.window.window_width - self.main_text_width) // 2
        self.main_text_pos_y = (self.window.window_height - self.main_text_height) // 2
        self.main_text.move(self.main_text_pos_x, self.main_text_pos_y)

    def update_text(self):
        self.main_text.setText(f"Clicks: {self.window.clicked}")
        self.main_text.adjustSize()

    def update_pos(self):
        self.main_text_pos_x = (self.window.window_width - self.main_text_width) // 2
        self.main_text_pos_y = (self.window.window_height - self.main_text_height) // 2
        self.main_text.move(self.main_text_pos_x, self.main_text_pos_y)


class Button:
    def __init__(self, window):
        self.window = window
        self.btn = QtWidgets.QPushButton(self.window)
        self.text = "CLICK ME"
        self.btn.setText(self.text)
        self.btn.setFixedSize(150, 50)
        self.btn_size = self.btn.size()
        self.btn_width = self.btn_size.width()
        self.btn_height = self.btn_size.height()
        self.btn_pos_x = (self.window.window_width - self.btn_width) // 2
        self.btn_pos_y = self.window.main_text.main_text_pos_y + self.window.main_text.main_text_height + 10

        self.btn.move(self.btn_pos_x, self.btn_pos_y)
        self.btn.clicked.connect((self.on_click))

    def update_pos(self):
        self.btn_pos_x = (self.window.window_width - self.btn_width) // 2
        self.btn_pos_y = self.window.main_text.main_text_pos_y + self.window.main_text.main_text_height + 10
        self.btn.move(self.btn_pos_x, self.btn_pos_y)

    def on_click(self):
        self.window.clicked += 1
        self.window.main_text.update_text()


def application():
    app = QApplication(sys.argv)
    window = Window(app)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

