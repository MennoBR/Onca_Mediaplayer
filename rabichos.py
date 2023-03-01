#formatações antigas do player:

#vr:01:

'''from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QLabel, QPushButton


class Player(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Configurando a janela:
        self.setWindowTitle('Media Player')
        self.setFixedSize(800, 600)

        # aplicando ícone e background:
        icon = QIcon('Icon_black1.jpeg')
        self.setWindowIcon(icon)

        pixmap = QPixmap('Icon_white1.jpeg')
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.resize(pixmap.width(), pixmap.height())

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # criando a função "Open...":
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        file_menu.addAction(open_action)

        # criando a Toolbar
        toolbar = QToolBar('Playback', self)
        self.addToolBar(Qt.BottomToolBarArea, toolbar)

        play_button = QPushButton('Play', self)
        play_button.setIcon(QIcon('Icon_black1.jpeg'))
        toolbar.addWidget(play_button)

        pause_button = QPushButton('Pause', self)
        pause_button.setIcon(QIcon('Icon_black1.jpeg'))
        toolbar.addWidget(pause_button)

        skip_button = QPushButton('Skip', self)
        skip_button.setIcon(QIcon('Icon_black1.jpeg'))
        toolbar.addWidget(skip_button)

        stop_button = QPushButton('Stop', self)
        stop_button.setIcon(QIcon('Icon_black1.jpeg'))
        toolbar.addWidget(stop_button)

        # Janela
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    player = Player()
    app.exec_()'''
