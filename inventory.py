import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox,QPushButton, QVBoxLayout ,QHBoxLayout, QLabel, QLineEdit, QDialog, QFormLayout, QMessageBox
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import sqlite3


class AddItemDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add New Item')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        model_name_label = QLabel('Model Name:')
        self.model_name_input = QLineEdit()

        fournitures_label = QLabel('Fournitures:')
        self.fournitures_dropdown = QComboBox()
        self.fournitures_dropdown.addItems(["Elastique", "Boutton", "Fils", "Fermeture/Glissiere"])
        self.fournitures_dropdown.currentIndexChanged.connect(self.on_fournitures_changed)

        self.ref_dropdown = QComboBox()
        self.ref_dropdown.addItems(["430362/135", "430362/491", "40384/012", "40384/013","40384/015"])
        self.ref_dropdown.setVisible(False)

        ref_label = QLabel('Ref/COULEUR:')
        
        stock_initial_label = QLabel('Stock Initial:')

        self.couleur_input = QLineEdit()
        self.stock_initial_input = QLineEdit()

        add_button = QPushButton('Add to Database')
        add_button.clicked.connect(self.add_item_to_database)

        form_layout = QFormLayout()
        form_layout.addRow(model_name_label, self.model_name_input)
        form_layout.addRow(fournitures_label, self.fournitures_dropdown)
        form_layout.addRow(ref_label, self.ref_dropdown)

        form_layout.addRow(stock_initial_label, self.stock_initial_input)

        layout.addLayout(form_layout)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def on_fournitures_changed(self, index):
        if self.fournitures_dropdown.currentText() == "Boutton":
            self.ref_dropdown.setVisible(True)
        else:
            self.ref_dropdown.setVisible(False)

    def add_item_to_database(self):
        model_name = self.model_name_input.text()
        fournitures = self.fournitures_dropdown.currentText()
        ref = self.ref_dropdown.currentText() if self.ref_dropdown.isVisible() else None
        couleur = self.couleur_input.text()
        stock_initial = self.stock_initial_input.text()

        if model_name and fournitures and couleur and stock_initial:
            try:
                stock_initial = int(stock_initial)
                # Add the item to the database (Assuming a SQLite database named fstock.db)
                conn = sqlite3.connect('fstock.db')
                c = conn.cursor()
                c.execute("INSERT INTO items (model_name, fournitures, ref/COULEUR, stock_initial) VALUES (?, ?, ?, ?)",
                          (model_name, fournitures, ref, couleur, stock_initial))
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Item Added", "Item added to the database successfully!")
                self.close()
            except ValueError:
                QMessageBox.warning(self, "Invalid Input", "Stock Initial must be an integer.")
        else:
            QMessageBox.warning(self, "Missing Information", "Please fill in all the fields.")

class LutexStockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lutex Stock')
        self.setGeometry(100, 100, 600, 400)

        # Create the title label
        title_label = QLabel('GESTION DE STOCK, LUTEX ', self)
        title_label.setFont(QFont('Arial', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)

        # Create the "Add a new model" button
        add_model_button = QPushButton('Add a new model', self)
        add_model_button.setFont(QFont('Arial', 16))
        add_model_button.setStyleSheet("background-color: #4CAF50; color: white; border: 2px solid #4CAF50; border-radius: 10px; padding: 10px 20px;")
        add_model_button.clicked.connect(self.open_add_item_dialog)

        # Create the image labels for the four categories
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

        # Set the main layout for the home page
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(add_model_button, alignment=Qt.AlignCenter)
        main_layout.addLayout(category_buttons_layout)


        self.setLayout(main_layout)
        self.show()

    def open_add_item_dialog(self):
        dialog = AddItemDialog()
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lutex_stock = LutexStockApp()
    sys.exit(app.exec_())
