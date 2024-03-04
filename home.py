import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFrame, QGridLayout, QSplitter, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize
from stock import StockManagement

class LutexStockApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GESTION DE STOCK, LUTEX')

        title_label = QLabel("Supplies Management System")
        title_label.setFont(QFont('Segoe UI', 20))

        sidebar_frame = QFrame()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(0)

        sidebar_buttons = ["Admin Dashboard", "User Guide", "FAQ"]
        for button_text in sidebar_buttons:
            sidebar_button = QPushButton(button_text, self)
            sidebar_button.setFont(QFont('Segoe UI', 12))
            sidebar_button.setStyleSheet("background-color: #333; color: white; border: none; padding: 10px 20px;")
            sidebar_layout.addWidget(sidebar_button)

        sidebar_frame.setLayout(sidebar_layout)

        button_names = ["Bouton", "Elastique", "Fils", "Fermeture/Glissier"]
        image_paths = ["button_icon.png", "elastic_icon.png", "thread_icon.png", "zipper_icon.png"]
        category_buttons_widget = QWidget()
        category_buttons_layout = QGridLayout(category_buttons_widget)
        for index, (name, path) in enumerate(zip(button_names, image_paths)):
            category_button = QPushButton(name, self)
            category_button.setStyleSheet("background-color: #0078D7; color: white; border: 2px solid #0078D7; border-radius: 50px; padding: 20px;")
            category_button.setFont(QFont('Segoe UI', 14))
            icon = QIcon(QPixmap(path))
            category_button.setIcon(icon)
            category_button.setIconSize(icon.actualSize(QSize(100, 100)))
            category_button.setFixedSize(200, 200)
            category_buttons_layout.addWidget(category_button, index // 2, index % 2)

            if name == "Bouton":
                category_button.clicked.connect(self.open_stock_management)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(sidebar_frame)
        splitter.addWidget(category_buttons_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addWidget(splitter)

        self.setLayout(main_layout)
        self.show()

    def open_stock_management(self):
        self.stock_window = StockManagement()
        self.stock_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LutexStockApp()
    sys.exit(app.exec_())
