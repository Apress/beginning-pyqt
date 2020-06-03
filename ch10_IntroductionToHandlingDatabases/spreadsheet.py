"""
Listing 10-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
    QTableWidget, QTableWidgetItem, QMenu, QAction,
    QInputDialog)

class SpreadsheetFramework(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("Spreadsheet - Table Example")

        # Used for copy and paste actions
        self.item_text = None

        self.createMenu()
        self.createTable()

        self.show()

    def createTable(self):
        """
        Set up table widget.
        """
        self.table_widget = QTableWidget()

        # Set initial row and column values
        self.table_widget.setRowCount(10)
        self.table_widget.setColumnCount(10)

        # Set focus on cell in the table 
        self.table_widget.setCurrentCell(0, 0)

        # When the horizontal headers are double-clicked, emit a signal
        self.table_widget.horizontalHeader().sectionDoubleClicked.connect(self.changeHeader)

        self.setCentralWidget(self.table_widget)

    def createMenu(self):
        """
        Set up the menu bar.
        """
        # Create file menu actions
        quit_act = QAction("Quit", self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(self.close)

        # Create table menu actions 
        self.add_row_above_act = QAction("Add Row Above", self)
        self.add_row_above_act.triggered.connect(self.addRowAbove)
        
        self.add_row_below_act = QAction("Add Row Below", self)
        self.add_row_below_act.triggered.connect(self.addRowBelow)

        self.add_col_before_act = QAction("Add Column Before", self)
        self.add_col_before_act.triggered.connect(self.addColumnBefore)
        
        self.add_col_after_act = QAction("Add Column After", self)
        self.add_col_after_act.triggered.connect(self.addColumnAfter)

        self.delete_row_act = QAction("Delete Row", self)
        self.delete_row_act.triggered.connect(self.deleteRow)

        self.delete_col_act = QAction("Delete Column", self)
        self.delete_col_act.triggered.connect(self.deleteColumn)

        self.clear_table_act = QAction("Clear All", self)
        self.clear_table_act.triggered.connect(self.clearTable)

        # Create the menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(quit_act)

        # Create table menu and add actions
        table_menu = menu_bar.addMenu('Table')
        table_menu.addAction(self.add_row_above_act)
        table_menu.addAction(self.add_row_below_act)
        table_menu.addSeparator()
        table_menu.addAction(self.add_col_before_act)
        table_menu.addAction(self.add_col_after_act)
        table_menu.addSeparator()
        table_menu.addAction(self.delete_row_act)
        table_menu.addAction(self.delete_col_act)
        table_menu.addSeparator()
        table_menu.addAction(self.clear_table_act)

    def contextMenuEvent(self, event):
        """
        Create context menu and actions.
        """
        context_menu = QMenu(self)
        
        context_menu.addAction(self.add_row_above_act)
        context_menu.addAction(self.add_row_below_act)
        context_menu.addSeparator()
        context_menu.addAction(self.add_col_before_act)
        context_menu.addAction(self.add_col_after_act)
        context_menu.addSeparator()
        context_menu.addAction(self.delete_row_act)
        context_menu.addAction(self.delete_col_act)
        context_menu.addSeparator()
        copy_act = context_menu.addAction("Copy")
        paste_act = context_menu.addAction("Paste")
        context_menu.addSeparator()
        context_menu.addAction(self.clear_table_act)

        # Execute the context_menu and return the action selected. 
        # mapToGlobal() translates the position of the window coordinates 
        # to the global screen cooridnates. This way we can detect if 
        # a right-click occurred inside of the GUI and display the context menu.
        action = context_menu.exec_(self.mapToGlobal(event.pos()))

        # To check for actions selected in the context menu that were not
        # created in the menu bar. 
        if action == copy_act:
            self.copyItem()
        if action == paste_act:
            self.pasteItem()
    
    def changeHeader(self):
        """ 
        Change horizontal headers by returning the text from input dialog.
        """
        col = self.table_widget.currentColumn()

        text, ok = QInputDialog.getText(self, "Enter Header", "Header text:")
        
        if ok and text != "":
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(text))
        else:
            pass    

    def copyItem(self):
        """
        If the current cell selected is not empty, store the text.
        """
        if self.table_widget.currentItem() != None:
            self.item_text = self.table_widget.currentItem().text()

    def pasteItem(self):
        """
        Set item for selected cell.
        """
        if self.item_text != None:
            row = self.table_widget.currentRow()
            column = self.table_widget.currentColumn()
            self.table_widget.setItem(row, column, QTableWidgetItem(self.item_text))

    def addRowAbove(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row)

    def addRowBelow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.insertRow(current_row + 1)

    def addColumnBefore(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col)

    def addColumnAfter(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.insertColumn(current_col + 1)

    def deleteRow(self):
        current_row = self.table_widget.currentRow()
        self.table_widget.removeRow(current_row)

    def deleteColumn(self):
        current_col = self.table_widget.currentColumn()
        self.table_widget.removeColumn(current_col)

    def clearTable(self):
        self.table_widget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpreadsheetFramework()
    sys.exit(app.exec_())