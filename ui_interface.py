from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *




import icons_rc

class Ui_Fournitures(object):
    def setupUi(self, Fournitures):
        if not Fournitures.objectName():
            Fournitures.setObjectName(u"Fournitures")
        Fournitures.resize(718, 450)
        self.centralwidget = QWidget(Fournitures)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menu = QFrame(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.boutons = QPushButton(self.menu)
        self.boutons.setObjectName(u"boutons")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.boutons.setIcon(icon)

        self.verticalLayout.addWidget(self.boutons)

        self.fils = QPushButton(self.menu)
        self.fils.setObjectName(u"fils")
        self.fils.setIcon(icon)

        self.verticalLayout.addWidget(self.fils)

        self.fermetures = QPushButton(self.menu)
        self.fermetures.setObjectName(u"fermetures")
        self.fermetures.setIcon(icon)

        self.verticalLayout.addWidget(self.fermetures)

        self.elastiques = QPushButton(self.menu)
        self.elastiques.setObjectName(u"elastiques")
        self.elastiques.setIcon(icon)

        self.verticalLayout.addWidget(self.elastiques)

        self.userguide = QPushButton(self.menu)
        self.userguide.setObjectName(u"userguide")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userguide.setIcon(icon1)

        self.verticalLayout.addWidget(self.userguide)

        self.dashboard = QPushButton(self.menu)
        self.dashboard.setObjectName(u"dashboard")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard.setIcon(icon2)

        self.verticalLayout.addWidget(self.dashboard)

        self.faq = QPushButton(self.menu)
        self.faq.setObjectName(u"faq")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.faq.setIcon(icon3)

        self.verticalLayout.addWidget(self.faq)


        self.horizontalLayout.addWidget(self.menu)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        Fournitures.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fournitures)

        QMetaObject.connectSlotsByName(Fournitures)

        self.boutons.clicked.connect(self.showOtherUI)
        def showOtherUI(self):
            # Remove the import statement here
            # from PySide2.QtUiTools import QUiLoader  # Import QUiLoader here

            # Load the other UI file
            loader = QUiLoader()
            file = QFile("buttons.ui")
            file.open(QFile.ReadOnly)
            other_ui = loader.load(file)
            file.close()

            # Create a dialog to show the loaded UI
            dialog = QDialog()
            layout = QVBoxLayout()
            layout.addWidget(other_ui)
            dialog.setLayout(layout)
            dialog.exec_()
    # setupUi



    def retranslateUi(self, Fournitures):
        Fournitures.setWindowTitle(QCoreApplication.translate("Fournitures", u"MainWindow", None))
        self.boutons.setText(QCoreApplication.translate("Fournitures", u"Boutons", None))
        self.fils.setText(QCoreApplication.translate("Fournitures", u"Fils", None))
        self.fermetures.setText(QCoreApplication.translate("Fournitures", u"Fermetures", None))
        self.elastiques.setText(QCoreApplication.translate("Fournitures", u"Elastiques", None))
        self.userguide.setText(QCoreApplication.translate("Fournitures", u"User guide", None))
        self.dashboard.setText(QCoreApplication.translate("Fournitures", u"Dashboard", None))
        self.faq.setText(QCoreApplication.translate("Fournitures", u"FAQ", None))
    # retranslateUi


    
