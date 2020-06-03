"""
Listing 4-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
    QTextEdit, QMessageBox, QFileDialog)

class Notepad(QWidget):
    
    def __init__(self): # constructor
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('4.1 – Notepad GUI')
        self.notepadWidgets()

        self.show()

    def notepadWidgets(self):
        """
        Create widgets for notepad GUI and arrange them in window
        """
        # create push buttons for editing menu
        new_button = QPushButton("New", self)
        new_button.move(10, 20)
        new_button.clicked.connect(self.clearText)

        save_button = QPushButton("Save", self)
        save_button.move(80, 20)
        save_button.clicked.connect(self.saveText)

        # create text edit field
        self.text_field = QTextEdit(self)
        self.text_field.resize(280, 330)
        self.text_field.move(10, 60)

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
        
    def saveText(self):
        """
        If the save button is clicked, display dialog asking user if
        they want to save the text in the text edit field to a text file.
        """ 
        options = QFileDialog.Options()
        notepad_text = self.text_field.toPlainText()

        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File',
            "","All Files (*);;Text Files (*.txt)", options=options)

        if file_name:
            with open(file_name, 'w') as f:            
                f.write(notepad_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())