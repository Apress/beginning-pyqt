"""
Listing 5-5
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QAction,
    QFileDialog, QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar,
    QDockWidget, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class PhotoEditor(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen
        """
        self.setFixedSize(650, 650)
        self.setWindowTitle('5.2 - Photo Editor GUI')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()

        self.show()

    def createMenu(self):
        """
        Create menu for photo editor GUI
        """
        # Create actions for file menu
        self.open_act = QAction(QIcon('images/open_file.png'),"Open", self)
        self.open_act.setShortcut('Ctrl+O')
        self.open_act.setStatusTip('Open a new image')
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon('images/save_file.png'),"Save", self)
        self.save_act.setShortcut('Ctrl+S')
        self.save_act.setStatusTip('Save image')
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon('images/print.png'), "Print", self)
        self.print_act.setShortcut('Ctrl+P')
        self.print_act.setStatusTip('Print image')
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        # Create actions for edit menu
        self.rotate90_act = QAction("Rotate 90º", self)
        self.rotate90_act.setStatusTip('Rotate image 90º clockwise')
        self.rotate90_act.triggered.connect(self.rotateImage90)

        self.rotate180_act = QAction("Rotate 180º", self)
        self.rotate180_act.setStatusTip('Rotate image 180º clockwise')
        self.rotate180_act.triggered.connect(self.rotateImage180)

        self.flip_hor_act = QAction("Flip Horizontal", self)
        self.flip_hor_act.setStatusTip('Flip image across horizontal axis')
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)

        self.flip_ver_act = QAction("Flip Vertical", self)
        self.flip_ver_act.setStatusTip('Flip image across vertical axis')
        self.flip_ver_act.triggered.connect(self.flipImageVertical)

        self.resize_act = QAction("Resize Half", self)
        self.resize_act.setStatusTip('Resize image to half the original size')
        self.resize_act.triggered.connect(self.resizeImageHalf)

        self.clear_act = QAction(QIcon('images/clear.png'), "Clear Image", self)
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip('Clear the current image')
        self.clear_act.triggered.connect(self.clearImage)

        # Create menubar 
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add actions 
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)

        # Create edit menu and add actions 
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_act)

        # Create view menu and add actions 
        view_menu = menu_bar.addMenu('View')
        view_menu.addAction(self.toggle_dock_tools_act)

        # Display info about tools, menu, and view in the statusbar
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        """
        Create toolbar for photo editor GUI
        """
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24,24))
        self.addToolBar(tool_bar)

        # add actions to toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)

    def createToolsDockWidget(self):
        """
        Use View -> Edit Image Tools menu and click the dock widget on or off.
        Tools dock can be placed on the left or right of the main window. 
        """
        # set up QDockWidget
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Image Tools")
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea |
            Qt.RightDockWidgetArea)

        # create container QWidget to hold all widgets inside dock widget
        self.tools_contents = QWidget()

        # create tool push buttons 
        self.rotate90 = QPushButton("Rotate 90º")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip('Rotate image 90º clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton("Rotate 180º")
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip('Rotate image 180º clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip('Flip image across vertical axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip('Resize image to half the original size')
        self.resize_half.clicked.connect(self.resizeImageHalf)

        # set up vertical layout to contain all the push buttons 
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)

        # set the main layout for the QWidget, tools_contents,
        # then set the main widget of the dock widget
        self.tools_contents.setLayout(dock_v_box)
        self.dock_tools_view.setWidget(self.tools_contents)
        
        # set initial location of dock widget
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)

        # handles the visibility of the dock widget
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()

    def photoEditorWidgets(self):
        """
        Set up instances of widgets for photo editor GUI
        """
        self.image = QPixmap()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be 
        # resized, horizontally and vertically. Here, the image 
        # will stretch horizontally, but not vertically.
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)

        self.setCentralWidget(self.image_label)

    def openImage(self):
        """
        Open an image file and display its contents in label widget.
        Display error message if image can't be opened. 
        """
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image",
            "", "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;\
                GIF Files (*.gif)")

        if image_file:
            self.image = QPixmap(image_file)

            self.image_label.setPixmap(self.image.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.information(self, "Error", 
                "Unable to open image.", QMessageBox.Ok)

        self.print_act.setEnabled(True)

    def saveImage(self):
        """
        Save the image.
        Display error message if image can't be saved. 
        """
        image_file, _ = QFileDialog.getSaveFileName(self, "Save Image",
            "", "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;\
                GIF Files (*.gif)")

        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Error", 
                "Unable to save image.", QMessageBox.Ok)

    def printImage(self):
        """
        Print image.
        """
        # create printer object and print output defined by the platform
        # the program is being run on. 
        # QPrinter.NativeFormat is the default
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat) 

        # Create printer dialog to configure printer
        print_dialog = QPrintDialog(printer)
        
        # if the dialog is accepted by the user, begin printing
        if (print_dialog.exec_() == QPrintDialog.Accepted):
            # use QPainter to output a PDF file 
            painter = QPainter()
            # begin painting device
            painter.begin(printer)
            # Set QRect to hold painter's current viewport, which 
            # is the image_label 
            rect = QRect(painter.viewport())
            # get the size of image_label and use it to set the size 
            # of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # scale the image_label to fit the rect source (0, 0) 
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            # end painting
            painter.end()
            
    def clearImage(self):
        """
        Clears current image in QLabel widget
        """
        self.image_label.clear()
        self.image = QPixmap() # reset pixmap so that isNull() = True

    def rotateImage90(self):
        """
        Rotate image 90º clockwise
        """
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)

            rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)

            self.image_label.setPixmap(rotated.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(rotated) 
            self.image_label.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def rotateImage180(self):
        """
        Rotate image 180º clockwise
        """
        if self.image.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)

            rotated = pixmap.transformed(transform180, mode=Qt.SmoothTransformation)

            self.image_label.setPixmap(rotated.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            # .......... To keep being allowed to rotate the image
            self.image = QPixmap(rotated) 
            self.image_label.repaint() # repaint the child widget
        else:
            # No image to rotate
            pass

    def flipImageHorizontal(self):
        """
        Mirror the image across the horizontal axis
        """
        if self.image.isNull() == False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)

            flipped = pixmap.transformed(flip_h)

            self.image_label.setPixmap(flipped.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            # No image to flip
            pass

    def flipImageVertical(self):
        """
        Mirror the image across the vertical axis
        """
        if self.image.isNull() == False:
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)

            flipped = pixmap.transformed(flip_v)

            self.image_label.setPixmap(flipped.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            # No image to flip
            pass

    def resizeImageHalf(self):
        """
        Resize the image to half its current size.
        """
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)

            resized = pixmap.transformed(resize)

            self.image_label.setPixmap(resized.scaled(self.image_label.size(), 
                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(resized)
            self.image_label.repaint()
        else:
            # No image to resize
            pass

    def centerMainWindow(self):
        """
        Use QDesktopWidget class to access information about your screen  
        and use it to center the application window.
        """
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()

        self.move((screen_width - self.width()) / 2, (screen_height - self.height()) / 2)

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
    ex = PhotoEditor()
    sys.exit(app.exec_())
