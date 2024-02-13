# main.py

from lutex_stock_app import LutexStockApp
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lutex_stock = LutexStockApp()
    sys.exit(app.exec_())
