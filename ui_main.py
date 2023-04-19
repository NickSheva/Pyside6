# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 634)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 \n"
"rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235),  stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255,  255,  30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.lbl_balance = QLabel(self.balance_frame)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.lbl_current_balance = QLabel(self.balance_frame)
        self.lbl_current_balance.setObjectName(u"lbl_current_balance")
        self.lbl_current_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_current_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_income = QLabel(self.balance_frame)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setMaximumSize(QSize(24, 16777215))
        self.label_income.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_income.setPixmap(QPixmap(u":/icon/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.label_income)

        self.lbl_income = QLabel(self.balance_frame)
        self.lbl_income.setObjectName(u"lbl_income")
        self.lbl_income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.lbl_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_sum_income = QLabel(self.balance_frame)
        self.lbl_sum_income.setObjectName(u"lbl_sum_income")
        self.lbl_sum_income.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_sum_income)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_outcome = QLabel(self.balance_frame)
        self.icon_outcome.setObjectName(u"icon_outcome")
        self.icon_outcome.setMaximumSize(QSize(24, 16777215))
        self.icon_outcome.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.icon_outcome.setPixmap(QPixmap(u":/icon/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.icon_outcome)

        self.lbl_outcome = QLabel(self.balance_frame)
        self.lbl_outcome.setObjectName(u"lbl_outcome")
        self.lbl_outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.lbl_outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lbl_sum_outcome = QLabel(self.balance_frame)
        self.lbl_sum_outcome.setObjectName(u"lbl_sum_outcome")
        self.lbl_sum_outcome.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_sum_outcome)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255,  255,  30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_9 = QLabel(self.categories_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.icon_groceries = QLabel(self.categories_frame)
        self.icon_groceries.setObjectName(u"icon_groceries")
        self.icon_groceries.setMaximumSize(QSize(24, 16777215))
        self.icon_groceries.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icon/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_groceries)

        self.lbl_groceries_2 = QLabel(self.categories_frame)
        self.lbl_groceries_2.setObjectName(u"lbl_groceries_2")
        self.lbl_groceries_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 24pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_groceries_2)

        self.sum_groceries = QLabel(self.categories_frame)
        self.sum_groceries.setObjectName(u"sum_groceries")
        self.sum_groceries.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.sum_groceries)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_entertainment = QLabel(self.categories_frame)
        self.icon_entertainment.setObjectName(u"icon_entertainment")
        self.icon_entertainment.setMaximumSize(QSize(24, 16777215))
        self.icon_entertainment.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_entertainment.setPixmap(QPixmap(u":/icon/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_entertainment)

        self.lbl_entertainment = QLabel(self.categories_frame)
        self.lbl_entertainment.setObjectName(u"lbl_entertainment")
        self.lbl_entertainment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_entertainment)

        self.sum_entertainment = QLabel(self.categories_frame)
        self.sum_entertainment.setObjectName(u"sum_entertainment")
        self.sum_entertainment.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.sum_entertainment)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_auto = QLabel(self.categories_frame)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(24, 16777215))
        self.icon_auto.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icon/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icon_auto)

        self.sum_auto = QLabel(self.categories_frame)
        self.sum_auto.setObjectName(u"sum_auto")
        self.sum_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.sum_auto)

        self.label_18 = QLabel(self.categories_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_others = QLabel(self.categories_frame)
        self.icon_others.setObjectName(u"icon_others")
        self.icon_others.setMaximumSize(QSize(24, 16777215))
        self.icon_others.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.icon_others.setPixmap(QPixmap(u":/icon/icons/list_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_others)

        self.lbl_others = QLabel(self.categories_frame)
        self.lbl_others.setObjectName(u"lbl_others")
        self.lbl_others.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_others)

        self.sum_others = QLabel(self.categories_frame)
        self.sum_others.setObjectName(u"sum_others")
        self.sum_others.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.sum_others)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_new_transaction = QPushButton(self.centralwidget)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lbl_new_transaction.setIcon(icon)
        self.lbl_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.lbl_new_transaction)

        self.lbl_edit = QPushButton(self.centralwidget)
        self.lbl_edit.setObjectName(u"lbl_edit")
        self.lbl_edit.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lbl_edit.setIcon(icon1)
        self.lbl_edit.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.lbl_edit)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setMaximumSize(QSize(16777215, 16777215))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px, solid rgba(255, 255, 255, 40);\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView:items {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView:item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255, 50);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.horizontalHeader().setMinimumSectionSize(44)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExpenseApp", None))
        self.lbl_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.lbl_current_balance.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_income.setText("")
        self.lbl_income.setText(QCoreApplication.translate("MainWindow", u"income", None))
        self.lbl_sum_income.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.icon_outcome.setText("")
        self.lbl_outcome.setText(QCoreApplication.translate("MainWindow", u"outcome", None))
        self.lbl_sum_outcome.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Expense Categories", None))
        self.icon_groceries.setText("")
        self.lbl_groceries_2.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.sum_groceries.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_entertainment.setText("")
        self.lbl_entertainment.setText(QCoreApplication.translate("MainWindow", u"Entertaiment", None))
        self.sum_entertainment.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_auto.setText("")
        self.sum_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.icon_others.setText("")
        self.lbl_others.setText(QCoreApplication.translate("MainWindow", u"Others", None))
        self.sum_others.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.lbl_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

