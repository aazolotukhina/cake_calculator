import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui


from MainWindow import Ui_cake_calc


class MainWindow(QtWidgets.QMainWindow, Ui_cake_calc):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ings = []
        self.pushButton.clicked.connect(self.btnClicked)
        self.pushButton_3.clicked.connect(self.setIngreds)
        self.pushButton_2.clicked.connect(self.clearIngreds)

    def setIngreds(self):
        self.rows_number = self.spinBox.value()

        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidget)
        self.scrollAreaWidgetLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.scrollArea.setWidget(self.scrollAreaWidget)

        for count in range(0,self.rows_number):
            groupBox = QtWidgets.QGroupBox(self.scrollAreaWidget)
            self.scrollAreaWidgetLayout.insertWidget(count, groupBox)

            gridLayout = QtWidgets.QGridLayout(groupBox)
            gridLayout.addWidget(QtWidgets.QLabel('Ingridient ' + str(count+1), groupBox),1, 0, 1, 1)
            self.lineEdit_1 = QtWidgets.QLineEdit(groupBox)
            gridLayout.addWidget(self.lineEdit_1, 1, 1, 1, 1)
            self.lineEdit_2 = QtWidgets.QLineEdit(groupBox)
            gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
            self.lineEdit_3 = QtWidgets.QLineEdit(groupBox)
            gridLayout.addWidget(self.lineEdit_3, 1, 3, 1, 1)
            self.ings.append((self.lineEdit_1, self.lineEdit_2, self.lineEdit_3))

    def clearIngreds(self):
        for count in range(0,self.rows_number):
            for j in [0,1,2]:
                self.ings[count][j].clear()
        self.textEdit.clear()


    def btnClicked(self):
        res = 0
        for i in range(0, self.rows_number):
            res = str(float(res) + float(self.ings[i][0].text())*float(self.ings[i][2].text())/float(self.ings[i][1].text()))
        self.textEdit.setText(res)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
