import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUiType
import os
import sqlite3

FORM_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'buttons.ui'))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.handel_buttons()
        self.table_setup()

    def handel_buttons(self):
        self.refresh.clicked.connect(self.get_data)
        self.add.clicked.connect(self.add_row)

    def table_setup(self):
        self.tab.setColumnCount(6)
        self.tab.setHorizontalHeaderLabels(['nom de list', 'model', 'ref/couleur', 'stock', 'rapport de coupe', 'consomation', 'stock_reel'])

    def add_row(self):
        row_data = [
            self.nom_de_list.text(),
            self.model.text(),
            self.ref_couleur.text(),
            float(self.stock.text()),
            float(self.rapport_de_coupe.text()),
            float(self.consomation.text()),
            float(self.stock_reel.text())
        ]

        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            command = '''INSERT INTO stock (nom de list, model, ref_couleur, stock, rapport_de_coupe, consomation, stock_reel) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(command, row_data)
            db.commit()

            self.get_data()  # Refresh the table after adding new row

    def get_data(self):
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            command = '''SELECT * FROM stock'''

            result = cursor.execute(command)
            self.tab.setRowCount(0)

            for row_count, row_data in enumerate(result):
                self.tab.insertRow(row_count)
                stock = row_data[5]
                consomation = row_data[4]
                rapport_de_coupe = row_data[3]
                stock_reel = stock - (consomation * rapport_de_coupe)

                for column_count, data in enumerate(row_data):
                    self.tab.setItem(row_count, column_count, QTableWidgetItem(str(data)))

                self.tab.setItem(row_count, 6, QTableWidgetItem(str(stock_reel)))


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
