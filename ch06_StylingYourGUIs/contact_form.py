"""
Listing 6-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QLabel, 
    QRadioButton, QGroupBox, QLineEdit, QHBoxLayout, QVBoxLayout)

class ContactForm(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Contact Form Example')

        self.setupTabs()

        self.show()

    def setupTabs(self):
        """
        Set up tab bar and different tab widgets. Each tab is a QWidget that
        serves as a container for each page. 
        """
        # Create tab bar and different tabs
        self.tab_bar = QTabWidget(self)

        self.prof_details_tab = QWidget()
        self.background_tab = QWidget()

        self.tab_bar.addTab(self.prof_details_tab, "Profile Details")
        self.tab_bar.addTab(self.background_tab, "Background")

        # Call methods that contain the widgets for each tab
        self.profileDetailsTab()
        self.backgroundTab()

        # Create layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)

        # Set main window's layout
        self.setLayout(main_h_box)

    def profileDetailsTab(self):
        """
        Create the profile tab. Allows the user enter their name, 
        address and select their gender.
        """
        # Set up labels and line edit widgets 
        name_label = QLabel("Name")
        name_entry = QLineEdit()

        address_label = QLabel("Address")
        address_entry = QLineEdit()

        # Create group box to contain radio buttons 
        sex_gb = QGroupBox("Sex")
 
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("Female")

        # Create and set layout for sex_gb widget
        sex_h_box = QHBoxLayout()
        sex_h_box.addWidget(male_rb)
        sex_h_box.addWidget(female_rb)

        sex_gb.setLayout(sex_h_box)

        # Add all widgets to the profile details page layout
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(address_label)
        tab_v_box.addWidget(address_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(sex_gb)

        # Set layout for profile details tab 
        self.prof_details_tab.setLayout(tab_v_box)

    def backgroundTab(self):
        """
        Create the background tab. The user can select a 
        """
        # Set up group box to hold radio buttons
        self.education_gb = QGroupBox("Highest Level of Education")

        # Layout for education_gb
        ed_v_box = QVBoxLayout()

        # Create and add radio buttons to ed_v_box
        education_list = ["High School Diploma", "Associate's Degree",
            "Bachelor's Degree", "Master's Degree", "Doctorate or Higher"]
        for ed in education_list:
            self.education_rb = QRadioButton(ed)
            ed_v_box.addWidget(self.education_rb)
        # Set layout for group box
        self.education_gb.setLayout(ed_v_box)

        # Create and set for background tab
        tab_v_box = QVBoxLayout()
        tab_v_box.addWidget(self.education_gb)

        self.background_tab.setLayout(tab_v_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactForm()
    sys.exit(app.exec_())