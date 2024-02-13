# lutex_stock_app.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize  # Import QSize from PyQt5.QtCore
from add_item_dialog import AddItemDialog  # Import the AddItemDialog from the separate file

class LutexStockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GESTION DE STOCK, LUTEX')
        
        title_label = QLabel("LUTEX Stock Management System")
        title_label.setFont(QFont('Arial', 20))

        add_model_button = QPushButton('Add a new model', self)
        add_model_button.setFont(QFont('Arial', 16))
        add_model_button.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50; border-radius: 10px; padding: 10px 20px;")
        add_model_button.clicked.connect(self.open_add_item_dialog)

        button_names = ["Bouton", "Elastique", "Fils", "Fermeture/Glissier"]
        image_paths = ["button_icon.png", "elastic_icon.png", "thread_icon.png", "zipper_icon.png"]
        category_buttons_layout = QHBoxLayout()
        for name, path in zip(button_names, image_paths):
            category_button = QPushButton(name, self)
            category_button.setStyleSheet("background-color: #008CBA; color: white; border: 2px solid #008CBA; border-radius: 50px; padding: 20px;")
            category_button.setFont(QFont('Arial', 14))
            icon = QIcon(QPixmap(path))
            category_button.setIcon(icon)
            category_button.setIconSize(icon.actualSize(QSize(100, 100)))
            category_button.setFixedSize(200, 200)
            category_buttons_layout.addWidget(category_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(add_model_button, alignment=Qt.AlignCenter)
        main_layout.addLayout(category_buttons_layout)

        self.setLayout(main_layout)
        self.show()

    def open_add_item_dialog(self):
        dialog = AddItemDialog()
        dialog.exec_()
