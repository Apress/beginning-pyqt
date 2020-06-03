"""
Listing 5-3
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
#import necessary modules 
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenu, QAction, 
    QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog,
    QColorDialog)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt

class Notepad(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('5.1 – Rich Text Notepad GUI')
        self.createNotepadWidget()
        self.notepadMenu()

        self.show()

    def createNotepadWidget(self):
        """
        Set the central widget for QMainWindow, which is the QTextEdit
        widget for the notepad.
        """
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)

    def notepadMenu(self):
        """
        Create menu for notepad GUI
        """
        # Create actions for file menu
        new_act = QAction(QIcon('images/new_file.png'), 'New', self)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clearText)

        open_act = QAction(QIcon('images/open_file.png'), 'Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openFile)

        save_act = QAction(QIcon('images/save_file.png'), 'Save', self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveToFile)

        exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        # Create actions for edit menu
        undo_act = QAction(QIcon('images/undo.png'),'Undo', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.text_field.undo)

        redo_act = QAction(QIcon('images/redo.png'),'Redo', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.triggered.connect(self.text_field.redo)

        cut_act = QAction(QIcon('images/cut.png'),'Cut', self)
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.text_field.cut)

        copy_act = QAction(QIcon('images/copy.png'),'Copy', self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.text_field.copy)

        paste_act = QAction(QIcon('images/paste.png'),'Paste', self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.text_field.paste)

        find_act = QAction(QIcon('images/find.png'), 'Find', self)
        find_act.setShortcut('Ctrl+F')
        find_act.triggered.connect(self.findTextDialog)

        # Create actions for tools menu
        font_act = QAction(QIcon('images/font.png'), 'Font', self)
        font_act.setShortcut('Ctrl+T')
        font_act.triggered.connect(self.chooseFont)

        color_act = QAction(QIcon('images/color.png'), 'Color', self)
        color_act.setShortcut('Ctrl+Shift+C')
        color_act.triggered.connect(self.chooseFontColor)

        highlight_act = QAction(QIcon('images/highlight.png'), 'Highlight', self)
        highlight_act.setShortcut('Ctrl+Shift+H')
        highlight_act.triggered.connect(self.chooseFontBackgroundColor)

        about_act = QAction('About', self)
        about_act.triggered.connect(self.aboutDialog)
    
        # Create menubar 
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_act)
        file_menu.addSeparator()
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)

        # Create edit menu and add actions 
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act) 
        edit_menu.addSeparator()       
        edit_menu.addAction(cut_act) 
        edit_menu.addAction(copy_act) 
        edit_menu.addAction(paste_act) 
        edit_menu.addSeparator()
        edit_menu.addAction(find_act)

        # Create tools menu and add actions 
        tool_menu = menu_bar.addMenu('Tools')
        tool_menu.addAction(font_act)
        tool_menu.addAction(color_act)
        tool_menu.addAction(highlight_act)

        # Create help menu and add actions 
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction(about_act)

    def openFile(self):
        """
        Open a text or html file and display its contents in
        the text edit field.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File",
            "", "HTML Files (*.html);;Text Files (*.txt)")

        if file_name:
            with open(file_name, 'r') as f:
                notepad_text = f.read()
            self.text_field.setText(notepad_text)
        else:
            QMessageBox.information(self, "Error", 
                "Unable to open file.", QMessageBox.Ok)

    def saveToFile(self):
        """
        If the save button is clicked, display dialog asking user if
        they want to save the text in the text edit field to a text file.
        """ 
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File',
            "","HTML Files (*.html);;Text Files (*.txt)")

        if file_name.endswith('.txt'):
            notepad_text = self.text_field.toPlainText()
            with open(file_name, 'w') as f:            
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_richtext = self.text_field.toHtml()
            with open(file_name, 'w') as f:            
                f.write(notepad_richtext)
        else:
            QMessageBox.information(self, "Error", 
                "Unable to save file.", QMessageBox.Ok)

    def clearText(self):
        """
        If the new button is clicked, display dialog asking user if
        they want to clear the text edit field or not. 
        """
        answer = QMessageBox.question(self, "Clear Text", 
            "Do you want to clear the text?", QMessageBox.No | QMessageBox.Yes,
            QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            self.text_field.clear()
        else:
            pass

    def findTextDialog(self):
        """
        Search for text in QTextEdit widget
        """
        # Display input dialog to ask user for text to search for
        find_text, ok = QInputDialog.getText(self, "Search Text", "Find:")

        extra_selections = []

        # check to make sure text can be modified
        if ok and not self.text_field.isReadOnly():
            # set the cursor in the textedit field to the beginning
            self.text_field.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)

            # look for next occurrence of text 
            while(self.text_field.find(find_text)):
                # Use ExtraSelections to mark the text you are
                # searching for as yellow 
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)

                # set the cursor of the selection 
                selection.cursor = self.text_field.textCursor()

                # add selection to list 
                extra_selections.append(selection)

            # highlight selections in text edit widget
            for i in extra_selections:
                self.text_field.setExtraSelections(extra_selections)
            
            
    def chooseFont(self):
        """
        Select font for text
        """
        current = self.text_field.currentFont()

        font, ok = QFontDialog.getFont(current, self, options=QFontDialog.DontUseNativeDialog)
        if ok:
            self.text_field.setCurrentFont(font) # Use setFont() to set to one type of font 
        
        self.text_field.setCurrentFont(font)
                
    def chooseFontColor(self):
        """
        Select color for text
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextColor(color)

    def chooseFontBackgroundColor(self):
        """
        Select color for text's background
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextBackgroundColor(color)

    def aboutDialog(self):
        """
        Display information about program dialog box
        """
        QMessageBox.about(self, "About Notepad", "Beginner's Practical Guide to PyQt\n\nProject 5.1 - Notepad GUI")

# Run program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())