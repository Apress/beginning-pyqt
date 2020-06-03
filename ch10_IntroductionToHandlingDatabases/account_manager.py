"""
Listing 10-7
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
    QPushButton, QComboBox, QTableView, QHeaderView,
    QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox)
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery,
    QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class AccountManager(QWidget):

    def __init__(self):
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setMinimumSize(1000, 600)
        self.setWindowTitle('10.1 – Account Management GUI')

        self.createConnection()
        self.createTable()
        self.setupWidgets()

        self.show()

    def createConnection(self):
        database = QSqlDatabase.addDatabase("QSQLITE") # SQLite version 3
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
        Set up the model, headers and populate the model.
        """
        self.model = QSqlRelationalTableModel()
        self.model.setTable('accounts')
        self.model.setRelation(self.model.fieldIndex('country_id'), QSqlRelation('countries', 'id', 'country'))

        self.model.setHeaderData(self.model.fieldIndex('id'), Qt.Horizontal, "ID")
        self.model.setHeaderData(self.model.fieldIndex('employee_id'), Qt.Horizontal, "Employee ID")
        self.model.setHeaderData(self.model.fieldIndex('first_name'), Qt.Horizontal, "First")
        self.model.setHeaderData(self.model.fieldIndex('last_name'), Qt.Horizontal, "Last")
        self.model.setHeaderData(self.model.fieldIndex('email'), Qt.Horizontal, "E-mail")
        self.model.setHeaderData(self.model.fieldIndex('department'), Qt.Horizontal, "Dept.")
        self.model.setHeaderData(self.model.fieldIndex('country_id'), Qt.Horizontal, "Country")
        
        # Populate the model with data
        self.model.select()

    def setupWidgets(self):
        """
        Create instances of widgets, the table view and set layouts.
        """
        icons_path = "icons"

        title = QLabel("Account Management System")
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        title.setStyleSheet("font: bold 24px")

        add_product_button = QPushButton("Add Employee")
        add_product_button.setIcon(QIcon(os.path.join(icons_path, "add_user.png")))
        add_product_button.setStyleSheet("padding: 10px")
        add_product_button.clicked.connect(self.addItem)

        del_product_button = QPushButton("Delete")
        del_product_button.setIcon(QIcon(os.path.join(icons_path, "trash_can.png")))
        del_product_button.setStyleSheet("padding: 10px")
        del_product_button.clicked.connect(self.deleteItem)

        # Set up sorting combobox
        sorting_options = ["Sort by ID", "Sort by Employee ID", "Sort by First Name", 
            "Sort by Last Name", "Sort by Department", "Sort by Country"]
        sort_name_cb = QComboBox()
        sort_name_cb.addItems(sorting_options)
        sort_name_cb.currentTextChanged.connect(self.setSortingOrder)

        buttons_h_box = QHBoxLayout()
        buttons_h_box.addWidget(add_product_button)
        buttons_h_box.addWidget(del_product_button)
        buttons_h_box.addStretch()
        buttons_h_box.addWidget(sort_name_cb)

        # Widget to contain editing buttons
        edit_buttons = QWidget()
        edit_buttons.setLayout(buttons_h_box)

        # Create table view and set model 
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)

        # Instantiate the delegate
        delegate = QSqlRelationalDelegate(self.table_view)
        self.table_view.setItemDelegate(delegate)

        # Main layout
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(title, Qt.AlignLeft)
        main_v_box.addWidget(edit_buttons)
        main_v_box.addWidget(self.table_view)
        self.setLayout(main_v_box)

    def addItem(self):
        """
        Add a new record to the last row of the table.
        """
        last_row = self.model.rowCount()
        self.model.insertRow(last_row)

        id = 0
        query = QSqlQuery()
        query.exec_("SELECT MAX (id) FROM accounts")
        if query.next():
            print(query.value(0))
            id = int(query.value(0))

    def deleteItem(self):
        """ 
        Delete an entire row from the table.
        """
        current_item = self.table_view.selectedIndexes()
        for index in current_item:
            self.model.removeRow(index.row())
        self.model.select()

    def setSortingOrder(self, text):
        """
        Sort the rows in table. 
        """
        if text == "Sort by ID":
            self.model.setSort(self.model.fieldIndex('id'), Qt.AscendingOrder)
        elif text == "Sort by Employee ID":
            self.model.setSort(self.model.fieldIndex('employee_id'), Qt.AscendingOrder)
        elif text == "Sort by First Name":
            self.model.setSort(self.model.fieldIndex('first_name'), Qt.AscendingOrder)
        elif text == "Sort by Last Name":
            self.model.setSort(self.model.fieldIndex('last_name'), Qt.AscendingOrder)
        elif text == "Sort by Department":
            self.model.setSort(self.model.fieldIndex('department'), Qt.AscendingOrder)
        elif text == "Sort by Country":
            self.model.setSort(self.model.fieldIndex('country'), Qt.AscendingOrder)

        self.model.select()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AccountManager()
    sys.exit(app.exec_())