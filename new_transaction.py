# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(316, 337)
        Dialog.setMaximumSize(QSize(1677721, 1677721))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 \n"
"rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235),  stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255,  255,  30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.btn_section = QComboBox(self.frame)
        self.btn_section.addItem("")
        self.btn_section.addItem("")
        self.btn_section.addItem("")
        self.btn_section.addItem("")
        self.btn_section.addItem("")
        self.btn_section.setObjectName(u"btn_section")
        self.btn_section.setStyleSheet(u"QComboBox {\n"
"font-size: 20pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.btn_section)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.date.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.date.setKeyboardTracking(True)
        self.date.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))

        self.verticalLayout.addWidget(self.date)

        self.lbl_description = QLineEdit(self.frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.lbl_description)

        self.lbl_balance = QLineEdit(self.frame)
        self.lbl_balance.setObjectName(u"lbl_balance")
        self.lbl_balance.setStyleSheet(u"font-size: 18pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.lbl_balance)

        self.btn_category = QComboBox(self.frame)
        self.btn_category.addItem("")
        self.btn_category.addItem("")
        self.btn_category.setObjectName(u"btn_category")
        self.btn_category.setStyleSheet(u"QComboBox {\n"
"font-size: 18pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.btn_category)

        self.lbl_save = QPushButton(self.frame)
        self.lbl_save.setObjectName(u"lbl_save")
        self.lbl_save.setStyleSheet(u"QPushButton {\n"
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
        self.lbl_save.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.lbl_save)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.btn_section.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u" New Transaction", None))
        self.btn_section.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.btn_section.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.btn_section.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.btn_section.setItemText(3, QCoreApplication.translate("Dialog", u"Others", None))
        self.btn_section.setItemText(4, QCoreApplication.translate("Dialog", u"Travel", None))

        self.btn_section.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.lbl_description.setText("")
        self.lbl_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.lbl_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.btn_category.setItemText(0, QCoreApplication.translate("Dialog", u"income", None))
        self.btn_category.setItemText(1, QCoreApplication.translate("Dialog", u"outcome", None))

        self.lbl_save.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

