import re
import requests
import sqlite3
from bs4 import BeautifulSoup as bsoup
from PyQt6 import QtCore, QtGui, QtWidgets
import pingspeed
import tablebd
from database import Database
from Parsik import Paarser

class Ui_FastProxy(object):
    def __init__(self):
        pass

    def setupUi(self, FastProxy):
        FastProxy.setObjectName("FastProxy")
        FastProxy.resize(531, 137)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        FastProxy.setFont(font)
        FastProxy.setAcceptDrops(False)
        FastProxy.setStyleSheet(
            "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        FastProxy.setModal(False)
        self.toolButton = QtWidgets.QToolButton(FastProxy)
        self.toolButton.setGeometry(QtCore.QRect(30, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(FastProxy)
        self.toolButton_2.setGeometry(QtCore.QRect(190, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(FastProxy)
        self.toolButton_3.setGeometry(QtCore.QRect(360, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.toolButton_3.setObjectName("toolButton_3")

        self.retranslateUi(FastProxy)
        QtCore.QMetaObject.connectSlotsByName(FastProxy)

        self.add_functions()

    def retranslateUi(self, FastProxy):
        _translate = QtCore.QCoreApplication.translate
        FastProxy.setWindowTitle(_translate("FastProxy", "FastProxy"))
        self.toolButton.setText(_translate("FastProxy", "Показать"))
        self.toolButton_2.setText(_translate("FastProxy", "Очистить"))
        self.toolButton_3.setText(_translate("FastProxy", "Проверить"))

    def add_functions(self):
        self.toolButton.clicked.connect(self.write_bd)
        self.toolButton.clicked.connect(self.Test)
        self.toolButton_2.clicked.connect(self.delete_bd)
        self.toolButton_3.clicked.connect(self.pingvich)


    def write_bd(self):

        urls = {'https://free.proxy-sale.com/',
                'http://foxtools.ru/Proxy',
                'https://best-proxies.ru/proxylist/free/',
                'https://www.freeproxy.world/',
                'https://www.proxy-list.download/HTTP'}
        for url in urls:
            Paarser(url)
        db = Database()

        rows = db.cursorObj.execute('''SELECT *
        FROM users''').fetchall()
        i = 0

        for row in rows:
            if i == 10:
                break

            ip = row[0]
            port = row[1]
            type = row[2]
            country = row[3]
            speed = row[4]
            print(ip,port,type,country,speed)
            i+=1
        db.close()
    def delete_bd(self):
        d = Database()
        d.delete()
    def Test(self):
        tablebd.window.show()
        tablebd.window.setGeometry(950, 650, 550, 350)
    def pingvich(self):
        pingspeed.see.show()
        FastProxy.hide()

def main():
    pass

if __name__ == "__main__":
    main()
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FastProxy = QtWidgets.QDialog()
    ui = Ui_FastProxy()
    ui.setupUi(FastProxy)
    FastProxy.show()
    sys.exit(app.exec())