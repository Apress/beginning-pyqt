"""
Listing 4-5
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessart modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
    QLineEdit, QPushButton, QCheckBox, QGridLayout, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ToDoList(QWidget):
    
    def __init__(self): # constructor
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle('4.4 – ToDo List GUI')
        self.setupWidgets()

        self.show()

    def setupWidgets(self):
        """
        Create widgets for to do list GUI and arrange them in window
        """
        # create grid layout
        main_grid = QGridLayout()

        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Arial', 24))
        todo_title.setAlignment(Qt.AlignCenter)

        clear_button = QPushButton("Close")
        clear_button.clicked.connect(self.close)

        # create section labels for to do list
        mustdo_label = QLabel("Must Dos")
        mustdo_label.setFont(QFont('Arial', 20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel("Appointments")
        appts_label.setFont(QFont('Arial', 20))
        appts_label.setAlignment(Qt.AlignCenter)

        # create must do section 
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)

        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)
        
        # create checkboxes and line edit widgets
        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setChecked(False)
            linedit = QLineEdit()
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)

        # create labels for appointments section
        morning_label = QLabel("Morning")
        morning_label.setFont(QFont('Arial', 16))
        morning_entry = QTextEdit()
        noon_label = QLabel("Noon")
        noon_label.setFont(QFont('Arial', 16))
        noon_entry = QTextEdit()
        evening_label = QLabel("Evening")
        evening_label.setFont(QFont('Arial', 16))
        evening_entry = QTextEdit()

        # create vertical layout and add widgets
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)

        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(morning_label)
        appt_v_box.addWidget(morning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)

        # add other layouts to main grid layout
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        main_grid.addWidget(clear_button, 2, 0, 1, 2)
        
        self.setLayout(main_grid)            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())