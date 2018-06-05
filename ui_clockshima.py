# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_clockshima.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        Main.setWindowOpacity(1.0)
        Main.setLayoutDirection(QtCore.Qt.LeftToRight)
        Main.setAutoFillBackground(False)
        self.digitalClock = QtWidgets.QLCDNumber(Main)
        self.digitalClock.setGeometry(QtCore.QRect(160, 80, 330, 100))
        self.digitalClock.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.digitalClock.setFrameShape(QtWidgets.QFrame.Panel)
        self.digitalClock.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.digitalClock.setLineWidth(8)
        self.digitalClock.setMidLineWidth(0)
        self.digitalClock.setSmallDecimalPoint(False)
        self.digitalClock.setDigitCount(8)
        self.digitalClock.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.digitalClock.setObjectName("digitalClock")
        self.scriptBox = QtWidgets.QPlainTextEdit(Main)
        self.scriptBox.setGeometry(QtCore.QRect(190, 190, 280, 70))
        self.scriptBox.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.scriptBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scriptBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scriptBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scriptBox.setReadOnly(True)
        self.scriptBox.setObjectName("scriptBox")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Clockshima"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

