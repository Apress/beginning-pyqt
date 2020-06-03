"""
Listing 12-2
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import os, sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget, QListWidgetItem,
    QLabel, QGroupBox, QPushButton, QVBoxLayout, QMdiArea, QMdiSubWindow,)
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtCore import Qt

class Camera(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('12.2 – Camera GUI')

        self.setupWindows()

        self.show()

    def setupWindows(self):
        """
        Set up QMdiArea parent and subwindows.
        Add available cameras on local system as items to 
        list widget.
        """
        # Create images directory if it does not already exist
        path = 'images'
        if not os.path.exists(path):
            os.makedirs(path)

        # Set up list widget that will display identified 
        # cameras on your computer.
        picture_label = QLabel("Press 'Spacebar' to take pictures.")
        camera_label = QLabel("Available Cameras")
        self.camera_list_widget = QListWidget()
        self.camera_list_widget.setAlternatingRowColors(True)

        # Add availableCameras to a list to be displayed in 
        # list widget. Use QCameraInfo() to list available cameras.
        self.cameras = list(QCameraInfo().availableCameras())
        for camera in self.cameras:
            self.list_item = QListWidgetItem()
            self.list_item.setText(camera.deviceName())
            self.camera_list_widget.addItem(self.list_item)

        # Create button that will allow user to select camera
        choose_cam_button = QPushButton("Select Camera")
        choose_cam_button.clicked.connect(self.selectCamera)

        # Create child widgets and layout for camera controls subwindow
        controls_gbox = QGroupBox()
        controls_gbox.setTitle("Camera Controls")

        v_box = QVBoxLayout()
        v_box.addWidget(picture_label, alignment=Qt.AlignCenter)
        v_box.addWidget(camera_label)
        v_box.addWidget(self.camera_list_widget)
        v_box.addWidget(choose_cam_button)

        controls_gbox.setLayout(v_box)

        controls_sub_window = QMdiSubWindow()
        controls_sub_window.setWidget(controls_gbox)
        controls_sub_window.setAttribute(Qt.WA_DeleteOnClose)

        # Create view finder subwindow
        self.view_finder_window = QMdiSubWindow()
        self.view_finder_window.setWindowTitle("Camera View")
        self.view_finder_window.setAttribute(Qt.WA_DeleteOnClose)

        # Create QMdiArea widget to manage subwindows
        mdi_area = QMdiArea()
        mdi_area.tileSubWindows()
        mdi_area.addSubWindow(self.view_finder_window)
        mdi_area.addSubWindow(controls_sub_window)

        # Set mdi_area widget as the central widget of main window
        self.setCentralWidget(mdi_area)

    def setupCamera(self, cam_name):
        """
        Create and setup camera functions.
        """
        for camera in self.cameras:
            # Select camera by matching cam_name to one of the 
            # devices in the cameras list. 
            if camera.deviceName() == cam_name:
                self.cam = QCamera(camera) # Construct QCamera device

                # Create camera viewfinder widget and add it to the 
                # view_finder_window.
                self.view_finder = QCameraViewfinder() 
                self.view_finder_window.setWidget(self.view_finder)
                self.view_finder.show()

                # Sets the view finder to display video 
                self.cam.setViewfinder(self.view_finder)

                # QCameraImageCapture() is used for taking 
                # images or recordings.
                self.image_capture = QCameraImageCapture(self.cam)

                # Configure the camera to capture still images.
                self.cam.setCaptureMode(QCamera.CaptureStillImage)
                self.cam.start() # Slot to start the camera
            else:
                pass

    def selectCamera(self):
        """
        Slot for selecting one of the available cameras displayed 
        in list widget. 
        """
        try:
            if self.list_item.isSelected():
                camera_name = self.list_item.text()
                self.setupCamera(camera_name)
            else:
                print("No camera selected.")
                pass
        except:
            print("No cameras detected.")

    def keyPressEvent(self, event):
        """
        Handle the key press event so that the camera takes images.
        """
        if event.key() == Qt.Key_Space:
            try:
                self.cam.searchAndLock()
                self.image_capture.capture("images/")
                self.cam.unlock()
            except:
                print("No camera in viewfinder.")
    
# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Camera()
    sys.exit(app.exec_())
