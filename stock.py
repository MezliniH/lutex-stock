import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QComboBox

import sqlite3

class StockManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stock Management')

        self.add_stock_button = QPushButton("Add Stock")
        self.add_stock_button.clicked.connect(self.show_add_stock_form)

        self.read_stock_button = QPushButton("Read Stock")
        self.read_stock_button.clicked.connect(self.show_stock_table)

        self.ref_color_label = QLabel("Ref/Color:")
        self.ref_color_input = QLineEdit()

        self.initial_stock_label = QLabel("Initial Stock:")
        self.initial_stock_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_stock_item)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["List", "ID Model", "Ref/Color", "Total des Pontallons", "Consumption", "Stock Reel"])

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.add_stock_button)
        self.layout.addWidget(self.read_stock_button)
        self.setLayout(self.layout)

        # Connect to SQLite database
        self.conn = sqlite3.connect('stock_database.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
                ref_color TEXT PRIMARY KEY,
                initial_stock INTEGER
            )
        ''')
        self.conn.commit()

    def show_add_stock_form(self):
        self.clear_layout()
        self.layout.addWidget(self.ref_color_label)
        self.layout.addWidget(self.ref_color_input)
        self.layout.addWidget(self.initial_stock_label)
        self.layout.addWidget(self.initial_stock_input)
        self.layout.addWidget(self.submit_button)
        self.setLayout(self.layout)

    def add_stock_item(self):
        ref_color = self.ref_color_input.text()
        initial_stock = self.initial_stock_input.text()

        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO stock (ref_color) VALUES (?)', (ref_color,))
        self.conn.commit()

    def show_stock_table(self):
        self.clear_layout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM stock')
        data = cursor.fetchall()

        self.table.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                if col_num == 2:  # Ref/Color column index
                    combo_box = QComboBox()
                    combo_box.addItems([col_data])
                    self.table.setCellWidget(row_num, col_num, combo_box)
                else:
                    item = QTableWidgetItem(str(col_data))
                    self.table.setItem(row_num, col_num, item)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

# Test the StockManagement class
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StockManagement()
    window.show()
    sys.exit(app.exec_())