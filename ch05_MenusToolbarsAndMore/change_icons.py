"""
Listing 5-2
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
    QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import random

class ChangeIcon(QWidget):

    def __init__(self):
        super().__init__()

        self.initializezUI()

    def initializezUI(self):
        self.setGeometry(100, 100, 200, 200) 
        self.setWindowTitle('Set Icons Example')
        self.setWindowIcon(QIcon('images/pyqt_logo.png'))

        self.createWidgets()

        self.show()

    def createWidgets(self):
        """
        Set up widgets.
        """
        info_label = QLabel("Click on the button and select a fruit.") 

        self.images = [
            "images/1_apple.png", "images/2_pineapple.png",
            "images/3_watermelon.png", "images/4_banana.png"
        ]

        self.icon_button = QPushButton(self)
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))
        self.icon_button.clicked.connect(self.changeButtonIcon)

        # create vertical layout and add widgets
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)

        # set main layout of window
        self.setLayout(v_box) 

    def changeButtonIcon(self):
        """
        When the button is clicked, change the icon to one of the
        images in the list. 
        """
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60, 60))

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    window = ChangeIcon() 
    sys.exit(app.exec_())