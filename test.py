import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

class JsonTableView(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('JSON Table View')

        self.table = QTableWidget()
        self.table.setColumnCount(len(self.data[0]))
        self.table.setHorizontalHeaderLabels(self.data[0].keys())
        self.populate_table()

        add_button = QPushButton('Add Row')
        add_button.clicked.connect(self.add_row)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(add_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def populate_table(self):
        for row_num, row_data in enumerate(self.data):
            self.table.insertRow(row_num)
            for col_num, (key, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_num, col_num, item)

    def add_row(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        for col_num, key in enumerate(self.data[0].keys()):
            item = QTableWidgetItem('')
            self.table.setItem(row_count, col_num, item)

if __name__ == '__main__':
    data = [
        {
            "List": "112",
            "Rapport de coupe": 100,
            "consomation ": 2.0,
            "model": "pico",
            "ref/couleur": "40384/15",
            "stock reel": None
        }
    ]

    app = QApplication(sys.argv)
    json_table_view = JsonTableView(data)
    json_table_view.show()
    sys.exit(app.exec_())
