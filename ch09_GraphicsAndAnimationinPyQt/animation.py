"""
Listing 9-3
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
    QGraphicsPixmapItem)
from PyQt5.QtCore import (QObject, QPointF, QRectF, 
    QPropertyAnimation, pyqtProperty)
from PyQt5.QtGui import QPixmap

# Create Objects class that defines the position property of 
# instances of the class using pyqtProperty.
class Objects(QObject):

    def __init__(self, image_path):
        super().__init__()

        item_pixmap = QPixmap(image_path)
        resize_item = item_pixmap.scaledToWidth(150)
        self.item = QGraphicsPixmapItem(resize_item)

    def _set_position(self, position):
        self.item.setPos(position)

    position = pyqtProperty(QPointF, fset=_set_position)

class AnimationScene(QGraphicsView):

    def __init__(self):
        super().__init__() 
        self.initializeView() 

    def initializeView(self):
        """
        Initialize the graphics view and display its contents 
        to the screen. 
        """
        self.setGeometry(100, 100, 700, 450)
        self.setWindowTitle('9.2 - Animation Example')

        self.createObjects()
        self.createScene()

        self.show()

    def createObjects(self):
        """
        Create instances of the Objects class, and set up the objects
        animations.
        """
        # List that holds all of the animations.
        animations = []

        # Create the car object and car animation.
        self.car = Objects('images/car.png')

        self.car_anim = QPropertyAnimation(self.car, b"position")
        self.car_anim.setDuration(6000)

        self.car_anim.setStartValue(QPointF(-50, 350))
        self.car_anim.setKeyValueAt(0.3, QPointF(150, 350))
        self.car_anim.setKeyValueAt(0.6, QPointF(170, 350))
        self.car_anim.setEndValue(QPointF(750, 350))

        # Create the tree object and tree animation.
        self.tree = Objects('images/trees.png')

        self.tree_anim = QPropertyAnimation(self.tree, b"position")
        self.tree_anim.setDuration(6000)

        self.tree_anim.setStartValue(QPointF(750, 150))
        self.tree_anim.setKeyValueAt(0.3, QPointF(170, 150))
        self.tree_anim.setKeyValueAt(0.6, QPointF(150, 150))
        self.tree_anim.setEndValue(QPointF(-150, 150))

        # Add animations to the animations list, and start the 
        # animations once the program begins running.
        animations.append(self.car_anim)
        animations.append(self.tree_anim)

        for anim in animations:
            anim.start()

    def createScene(self):
        """
        Create the graphics scene and add Objects instances
        to the scene.
        """
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 700, 450)
        self.scene.addItem(self.car.item)
        self.scene.addItem(self.tree.item)
        self.setScene(self.scene)

    def drawBackground(self, painter, rect):
        """
        Reimplement QGraphicsView's drawBackground() method.
        """
        scene_rect = self.scene.sceneRect()
        
        background = QPixmap("images/highway.jpg")
        bg_rectf = QRectF(background.rect())
        painter.drawPixmap(scene_rect, background, bg_rectf)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimationScene()
    sys.exit(app.exec_())