import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUiType
import os
import sqlite3
import json

FORM_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'buttons.ui'))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.handel_buttons()
        self.table_setup()
        self.calculate_stock_reel_for_existing_rows()  # Calculate stock reel for existing rows
        self.calculer.clicked.connect(self.refresh_stock_reel)
        self.vue.clicked.connect(self.load_all_records)
        self.update.clicked.connect(self.update_stock)



    def update_stock(self):
        ref_couleur = self.refedit.text()
        stock = self.stockedit.text()

        if not ref_couleur or not stock:
            self.statusBar().showMessage("Both ref_couleur and stock must be provided.")
            return

        data = {}

        try:
            with open("stock_data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            pass

        data[ref_couleur] = stock

        with open("stock_data.json", "w") as file:
            json.dump(data, file, indent=4)

        self.statusBar().showMessage("Stock data updated successfully.")


    def refresh_stock_reel(self):
        if self.check_ref_couleur_and_stock_existence():
            self.calculate_stock_reel_for_existing_rows()



    def calculate_stock_reel_for_existing_rows(self):
        for row in range(self.tab.rowCount()):
            stock = float(self.tab.item(row, 3).text()) if self.tab.item(row, 3) else 0
            rapport_de_coupe = float(self.tab.item(row, 4).text()) if self.tab.item(row, 4) else 0
            consommation = float(self.tab.item(row, 5).text()) if self.tab.item(row, 5) else 0
            stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)
            item = QTableWidgetItem(str(stock_reel))
            self.tab.setItem(row, 6, item)

            # Update stock reel in the database
            with sqlite3.connect("lutexdb") as db:
                cursor = db.cursor()
                command = '''UPDATE stock SET stock_reel = ? WHERE rowid = ?'''
                cursor.execute(command, (stock_reel, row + 1))  # rowid starts from 1 in SQLite
                db.commit()



    def check_ref_couleur_and_stock_existence(self):
        with open("stock_data.json", "r") as file:
            existing_data = json.load(file)

        for row in range(self.tab.rowCount()):
            ref_couleur = self.tab.item(row, 2).text()
            stock_text = self.tab.item(row, 3).text() if self.tab.item(row, 3) else ''
            try:
                stock_user = float(stock_text)
            except ValueError:
                QMessageBox.critical(self, "Error", f"Invalid stock value '{stock_text}' for ref_couleur '{ref_couleur}'.")
                return False

            if ref_couleur not in existing_data:
                QMessageBox.critical(self, "Error", f"Ref_couleur '{ref_couleur}' not found in JSON file.")
                return False        
                

    def calculate_stock_reel_for_existing_rows(self):
        for row in range(self.tab.rowCount()):
            stock = float(self.tab.item(row, 3).text() or 0)
            rapport_de_coupe = float(self.tab.item(row, 4).text() or 0)
            consommation = float(self.tab.item(row, 5).text() or 0)
            stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)
            item = QTableWidgetItem(str(stock_reel))
            self.tab.setItem(row, 6, item)

            # Update stock reel in the database
            with sqlite3.connect("lutexdb") as db:
                cursor = db.cursor()
                command = '''UPDATE stock SET stock_reel = ? WHERE rowid = ?'''
                cursor.execute(command, (stock_reel, row + 1))  # rowid starts from 1 in SQLite
                db.commit()
    
    
    def handel_buttons(self): 
        self.add.clicked.connect(self.add_row)

    def table_setup(self):
        self.tab.setColumnCount(7)
        self.tab.setHorizontalHeaderLabels(['liste', 'model', 'ref_couleur', 'stock', 'rapport_de_coupe', 'consommation', 'stock_reel'])

    def calculate_stock_reel(self, stock, consommation, rapport_de_coupe):
        return stock - (consommation * rapport_de_coupe)

    def add_row(self):
        row_data = [
            self.tab.item(row, col).text() if self.tab.item(row, col) is not None else ''
            for row in range(self.tab.rowCount())
            for col in range(self.tab.columnCount())
        ]

        self.tab.insertRow(self.tab.rowCount())
        for col, data in enumerate(row_data):
            item = QTableWidgetItem(data)
            self.tab.setItem(self.tab.rowCount() - 1, col, item)

        # Check if row_data contains enough elements
        if len(row_data) < 6:
            # Insufficient data, cannot add row
            return

        # Calculate and insert stock reel for the new row
        stock = float(row_data[3]) if row_data[3] else 0
        rapport_de_coupe = float(row_data[4]) if row_data[4] else 0
        consommation = float(row_data[5]) if row_data[5] else 0
        stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)

        # Insert data into the database
        data_to_insert = row_data[:3] + [stock, rapport_de_coupe, consommation, stock_reel]  # Extracting necessary values from row_data
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            command = '''INSERT INTO stock ("liste", model, ref_couleur, stock, "rapport_de_coupe", consommation, stock_reel) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            cursor.execute(command, data_to_insert)
            db.commit()




    def calculate_stock_reel_for_existing_rows(self):
        for row in range(self.tab.rowCount()):
            stock = float(self.tab.item(row, 3).text()) if self.tab.item(row, 3) else 0
            consommation = float(self.tab.item(row, 5).text()) if self.tab.item(row, 5) else 0
            rapport_de_coupe = float(self.tab.item(row, 4).text()) if self.tab.item(row, 4) else 0
            stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)
            item = QTableWidgetItem(str(stock_reel))
            self.tab.setItem(row, 6, item)

            # Update stock reel in the database
            with sqlite3.connect("lutexdb") as db:
                cursor = db.cursor()
                command = '''UPDATE stock SET stock_reel = ? WHERE rowid = ?'''
                cursor.execute(command, (stock_reel, row + 1))  # rowid starts from 1 in SQLite
                db.commit()

    def load_all_records(self):
        self.load_data_from_database()  # Load all records from the database

    def load_data_from_database(self):
        # Clear the current table contents
        self.tab.setRowCount(0)

        # Fetch all records from the database and populate the table
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM stock''')
            rows = cursor.fetchall()
            for row_index, row_data in enumerate(rows):
                self.tab.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tab.setItem(row_index, col_index, item)




def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
