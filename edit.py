import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import json

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("buttons.ui", self)
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

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
