"""
Listing 12-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileSystemModel,
    QTreeView, QFrame, QAction, QFileDialog, QVBoxLayout)

class DisplayDirectory(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setMinimumSize(500, 400)
        self.setWindowTitle('12.1 – View Directory GUI')

        self.createMenu()
        self.setupTree()

        self.show()

    def createMenu(self):
        """
        Set up the menu bar.
        """
        open_dir_act = QAction('Open Directory...', self)
        open_dir_act.triggered.connect(self.chooseDirectory)

        root_act = QAction("Return to Root", self)
        root_act.triggered.connect(self.returnToRootDirectory)

        # Create menubar
        menu_bar = self.menuBar()
        #menu_bar.setNativeMenuBar(False) # uncomment for macOS

        # Create file menu and add actions 
        dir_menu = menu_bar.addMenu('Directories')
        dir_menu.addAction(open_dir_act)
        dir_menu.addAction(root_act)

    def setupTree(self):
        """
        Set up the QTreeView so that it displays the contents 
        of the local filesystem. 
        """
        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree = QTreeView()
        self.tree.setIndentation(10)
        self.tree.setModel(self.model)

        # Set up container and layout 
        frame = QFrame()
        frame_v_box = QVBoxLayout()
        frame_v_box.addWidget(self.tree)
        frame.setLayout(frame_v_box)

        self.setCentralWidget(frame)

    def chooseDirectory(self):
        """
        Select a directory to display.
        """
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.Directory)
        directory = file_dialog.getExistingDirectory(self, "Open Directory", 
                "", QFileDialog.ShowDirsOnly)

        self.tree.setRootIndex(self.model.index(directory))

    def returnToRootDirectory(self):
        """
        Re-display the contents of the root directory. 
        """
        self.tree.setRootIndex(self.model.index(''))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplayDirectory()
    sys.exit(app.exec_())