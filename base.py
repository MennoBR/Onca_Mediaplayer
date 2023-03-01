# Base para o Media player / Conversor.

import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QHBoxLayout, QLabel,
    QPushButton, QSlider, QVBoxLayout, QWidget
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtGui import QPixmap

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()

        #Mudando nome window:
        self.setWindowTitle("ONÇA - Media Player")

        # Configurando o media player e playlist:
        self.media_player = QMediaPlayer()
        self.media_player.setVolume(50)
        self.playlist = QMediaPlaylist(self.media_player)
        self.media_player.setPlaylist(self.playlist)

        # Detalhes da GUI:

        self.track_label = QLabel("No track selected")
        self.track_label.setAlignment(Qt.AlignCenter)
        self.track_label.setStyleSheet("QLabel { background-color: grey; color: white; }")

        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.stop_button = QPushButton("Stop")

        hbox = QHBoxLayout()
        hbox.addWidget(self.play_button)
        hbox.addWidget(self.pause_button)
        hbox.addWidget(self.stop_button)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.setTickPosition(QSlider.TicksBothSides)
        self.volume_slider.setTickInterval(10)
        self.volume_slider.valueChanged.connect(self.media_player.setVolume)

        vbox = QVBoxLayout()
        vbox.addWidget(self.track_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.volume_slider)

        self.setLayout(vbox)

        logo_label = QLabel(self)
        pixmap = QPixmap('Icon_black1.jpeg')
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(pixmap.width(), pixmap.height())

        # Conectando os butões ao media player:
        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)

    def play(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open MP3 File", ".", "MP3 Files (*.mp3)")

        if file_name:
            self.playlist.clear()
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.media_player.play()
            self.track_label.setText(file_name)

    def pause(self):
        self.media_player.pause()

    def stop(self):
        self.media_player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MP3Player()
    player.show()
    sys.exit(app.exec_())








