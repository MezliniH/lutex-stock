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
        # self.delete.clicked.connect(self.delete_row)  # Connect the Delete button to delete_row method

    def table_setup(self):
        self.tab.setColumnCount(6)
        self.tab.setHorizontalHeaderLabels(['List', 'model', 'ref/couleur', 'rapport de coupe', 'consomation', 'stock reel'])

    def get_data(self):
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            command = '''SELECT s.*, p.stock FROM stock s INNER JOIN products p ON s.ref_couleur = p.ref_couleur'''

            result = cursor.execute(command)
            self.tab.setRowCount(0)

            for row_count, row_data in enumerate(result):
                self.tab.insertRow(row_count)
                for column_count, data in enumerate(row_data):
                    if column_count == 5:  # Check if it's the "stock" column
                        stock = data
                    self.tab.setItem(row_count, column_count, QTableWidgetItem(str(data)))

                consomation = float(self.tab.item(row_count, 4).text())
                rapport_de_coupe = float(self.tab.item(row_count, 3).text())
                stock_reel = stock - (consomation * rapport_de_coupe)

                self.tab.setItem(row_count, 5, QTableWidgetItem(str(stock_reel)))


     
    def add_row(self):
        row_data = ["", "", "", "", "", ""]
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            command = ''' INSERT INTO stock VALUES (?, ?, ?, ?, ?, ?) '''
            cursor.execute(command,row_data)
            db.commit()

            self.get_data()  # Refresh the table after adding new row


    

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
