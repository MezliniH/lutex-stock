import sys
from PyQt5.QtWidgets import QApplication
from Main_window import LutexStockApp
from Add_item_dialog import AddItemDialog
from Database import Database

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lutex_stock = LutexStockApp()
    sys.exit(app.exec_())
