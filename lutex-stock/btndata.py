import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import sqlite3
import json

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('buttons.ui', self)  # Load the UI from buttons.ui
        self.init_ui()
        self.load_all_records()

    def init_ui(self):
        self.add.clicked.connect(self.add_row)
        self.calculer.clicked.connect(self.calculate_stock_reel_for_existing_rows)
        self.updating.clicked.connect(self.update_stock)
        self.vue.clicked.connect(self.drop_row)

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

            if ref_couleur in existing_data and stock_user != existing_data[ref_couleur]['stock']:
                QMessageBox.critical(self, "Error", f"Stock value for ref_couleur '{ref_couleur}' does not match the existing data.")
                return False

        return True    



    def calculate_stock_reel(self, stock, consommation, rapport_de_coupe):
        return stock - (consommation * rapport_de_coupe)

    def add_row(self):
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            cursor.execute('''SELECT COUNT(*) FROM stock''')
            row_count = cursor.fetchone()[0]

            if row_count == 0:  # If lutexdb is empty, add a default row with 7 columns
                default_row = [''] * 7  # Create a default row with empty values
                cursor.execute('''INSERT INTO stock ("liste", model, ref_couleur, stock, "rapport_de_coupe", consommation, stock_reel) VALUES (?, ?, ?, ?, ?, ?, ?)''', default_row)
                db.commit()
            else:  # If there are existing rows, add a row normally
                row_data = [
                    self.tab.item(row, col).text() if self.tab.item(row, col) is not None else ''
                    for row in range(self.tab.rowCount())
                    for col in range(self.tab.columnCount())
                ]

                if len(row_data) < 6:
                    return

                stock = float(row_data[3]) if row_data[3] else 0
                rapport_de_coupe = float(row_data[4]) if row_data[4] else 0
                consommation = float(row_data[5]) if row_data[5] else 0
                stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)

                data_to_insert = row_data[:3] + [stock, rapport_de_coupe, consommation, stock_reel]
                cursor.execute('''INSERT INTO stock ("liste", model, ref_couleur, stock, "rapport_de_coupe", consommation, stock_reel) VALUES (?, ?, ?, ?, ?, ?, ?)''', data_to_insert)
                db.commit()

        self.load_all_records()

    def calculate_stock_reel_for_existing_rows(self):
        for row in range(self.tab.rowCount()):
            stock = float(self.tab.item(row, 3).text()) if self.tab.item(row, 3) else 0
            consommation = float(self.tab.item(row, 5).text()) if self.tab.item(row, 5) else 0
            rapport_de_coupe = float(self.tab.item(row, 4).text()) if self.tab.item(row, 4) else 0
            stock_reel = self.calculate_stock_reel(stock, consommation, rapport_de_coupe)
            item = QTableWidgetItem(str(stock_reel))
            self.tab.setItem(row, 6, item)

            with sqlite3.connect("lutexdb") as db:
                cursor = db.cursor()
                cursor.execute('''UPDATE stock SET stock_reel = ? WHERE rowid = ?''', (stock_reel, row + 1))
                db.commit()

    def load_all_records(self):
        self.tab.setRowCount(0)
        self.load_data_from_database()

    def load_data_from_database(self):
        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM stock''')
            rows = cursor.fetchall()
            for row_index, row_data in enumerate(rows):
                self.tab.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tab.setItem(row_index, col_index, item)


    def drop_row(self, selected_row):
        if selected_row is None:
            return

        liste_value = self.tab.item(selected_row, 0).text()  # Assuming the first column contains the 'liste' value

        with sqlite3.connect("lutexdb") as db:
            cursor = db.cursor()
            cursor.execute('''DELETE FROM stock WHERE "liste" = ?''', (liste_value,))
            db.commit()

        self.load_all_records()



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()