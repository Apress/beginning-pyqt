"""
Listing 8-4
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget,
    QPushButton, QHBoxLayout, QVBoxLayout, QListWidgetItem, QInputDialog)

class GroceryListGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("QListWidget Example")
        self.setupWidgets()

        self.show()

    def setupWidgets(self):
        """
        Create and arrange widgets in window
        """
        self.list_widget = QListWidget()
        self.list_widget.setAlternatingRowColors(True)

        # initilialize the Qlistwidget with items 
        grocery_list = ["grapes", "broccoli", "garlic", "cheese",
                         "bacon", "eggs", "waffles", "rice", "soda"]
        for item in grocery_list:
            list_item = QListWidgetItem()
            list_item.setText(item)
            self.list_widget.addItem(list_item)

        # Create buttons
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.addListItem)

        insert_button = QPushButton("Insert")
        insert_button.clicked.connect(self.insertItemInList)

        remove_button = QPushButton("Remove")
        remove_button.clicked.connect(self.removeOneItem)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.list_widget.clear)

        # create layout
        right_v_box = QVBoxLayout()
        right_v_box.addWidget(add_button)
        right_v_box.addWidget(insert_button)
        right_v_box.addWidget(remove_button)
        right_v_box.addWidget(clear_button)

        left_h_box = QHBoxLayout()
        left_h_box.addWidget(self.list_widget)
        left_h_box.addLayout(right_v_box)

        self.setLayout(left_h_box)

    def addListItem(self):
        """
        Add a single item to the list widget.
        """
        text, ok = QInputDialog.getText(self, "New Item", "Add item:")
        if ok and text != "":
            list_item = QListWidgetItem()
            list_item.setText(text)
            self.list_widget.addItem(list_item)

    def insertItemInList(self):
        """
        Insert a single item into the list widget under the
        current highlighted row. 
        """
        text, ok = QInputDialog.getText(self, "Insert Item", "Insert item:")
        if ok and text != "":
            row = self.list_widget.currentRow()
            row = row + 1 # select row below current row
            new_item = QListWidgetItem()
            new_item.setText(text)
            self.list_widget.insertItem(row, new_item)

    def removeOneItem(self):
        """
        Remove a single item from the list widget.
        """
        row = self.list_widget.currentRow()
        self.list_widget.takeItem(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroceryListGUI()
    sys.exit(app.exec_())