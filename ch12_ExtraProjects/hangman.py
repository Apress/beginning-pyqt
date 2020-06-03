"""
Listing 12-5
written by Joshua Willman
Featured in "Beginning Pyqt - A Hands-on Approach to GUI Programming"
"""
# import necessary modules
import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
    QLabel, QFrame, QButtonGroup, QHBoxLayout, QVBoxLayout, 
    QMessageBox, QSizePolicy)
from PyQt5.QtCore import Qt, QRect, QLine
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

style_sheet = """
    QWidget{
        background-color: #FFFFFF
    }

    QLabel#Word{
        font: bold 20px;
        qproperty-alignment: AlignCenter
    }

    QPushButton#Letters{
        background-color: #1FAEDE;
        color: #D2DDE1;
        border-style: solid; 
        border-radius: 3px;
        border-color: #38454A;
        font: 28px
    }

    QPushButton#Letters:pressed{
        background-color: #C86354;
        border-radius: 4px;
        padding: 6px;
        color: #DFD8D7
    }

    QPushButton#Letters:disabled{
        background-color: #BBC7CB
    }
"""

# The hangman is drawn on a QLabel object, rather than 
# on the main window. This class handles the drawing. 
class DrawingLabel(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.height = 200
        self.width = 300

        self.incorrect_letter = False
        self.incorrect_turns = 0

        self.empty_list = []

    def drawHangmanBackground(self, painter):
        """ 
        Draw the gallows.
        """
        painter.setBrush(QBrush(QColor("#000000")))
        # drawRect(x, y, width, height)
        painter.drawRect((self.width / 2) - 40, self.height, 150, 4)
        painter.drawRect(self.width / 2, 0, 4, 200)
        painter.drawRect(self.width / 2, 0, 60, 4)
        painter.drawRect((self.width / 2) + 60, 0, 4, 40)

    def drawHangmanBody(self, painter):
        """
        Create and draw body parts for hangman.
        """
        if "head" in self.empty_list:
            head = QRect((self.width / 2) + 42, 40, 40, 40)
            painter.setPen(QPen(QColor("#000000"), 3))
            painter.setBrush(QBrush(QColor("#FFFFFF")))
            painter.drawEllipse(head)
        if "body" in self.empty_list:
            body = QRect((self.width / 2) + 60, 80, 2, 55)
            painter.setBrush(QBrush(QColor("#000000")))
            painter.drawRect(body)
        if "right_arm" in self.empty_list:
            right_arm = QLine((self.width / 2) + 60, 85, 
                (self.width / 2) + 50, (self.height / 2) + 30)
            pen = QPen(Qt.black, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(right_arm)
        if "left_arm" in self.empty_list:
            left_arm = QLine((self.width / 2) + 62, 85, 
                (self.width / 2) + 72, (self.height / 2) + 30)
            painter.drawLine(left_arm)
        if "right_leg" in self.empty_list:
            right_leg = QLine((self.width / 2) + 60, 135, 
                (self.width / 2) + 50, (self.height / 2) + 75)
            painter.drawLine(right_leg)
        if "left_leg" in self.empty_list:
            left_leg = QLine((self.width / 2) + 62, 135, 
                (self.width / 2) + 72, (self.height / 2) + 75)      
            painter.drawLine(left_leg)
        
        # Reset variable
        self.incorrect_letter = False

    def paintEvent(self, event):
        """
        Construct the QPainter and handle painting events.
        """
        painter = QPainter()
        painter.begin(self)

        self.drawHangmanBackground(painter)

        if self.incorrect_letter == True:
            self.drawHangmanBody(painter)

        painter.end()

class Hangman(QMainWindow):

    def __init__(self):
        super().__init__() 

        self.initializeUI() 

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setFixedSize(400, 500)
        self.setWindowTitle('12.5 - Hangman GUI')

        self.newGame()

        self.show()  

    def newGame(self):
        """
        Create new Hangman game.
        """
        self.setupHangmanBoard()
        self.setupWord()
        self.setupBoard()

    def setupHangmanBoard(self):
        """
        Set up label object to display hangman.
        """ 
        self.hangman_label = DrawingLabel(self)
        self.hangman_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def setupWord(self):
        """
        Open words file and choose random word.
        Create labels that will display '_' depending
        upon length of word.
        """
        words = self.openFile()
        self.chosen_word = random.choice(words).upper()
        #print(self.chosen_word)

        # Keep track of correct guesses
        self.correct_counter = 0

        # Keep track of label objects.
        # Is used for updating the text on the labels
        self.labels = []

        word_h_box = QHBoxLayout()

        for letter in self.chosen_word:
            self.letter_label = QLabel("___")
            self.labels.append(self.letter_label)
            self.letter_label.setObjectName("Word")
            word_h_box.addWidget(self.letter_label)
            
        self.word_frame = QFrame()
        self.word_frame.setLayout(word_h_box)

    def setupBoard(self):
        """
        Set up objects and layouts for keyboard and main window.
        """
        top_row_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        mid_row_list = ["I", "J", "K", "L", "M", "N", "O", "P", "Q"]
        bot_row_list = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # Create buttongroup to keep track of letters
        self.keyboard_bg = QButtonGroup()
        
        # Set up keys in the top row
        top_row_h_box = QHBoxLayout()

        for letter in top_row_list:
            button = QPushButton(letter)
            button.setObjectName("Letters")
            top_row_h_box.addWidget(button)
            self.keyboard_bg.addButton(button)

        top_frame = QFrame()
        top_frame.setLayout(top_row_h_box)

        # Set up keys in the middle row
        mid_row_h_box = QHBoxLayout()

        for letter in mid_row_list:
            button = QPushButton(letter)
            button.setObjectName("Letters")
            mid_row_h_box.addWidget(button)
            self.keyboard_bg.addButton(button)

        mid_frame = QFrame()
        mid_frame.setLayout(mid_row_h_box)

        # Set up keys in the bottom row
        bot_row_h_box = QHBoxLayout()

        for letter in bot_row_list:
            button = QPushButton(letter)
            button.setObjectName("Letters")
            bot_row_h_box.addWidget(button)
            self.keyboard_bg.addButton(button)

        bot_frame = QFrame()
        bot_frame.setLayout(bot_row_h_box)

        # Connect buttons in button group to slot
        self.keyboard_bg.buttonClicked.connect(self.buttonPushed)
        
        keyboard_v_box = QVBoxLayout()
        keyboard_v_box.addWidget(top_frame)
        keyboard_v_box.addWidget(mid_frame)
        keyboard_v_box.addWidget(bot_frame)

        keyboard_frame = QFrame()
        keyboard_frame.setLayout(keyboard_v_box)
        
        # Create main layout and add widgets
        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.hangman_label)
        main_v_box.addWidget(self.word_frame)
        main_v_box.addWidget(keyboard_frame)

        # Create central widget for main window
        central_widget = QWidget()
        central_widget.setLayout(main_v_box)

        self.setCentralWidget(central_widget)

    def buttonPushed(self, button):
        """
        Handle buttons from the button group and game logic.
        """
        button.setEnabled(False)

        body_parts_list = ["head", "body", "right_arm", 
            "left_arm", "right_leg", "left_leg"]

        # When the user guesses incorrectly and the number of incorrect
        # turns is not equal to 6 (the number of body parts).
        if button.text() not in self.chosen_word and self.hangman_label.incorrect_turns <= 5:
            self.hangman_label.incorrect_turns += 1
            index = self.hangman_label.incorrect_turns - 1
            self.hangman_label.empty_list.append(body_parts_list[index])
            self.hangman_label.incorrect_letter = True  
        # When a correct letter is chosen, update labels and 
        # correct counter.
        elif button.text() in self.chosen_word and self.hangman_label.incorrect_turns <= 5:
            self.hangman_label.incorrect_letter = True
            for i in range(len(self.chosen_word)):
                if self.chosen_word[i] == button.text():
                    self.labels[i].setText(button.text())
                    self.correct_counter += 1

        # Call update before checking winning conditions
        self.update()

        # User wins when the number of correct letters equals
        # the length of the word.
        if self.correct_counter == len(self.chosen_word):
            self.displayDialogs("win")
        
        # Game over if number of incorrect turns equals
        # the number of body parts. Reveal word to user.
        if self.hangman_label.incorrect_turns == 6:
            for i in range(len(self.chosen_word)):
                self.labels[i].setText(self.chosen_word[i])
            self.displayDialogs("game_over")

        #self.update()

    def openFile(self):
        """
        Open words.txt file.
        """
        try:
            with open("files/words.txt", 'r') as f:
                word_list = f.read().splitlines()
                return word_list
        except FileNotFoundError:
            print("File Not Found.")
            ex_list = ["nofile"]
            return ex_list

    def displayDialogs(self, text):
        """
        Display win and game over dialog boxes.
        """
        if text == "win":
            message = QMessageBox().question(self, "Win!", 
                "You Win!\nNEW GAME?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        elif text == "game_over":
            message = QMessageBox().question(self, "Game Over", 
                "Game Over\nNEW GAME?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if message == QMessageBox.No:
            self.close()
        else:
            self.newGame()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = Hangman()
    sys.exit(app.exec_())