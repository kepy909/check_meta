# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 300)
        self.widget = Widget
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(190, 28, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(Widget)
        self.toolButton.setGeometry(QtCore.QRect(140, 30, 37, 18))
        self.toolButton.setObjectName("toolButton")
        self.textBrowser = QtWidgets.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 381, 221))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Meta检查"))
        self.pushButton.setText(_translate("Widget", "提交"))
        self.toolButton.setText(_translate("Widget", "浏览文件"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(widget)

    widget.show()
    sys.exit(app.exec_())
