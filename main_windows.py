from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from check_meta import CheckMeta
from first import Ui_Widget


class MyWindow(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.toolButton.clicked.connect(self.msg)
        self.pushButton.clicked.connect(self.check_meta)

        self.file = ""

    def msg(self):
        self.file, filetype = QFileDialog.getOpenFileName(self, "选取文件", "", "Excel Files (*.xlsx);;Excel Files (*.xls)")  # 起始路径
        self.lineEdit.setText(self.file)
        print(self.file)

    def check_meta(self):
        cm = CheckMeta(self.file)
        text = cm.open_website()
        self.textBrowser.setText(text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
