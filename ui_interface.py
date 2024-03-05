# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"*{border: none; background-color:transparent;color:#fff;}\n"
"#centralwidget{ background-color: #040f13;}\n"
"#side_menu{\n"
"background-color: #071e25; border-radius: 20px;}\n"
"QPushButton{ padding: 10px;\n"
"background-color: #2b3137;\n"
"border-radius: 5px;}\n"
"#main_body{\n"
"background-color: #071e25; border-radius: 10px;}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_menu = QFrame(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.boutons = QPushButton(self.frame_4)
        self.boutons.setObjectName(u"boutons")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boutons.setIcon(icon)

        self.gridLayout.addWidget(self.boutons, 0, 0, 1, 1)

        self.fermetures = QPushButton(self.frame_4)
        self.fermetures.setObjectName(u"fermetures")
        self.fermetures.setIcon(icon)

        self.gridLayout.addWidget(self.fermetures, 1, 0, 1, 1)

        self.elastiques = QPushButton(self.frame_4)
        self.elastiques.setObjectName(u"elastiques")
        self.elastiques.setIcon(icon)

        self.gridLayout.addWidget(self.elastiques, 2, 0, 1, 1)

        self.fils = QPushButton(self.frame_4)
        self.fils.setObjectName(u"fils")
        self.fils.setIcon(icon)

        self.gridLayout.addWidget(self.fils, 3, 0, 1, 1)

        self.userguide = QPushButton(self.frame_4)
        self.userguide.setObjectName(u"userguide")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userguide.setIcon(icon1)

        self.gridLayout.addWidget(self.userguide, 4, 0, 1, 1)

        self.dashboard = QPushButton(self.frame_4)
        self.dashboard.setObjectName(u"dashboard")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard.setIcon(icon2)

        self.gridLayout.addWidget(self.dashboard, 5, 0, 1, 1)

        self.faq = QPushButton(self.frame_4)
        self.faq.setObjectName(u"faq")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.faq.setIcon(icon3)

        self.gridLayout.addWidget(self.faq, 6, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.body = QLabel(self.main_body)
        self.body.setObjectName(u"body")
        self.body.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.body)


        self.horizontalLayout.addWidget(self.main_body)


        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setStyleSheet(u"background-color: rgb(7, 30, 37);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 100, 48))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Menu = QPushButton(self.frame)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(0, 30))
        self.Menu.setMaximumSize(QSize(16777215, 30))
        self.Menu.setStyleSheet(u"background-color: rgb(43, 49, 55);\n"
"font: 75 10pt \"Noto Sans\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon4)

        self.verticalLayout.addWidget(self.Menu)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(440, 0, 219, 42))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.titre = QLabel(self.frame_3)
        self.titre.setObjectName(u"titre")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.titre)


        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boutons.setText(QCoreApplication.translate("MainWindow", u"Boutons", None))
        self.fermetures.setText(QCoreApplication.translate("MainWindow", u"Fermetures", None))
        self.elastiques.setText(QCoreApplication.translate("MainWindow", u"Elastiques", None))
        self.fils.setText(QCoreApplication.translate("MainWindow", u"Fils", None))
        self.userguide.setText(QCoreApplication.translate("MainWindow", u"User guide", None))
        self.dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.faq.setText(QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.body.setText(QCoreApplication.translate("MainWindow", u"MAIN-BODY", None))
        self.Menu.setText(QCoreApplication.translate("MainWindow", u" MENU", None))
        self.titre.setText(QCoreApplication.translate("MainWindow", u"Stock fournitures Lutex", None))
    # retranslateUi

