import sys
from PyQt5 import QtWidgets, uic

from MainWindow import Ui_cake_calc


class MainWindow(QtWidgets.QMainWindow, Ui_cake_calc):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        used_1 = float(self.lineEdit_1.text())
        used_2 = float(self.lineEdit_4.text())
        used_3 = float(self.lineEdit_7.text())
        total_1 = float(self.lineEdit_2.text())
        total_2 = float(self.lineEdit_5.text())
        total_3 = float(self.lineEdit_8.text())
        price_1 = float(self.lineEdit_3.text())
        price_2 = float(self.lineEdit_6.text())
        price_3 = float(self.lineEdit_9.text())
        res = 'Result sum: '+ str(round(used_1*price_1/total_1+used_2*price_2/total_2+used_3*price_3/total_3, 3))
        self.textEdit.setText(res)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
