"""
Listing 9-1
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import (QPainter, QPainterPath, QColor, 
    QBrush, QPen, QFont, QPolygon, QLinearGradient)
from PyQt5.QtCore import Qt, QPoint, QRect

class Drawing(QWidget):

    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setFixedSize(600, 600)
        self.setWindowTitle('QPainter Basics')

        # Create a few pen colors
        self.black = '#000000'
        self.blue = '#2041F1'
        self.green = '#12A708'
        self.purple = '#6512F0'
        self.red = '#E00C0C'
        self.orange = '#FF930A'

        self.show()

    def paintEvent(self, event):
        """
        Create QPainter object and handle paint events.
        """
        painter = QPainter()
        painter.begin(self)
        # Use antialiasing to smooth curved edges
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawPoints(painter)
        self.drawDiffLines(painter)
        self.drawText(painter)
        self.drawRectangles(painter)
        self.drawPolygons(painter)
        self.drawRoundedRects(painter)
        self.drawCurves(painter)
        self.drawCircles(painter)
        self.drawGradients(painter)

        painter.end()

    def drawPoints(self, painter):
        """
        Example of how to draw points with QPainter.
        """
        pen = QPen(QColor(self.black))

        for i in range(1, 9):
            pen.setWidth(i * 2)
            painter.setPen(pen)
            painter.drawPoint(i * 20, i * 20)
        
    def drawDiffLines(self, painter):
        """
        Examples of how to draw lines with QPainter.
        """
        pen = QPen(QColor(self.black), 2)

        painter.setPen(pen)
        painter.drawLine(230, 20, 230, 180)
        
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(260, 20, 260, 180)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(290, 20, 290, 180)

        pen.setStyle(Qt.DashDotLine) 
        painter.setPen(pen)
        painter.drawLine(320, 20, 320, 180)    

        # Change the color and thickness of the pen
        blue_pen = QPen(QColor(self.blue), 4)

        painter.setPen(blue_pen)
        painter.drawLine(350, 20, 350, 180)

        blue_pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(blue_pen)
        painter.drawLine(380, 20, 380, 180)

    def drawText(self, painter):
        """
        Example of how to draw text with QPainter.
        """
        text = "Don't look behind you."

        pen = QPen(QColor(self.red))
        painter.setFont(QFont("Helvetica", 15))
        painter.setPen(pen)
        painter.drawText(420, 110, text)

    def drawRectangles(self, painter):
        """
        Examples of how to draw rectangles with QPainter.
        """
        pen = QPen(QColor(self.black))
        brush = QBrush(QColor(self.black))

        painter.setPen(pen)
        painter.drawRect(20, 220, 80, 80)

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(120, 220, 80, 80)

        red_pen = QPen(QColor(self.red), 5)
        green_brush = QBrush(QColor(self.green))

        painter.setPen(red_pen)
        painter.setBrush(green_brush)
        painter.drawRect(20, 320, 80, 80)

        # Demonstrate how to change the alpha channel
        # to include transparency 
        blue_pen = QPen(QColor(32, 85, 230, 100), 5)
        blue_pen.setStyle(Qt.DashLine)
        painter.setPen(blue_pen)
        painter.setBrush(green_brush)
        painter.drawRect(120, 320, 80, 80)

    def drawPolygons(self, painter):
        """
        Example of how to draw polygons with QPainter.
        """
        pen = QPen(QColor(self.blue), 2)
        brush = QBrush(QColor(self.orange))

        points = QPolygon([QPoint(240, 240), QPoint(380, 250),
                         QPoint(230, 380), QPoint(370, 360)])

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPolygon(points)

    def drawRoundedRects(self, painter):
        """
        Examples of how to draw rectangles with
        rouneded corners with QPainter.
        """
        pen = QPen(QColor(self.black))
        brush = QBrush(QColor(self.black))

        rect_1 = QRect(420, 340, 40, 60)
        rect_2 = QRect(480, 300, 50, 40)
        rect_3 = QRect(540, 240, 40, 60)

        painter.setPen(pen)
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect_1, 8, 8)

        brush.setStyle(Qt.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect_2, 5, 20)

        brush.setStyle(Qt.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRoundedRect(rect_3, 15, 15)

    def drawCurves(self, painter):
        """
        Examples of how to draw curves with QPainterPath.
        """
        pen = QPen(Qt.black, 3)
        brush = QBrush(Qt.white)

        tail_path = QPainterPath()
        tail_path.moveTo(30, 420)
        tail_path.cubicTo(30, 420, 65, 500, 30, 560)
        tail_path.lineTo(163, 540)
        tail_path.cubicTo(125, 360, 110, 440, 30, 420)
        tail_path.closeSubpath()
        
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(tail_path)

    def drawCircles(self, painter):
        """
        Example of how to draw ellipses with QPainter.
        """
        height, width = self.height(), self.width()

        center_x, center_y = (width / 2), height - 100 
        radius_x, radius_y = 60, 60

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        brush = QBrush(Qt.darkMagenta, Qt.Dense5Pattern)

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawEllipse(QPoint(center_x, center_y), radius_x, radius_y)

    def drawGradients(self, painter):
        """
        Example of how to draw fill shapes using gradients.
        """
        pen = QPen(QColor(self.black), 2)
        gradient = QLinearGradient(450, 480, 520, 550)

        gradient.setColorAt(0.0, Qt.blue)
        gradient.setColorAt(0.5, Qt.yellow)
        gradient.setColorAt(1.0, Qt.cyan)

        painter.setPen(pen)
        painter.setBrush(QBrush(gradient))
        painter.drawRect(420, 420, 160, 160)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Drawing()
    sys.exit(app.exec_())