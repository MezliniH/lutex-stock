# Import necessary modules
from PySide2.QtCore import QRect, QEasingCurve, QPropertyAnimation

# Add the animation code within the class definition
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Existing code for setting up UI elements
        
        # Define the animation properties
        animation = QPropertyAnimation(self.frame_3, b"geometry")
        animation.setDuration(500)  # Animation duration in milliseconds
        animation.setEasingCurve(QEasingCurve.OutCubic)  # Easing curve for smooth animation

        # Define the start and end positions for the animation
        start_pos = QRect(440, 0, 0, 50)  # Initial position outside the window
        end_pos = QRect(0, 0, 440, 50)    # Final position at the desired location
        animation.setStartValue(start_pos)
        animation.setEndValue(end_pos)

        # Start the animation when the button is clicked
        def animate_sidebar():
            animation.start()

        # Connect the button click event to the animation function
        self.pushButton.clicked.connect(animate_sidebar)
