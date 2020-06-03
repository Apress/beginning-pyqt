"""
Listing 5-4
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStatusBar, QAction, 
    QTextEdit, QToolBar, QDockWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class BasicMenu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 350, 350) # x, y, width, height 
        self.setWindowTitle('Basic Menu Example 2')

        # set central widget for main window
        self.setCentralWidget(QTextEdit())

        self.createMenu()
        self.createToolBar()
        self.createDockWidget()

        self.show()

    def createMenu(self):
        """
        Create menu bar and menu actions
        """
        # Create actions for file menu
        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        # Create actions for view menu
        full_screen_act = QAction('Full Screen', self, checkable=True)
        full_screen_act.setStatusTip('Swtich to full screen mode')
        full_screen_act.triggered.connect(self.switchToFullScreen)

        # Create menubar 
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)

        # Create view menu, Appearance submenu and add actions 
        view_menu = menu_bar.addMenu('View')
        appearance_submenu = view_menu.addMenu('Appearance')
        appearance_submenu.addAction(full_screen_act)

        # Display info about tools, menu, and view in the statusbar
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        """
        Create toolbar for GUI
        """
        # set up toolbar
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        # Add actions to toolbar
        tool_bar.addAction(self.exit_act)

    def createDockWidget(self):
        """
        Create dock widget
        """
        # set up dock widget
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)

        # set main widget for the dock widget
        dock_widget.setWidget(QTextEdit())

        # set initial location of dock widget in main window
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def switchToFullScreen(self, state):
        """
        If state is True, then display the main window in full screen.
        Otherwise, return the the window to normal.
        """
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())
