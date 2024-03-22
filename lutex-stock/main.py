import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QFile, QTextStream

app = QApplication(sys.argv)

# Load the interface.ui file
interfaceFile = QFile("interface.ui")
interfaceFile.open(QFile.ReadWrite)
stream = QTextStream(interfaceFile)
interfaceData = stream.readAll()
interfaceWidget = QWidget()
interfaceWidget.setLayout(QVBoxLayout())  # Set layout as needed
interfaceWidget.setWindowTitle("Interface UI")
interfaceWidget.setGeometry(100, 100, 400, 200)  # Set geometry as needed
interfaceFile.close()

# Load the buttons.ui file
buttonsFile = QFile("buttons.ui")
buttonsFile.open(QFile.ReadWrite)
stream = QTextStream(buttonsFile)
buttonsData = stream.readAll()
buttonsWidget = QWidget()
buttonsWidget.setLayout(QVBoxLayout())  # Set layout as needed
buttonsWidget.setWindowTitle("Buttons UI")
buttonsWidget.setGeometry(100, 100, 400, 200)  # Set geometry as needed
buttonsFile.close()

# Find the QPushButton in the interface.ui file
bouton = QPushButton("Click me", interfaceWidget)
bouton.setObjectName("bouton")

# Connect the button click signal to switch to the buttons.ui file
def show_buttons():
    buttonsWidget.show()

bouton.clicked.connect(show_buttons)

interfaceWidget.show()

sys.exit(app.exec_())
