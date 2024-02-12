from PyQt5.QtWidgets import QDialog,QComboBox,QPushButton, QVBoxLayout , QLabel, QLineEdit, QDialog, QFormLayout, QMessageBox
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

