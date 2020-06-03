"""
Listing 4-2
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
    QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont

class DisplaySurvey(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('4.2 – Survey GUI')
        self.displayWidgets()

        self.show()

    def displayWidgets(self):
        """
        Set up widgets horizontally using QHBoxLayout. 
        """
        # create label and button widgets
        title = QLabel("Restaurant Name")
        title.setFont(QFont('Arial', 17))
        question = QLabel("How would you rate your service today?")

        # create horizontal layouts
        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()

        ratings = ["Not Satisfied", "Average", "Satisfied"]

        # create checkboxes and them to horizontal layout, and stretchable
        # space on both sides of the widgets
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(60) # set spacing between in widgets in horizontal layout

        ratings_h_box.addStretch()
        for rating in ratings:
            rate_label = QLabel(rating, self)
            ratings_h_box.addWidget(rate_label)
        ratings_h_box.addStretch()

        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100) # set spacing between in widgets in horizontal layout
        # Create button group to contain checkboxes
        scale_bg = QButtonGroup(self)

        cb_h_box.addStretch()
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb), self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()

        # check for signal when checkbox is clicked
        scale_bg.buttonClicked.connect(self.checkboxClicked)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close)

        # create vertical layout and add widgets and h_box layouts
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_button)

        # set main layout of the window
        self.setLayout(v_box)

    def checkboxClicked(self, cb):
        """
        Print the text of checkbox selected.
        """
        print("{} Selected.".format(cb.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplaySurvey()
    sys.exit(app.exec_())