"""
Listing 12-3
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
    QFrame, QVBoxLayout)
from PyQt5.QtCore import Qt, QDateTime, QDate, QTime, QTimer

class DisplayTime(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setGeometry(100, 100, 250, 100)
        self.setWindowTitle('12.3 – QDateTime Example')
        self.setStyleSheet("background-color: black")

        self.setupWidgets()

        # Create timer object
        timer = QTimer(self)
        timer.timeout.connect(self.updateDateTime)
        timer.start(1000) 

        self.show()

    def setupWidgets(self):
        """
        Set up labels that will display current date and time. 
        """
        current_date, current_time = self.getDateTime()

        self.date_label = QLabel(current_date)
        self.date_label.setStyleSheet("color: white; font: 16px Courier")
        self.time_label = QLabel(current_time)
        self.time_label.setStyleSheet("""color: white;
                                         border-color: white;
                                         border-width: 2px; 
                                         border-style: solid;
                                         border-radius: 4px;
                                         padding: 10px; 
                                         font: bold 24px Courier""")

        # Create layout and add widgets
        v_box = QVBoxLayout()
        v_box.addWidget(self.date_label, alignment=Qt.AlignCenter)
        v_box.addWidget(self.time_label, alignment=Qt.AlignCenter)

        self.setLayout(v_box)
    
    def getDateTime(self):
        """
        Returns current date and time. 
        """
        date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)

        time = QTime.currentTime().toString("hh:mm:ss AP")
        return date, time

    def updateDateTime(self):
        """
        Slot that updates date and time values. 
        """
        date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        time = QTime.currentTime().toString("hh:mm:ss AP")

        self.date_label.setText(date)
        self.time_label.setText(time)
        return date, time

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayTime()
    sys.exit(app.exec_())