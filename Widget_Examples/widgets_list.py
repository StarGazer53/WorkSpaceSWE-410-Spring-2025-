"""
Caleb Aguiar
SWE-410
01/30/2025
GUI Application using PyQt6
In class activity
"""

#Import the system module to handle command line arguments
import sys

#import necessary PyQt6 modules for GUI components 
from PyQt6.QtCore import Qt # Qtcore module is for the core functionality like aligment, times, etc
from PyQt6.QtWidgets import QVBoxLayout # Layout manager for organizing widgets vertically 
from PyQt6.QtWidgets import QWidget # Base class for all UI objects 

from PyQt6.QtWidgets import (# Import various UI componets
    QApplication, # Manages application-wide settings and event handling
    QCheckBox, # Checkbox widge for boolean options
    QComboBox, # Drop down lists
    QDateEdit, # Date selection widget 
    QDateTimeEdit, # Date and Time selection 
    QDial, # Circular dial control 
    QDoubleSpinBox, # Input box for floating point numbers 
    QFontComboBox, # Drop down for selecting fonts 
    QLabel, # Display Text or images
    QLCDNumber, # LCD-Style number display
    QLineEdit, # Single line input field 
    QMainWindow, # Main application window class
    QProgressBar, # Display Progress of your task 
    QPushButton, # Clickable button widget 
    QRadioButton, # Radio button widget for selecting object option from many  
    QSlider, # Slider control for selecting a range of values 
    QSpinBox, # Input box for integers 
    QTimeEdit, # Time selection widget 
    )

# Define the main Application Window by subclass QMainwindow 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # Call the Constructor of the parent QMainWindow Class
        self.setWindowTitle("Widget App")
        layout = QVBoxLayout() #Create a vertical layout for organizing widgets 

        # List of Widgets to add to the layout
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for wid in widgets:  # wid stands for widgets 
            layout.addWidget(wid()) # Instantiate and add widget to the layout 

        # create a QLineEdit (textbox)
        self.textbox = QLineEdit() # Create a text input field 
        self.textbox.setPlaceholderText("Enter text here....")
        self.textbox.setText("Hello PyQt6")

        # Create a QPushButton to change the text value 
        self.button = QPushButton("Change Text")  # Create a button with text "Change Text"
        self.button.clicked.connect(self.change_text) # Connect button to change_text method

        # Add the textbox and button to the layout
        layout.addWidget(self.textbox)
        layout.addWidget(self.button)

        # Create the QWidget to hold the layout 
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the main window
        # This will expand to fll available space
        self.setCentralWidget(widget)
    
    def change_text(self):
        self.textbox.setText("New Text Value")

# Create a instance of QApplication
app = QApplication(sys.argv)
# Create an instance of the main window 
window = MainWindow()
window.show()
# Rub the event
app.exec()