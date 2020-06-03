"""
Listing 5-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction)

class BasicMenu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 350, 350) # x, y, width, height
        self.setWindowTitle('Basic Menu Example')

        self.createMenu()

        self.show()

    def createMenu(self):
        """
        Create skeleton with menu bar
        """
        # Create actions for file menu
        exit_act = QAction('&Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        # Create menubar 
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BasicMenu()
    sys.exit(app.exec_())
