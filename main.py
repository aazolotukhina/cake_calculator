import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui


from MainWindow import Ui_cake_calc


class MainWindow(QtWidgets.QMainWindow, Ui_cake_calc):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btnClicked)
        self.pushButton_3.clicked.connect(self.setIngreds)

    def setIngreds(self):
        rows_number = self.spinBox.value()
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.update()
        self.show()
#        self.gridLayout = QtWidgets.QGridLayout()
#        self.gridLayout.setObjectName("gridLayout")
#        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
#        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
#        self.label_5.setObjectName("label_5")
#        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
#        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
#        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
#        self.label_6.setObjectName("label_6")
#        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
#        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
#        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
#        self.label_7.setObjectName("label_7")
#        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

#        for i in range(1,rows_number):
#            self.label_2 = QtWidgets.QLabel(self.layoutWidget)
#            self.label_2.setObjectName("label_2")
#            self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
#            self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
#            self.lineEdit_1.setObjectName("lineEdit_1")
#            self.gridLayout.addWidget(self.lineEdit_1, 1, 1, 1, 1)
#            self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
#            self.lineEdit_2.setObjectName("lineEdit_2")
#            self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
#            self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
#            self.lineEdit_3.setObjectName("lineEdit_3")
#            self.gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.textEdit.setText(str(rows_number))


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
