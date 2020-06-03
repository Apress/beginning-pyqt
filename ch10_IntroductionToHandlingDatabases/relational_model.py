"""
Listing 10-6
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modeules
import os, sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, 
    QVBoxLayout, QMessageBox, QHeaderView)
from PyQt5.QtSql import (QSqlDatabase, QSqlRelationalTableModel, 
    QSqlRelation)

class TableDisplay(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setMinimumSize(1000, 500)
        self.setWindowTitle('Relational Table Model')

        self.createConnection()
        self.createTable()

        self.show()

    def createConnection(self):
        """
        Set up the connection to the database.
        Check for the tables needed. 
        """
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("files/accounts.db")

        if not database.open():
            print("Unable to open data source file.")
            sys.exit(1) # Error code 1 - signifies error

        # Check if the tables we need exist in the database
        tables_needed = {'accounts', 'countries'}
        tables_not_found = tables_needed - set(database.tables())
        if tables_not_found:
            QMessageBox.critical(None, 'Error',
                f'The following tables tables are missing from the database: {tables_not_found}')
            sys.exit(1) # Error code 1 - signifies error

    def createTable(self):
        """
        Create the table using model/view architecture.
        """
        # Create the model
        model = QSqlRelationalTableModel()
        model.setTable('accounts')
        # Set up relationship for foreign keys
        model.setRelation(model.fieldIndex('country_id'), QSqlRelation('countries', 'id', 'country'))

        table_view = QTableView()
        table_view.setModel(model)
        table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Populate the model with data
        model.select()

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(table_view)
        self.setLayout(main_v_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableDisplay()
    sys.exit(app.exec_())