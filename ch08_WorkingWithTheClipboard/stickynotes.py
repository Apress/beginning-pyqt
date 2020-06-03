"""
Listing 8-2
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, 
    QTextEdit)
from PyQt5.QtCore import QSize

class StickyNotes(QMainWindow):
    # static variables
    note_id = 1 
    notes = []

    def __init__(self, note_ref=str()):
        super().__init__()
        self.note_ref = note_ref
        StickyNotes.notes.append(self)

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setMinimumSize(QSize(250, 250))
        self.setWindowTitle("8.1 - Sticky Notes GUI")

        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)

        self.createMenu()
        self.createClipboard()

        self.show()

    def createMenu(self):
        """
        Create simple menu bar and menu actions
        """
        # Create actions for the file menu
        self.new_note_act = QAction('New Note', self)
        self.new_note_act.setShortcut('Ctrl+N')
        self.new_note_act.triggered.connect(self.newNote)

        self.close_act = QAction('Clear', self)
        self.close_act.setShortcut('Ctrl+W')
        self.close_act.triggered.connect(self.clearNote)

        self.quit_act = QAction('Quit', self)
        self.quit_act.setShortcut('Ctrl+Q')
        self.quit_act.triggered.connect(self.close)

        # Create actions for the color menu
        self.yellow_act = QAction('Yellow', self)
        self.yellow_act.triggered.connect(lambda: self.changeBackground(self.yellow_act.text()))

        self.blue_act = QAction('Blue', self)
        self.blue_act.triggered.connect(lambda: self.changeBackground(self.blue_act.text()))

        self.green_act = QAction('Green', self)
        self.green_act.triggered.connect(lambda: self.changeBackground(self.green_act.text()))

        # Create actions for the paste menu
        self.paste_act = QAction('Paste', self)
        self.paste_act.setShortcut('Ctrl+V')
        self.paste_act.triggered.connect(self.pasteToClipboard)

        # Create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False) # Uncomment to display menu in window on MacOS

        # Create file menu and add actions 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.new_note_act)
        file_menu.addAction(self.close_act)
        file_menu.addAction(self.quit_act)

        # Create color menu and add actions 
        file_menu = menu_bar.addMenu('Color')
        file_menu.addAction(self.yellow_act)
        file_menu.addAction(self.blue_act)
        file_menu.addAction(self.green_act)

        # Create paste menu and add actions 
        file_menu = menu_bar.addMenu('Paste')
        file_menu.addAction(self.paste_act)

    def createClipboard(self):
        """
        Set up clipboard. 
        """
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copyToClipboard)

    def newNote(self):
        """
        Create new instance of StickyNotes class.
        """
        self.note_ref = str("note_%d" % StickyNotes.note_id)
        StickyNotes().show()
        StickyNotes.note_id += 1

    def clearNote(self):
        """
        Delete the current note's text.
        """
        self.central_widget.clear() 

    def copyToClipboard(self):
        """
        Get the contents of the system clipboard.
        """
        return self.clipboard.text()

    def pasteToClipboard(self):
        """
        Get the contents of the system clipboard and paste
        into the note. 
        """
        text = self.copyToClipboard()
        self.central_widget.insertPlainText(text + '\n')

    def changeBackground(self, color_text):
        """
        Change a note's background color.
        """
        if color_text == "Yellow":
            self.central_widget.setStyleSheet("background-color: rgb(248, 253, 145)")
        elif color_text == "Blue":
            self.central_widget.setStyleSheet("background-color: rgb(145, 253, 251)")
        elif color_text == "Green":
            self.central_widget.setStyleSheet("background-color: rgb(148, 253, 145)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyNotes()
    sys.exit(app.exec_())
