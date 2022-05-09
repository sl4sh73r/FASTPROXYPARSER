import re
import requests
import sqlite3
from bs4 import BeautifulSoup as bsoup
from PyQt6 import QtCore, QtGui, QtWidgets

import tablebd
from database import Database



class  Paarser:
    def __init__(self, url):
        self.user_ip_list = []
        self.user_country_list = []
        self.user_speed_list = []
        self.user_port_list = []
        self.user_type_list = []
        if url == 'https://free.proxy-sale.com/':
            self.screb1(url)
        if url == 'http://foxtools.ru/Proxy':
            self.screb2(url)
        if url == 'https://best-proxies.ru/proxylist/free/':
            self.screb3(url)
        if url == 'https://www.freeproxy.world/':
            self.screb4(url)
        if url == 'https://www.proxy-list.download/HTTP':
            self.screb5(url)
            pass
    def clear(self):
        self.user_ip_list = []
        self.user_country_list = []
        self.user_speed_list = []
        self.user_port_list = []
        self.user_type_list = []
    def screb1(self, url1):

        #self.db.bd(user_ip_list, user_port_list, user_type_list, user_country_list, user_speed_list)
        page = requests.get(url1)
        result = bsoup(page.text, 'lxml')
        for el0 in result.find_all('td', class_='ip'):
            for el1 in el0.find_all('a'):
                user_IP = ((el1.text).split("\t")[0])
                self.user_ip_list.append(user_IP)

        for el00 in result.find_all('td', class_='country'):
            user_country = (el00.text.split()[0])
            self.user_country_list.append(user_country)

        for el00 in result.find_all('td'):
            for el0 in result.find_all('div', class_='progress-bar blue stripes'):
                for el1 in el0.find_all('i'):
                    user_speed = (el1.text).split(" мс")[0]
                    if user_speed != "":
                        self.user_speed_list.append(user_speed)

        for el0 in result.find_all('div', class_='kc-elm kc-css-517022 kc-raw-code'):
            el0 = re.sub(r'\s+', ' ', str(el0))
            _start = [i for i in range(len(el0)) if el0.startswith('attrPorts = attrPorts + "," + ', i)]
            _end = [i for i in range(len(el0)) if el0.startswith('</script>', i)]
            for i in range(len(_start)):
                self.user_port_list.append(int(el0[_start[i] + 30:_end[i] - 2]))

        for el0 in result.find_all('td'):
            for el1 in el0.find_all('a'):
                temp = ((el1.text).split('\t')[0])
                temp1 = (temp.split('\n')[0])
                user_type = ((re.sub('[^A-Z]', '', temp1)))
                self.user_type_list.append(user_type)
        user_type_list = [i for i in self.user_type_list if i]

        #db = Database().bd()
        Database().bd(self.user_ip_list, self.user_port_list, user_type_list, self.user_country_list, self.user_speed_list)
        self.clear()

    def screb2(self,url2):
        iter = []
        page = requests.get(url2)
        result = bsoup(page.text, 'lxml')

        for ell1 in result.find_all('td'):
            temp = ((ell1.text))
            iter.append(temp)
        for i in range(1, len(iter), 8):
            self.user_ip_list.append(iter[i])

        for i in range(2, len(iter), 8):
            self.user_port_list.append(iter[i])

        for i in range(3, len(iter), 8):
            self.user_country_list.append(iter[i])

        for i in range(5, len(iter), 8):
            tempp=((re.sub('[^A-Z]', '',iter[i])))
            self.user_type_list.append(str(tempp))


        for i in range(6, len(iter), 8):
            self.user_speed_list.append(iter[i])

        Database().bd(self.user_ip_list, self.user_port_list, self.user_type_list, self.user_country_list,
                      self.user_speed_list)
        self.clear()

    def screb3(self, url3):
        iter = []
        port = []
        ip = []
        country = []
        speed = []
        type = []
        page = requests.get(url3)
        result = bsoup(page.text, 'lxml')

        for ell1 in result.find_all('td'):
            temp = ((ell1.text))
            iter.append(temp)
        # print(iter)
        for i in range(1, len(iter), 8):
            port.append(iter[i])
            port = [line.strip() for line in port]
        self.user_port_list.extend(port[:10])
        for i in range(0, len(iter), 8):
            ip.append(iter[i])
            ip = [line.strip() for line in ip]
        self.user_ip_list.extend(ip[:10])
        for i in range(2, len(iter), 8):
            country.append(iter[i])
            country = [line.strip() for line in country]
        self.user_country_list.extend(country[:10])

        for i in range(4, len(iter), 8):
            speed.append(iter[i])
            speed = [line.strip() for line in speed]
        self.user_speed_list.extend(speed[:10])

        for i in range(5, len(iter), 8):
            type.append(iter[i])
            type = [line.strip() for line in type]
        self.user_type_list.extend(type[:10])

        Database().bd(self.user_ip_list, self.user_port_list, self.user_type_list, self.user_country_list,
                      self.user_speed_list)
        self.clear()

    def screb4(self, url4):
        iter = []
        port = []
        ip = []
        country = []
        speed = []
        type = []

        page = requests.get(url4)
        result = bsoup(page.text, 'lxml')
        for el2 in result.find_all('tr'):
            for el3 in el2.find_all('td'):
                tabl = (el3.text.strip())
                iter.append(tabl)
        for i in range(1, len(iter), 8):
            port.append(iter[i])
            port = [line.strip() for line in port]
        self.user_port_list.extend(port[:10])
        for i in range(0, len(iter), 8):
            ip.append(iter[i])
            ip = [line.strip() for line in ip]
        self.user_ip_list.extend(ip[:10])
        for i in range(2, len(iter), 8):
            country.append(iter[i])
            country = [line.strip() for line in country]
        self.user_country_list.extend(country[:10])

        for i in range(4, len(iter), 8):
            speed.append(iter[i])
            speed = [line.strip() for line in speed]
        self.user_speed_list.extend(speed[:10])

        for i in range(5, len(iter), 8):
            type.append(iter[i])
            type = [line.strip() for line in type]
        self.user_type_list.extend(type[:10])
        Database().bd(self.user_ip_list, self.user_port_list, self.user_type_list, self.user_country_list,
                      self.user_speed_list)
        self.clear()

    def screb5(self,url5):
        iter = []
        port = []
        ip = []
        country = []
        speed = []
        type = []

        page = requests.get(url5)
        result = bsoup(page.text, 'lxml')

        for el2 in result.find_all('td'):
            tabl = (el2.text.strip())
            iter.append(tabl)

        for i in range(1, len(iter), 5):
            port.append(iter[i])
            port = [line.strip() for line in port]
        self.user_port_list.extend(port[:10])

        for i in range(0, len(iter), 5):
            ip.append(iter[i])
            ip = [line.strip() for line in ip]
        self.user_ip_list.extend(ip[:10])

        for i in range(0, 10):
            type.append('HTTP')
        self.user_type_list.extend(type)

        for i in range(3, len(iter), 5):
            country.append(iter[i])
            country = [line.strip() for line in country]
        self.user_country_list.extend(country[:10])

        for i in range(4, len(iter), 5):
            speed.append(iter[i])
            speed = [line.strip() for line in speed]
        self.user_speed_list.extend(speed[:10])

        Database().bd(self.user_ip_list, self.user_port_list, self.user_type_list, self.user_country_list,
                      self.user_speed_list)
        self.clear()

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 800)
        Dialog.setStyleSheet("background-color: rgb(255, 229, 198);")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 400, 800))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

class Ui_FastProxy(object):
    def __init__(self):
        pass
    def setupUi(self, FastProxy):
        FastProxy.setObjectName("FastProxy")
        FastProxy.resize(360, 152)
        FastProxy.setAcceptDrops(False)
        FastProxy.setStyleSheet(
            "background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        FastProxy.setModal(False)
        self.toolButton = QtWidgets.QToolButton(FastProxy)
        self.toolButton.setGeometry(QtCore.QRect(30, 40, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(FastProxy)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 40, 141, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(FastProxy)
        QtCore.QMetaObject.connectSlotsByName(FastProxy)

        self.add_functions()

    def retranslateUi(self, FastProxy):
        _translate = QtCore.QCoreApplication.translate
        FastProxy.setWindowTitle(_translate("FastProxy", "FastProxy"))
        self.toolButton.setText(_translate("FastProxy", "Показать"))
        self.pushButton_2.setText(_translate("FastProxy", "Очистить"))

    def add_functions(self):
        # self.toolButton.clicked.connect(self.write_bd)
        self.toolButton.clicked.connect(self.Test)
        self.pushButton_2.clicked.connect(self.delete_bd)

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
            # pyqt.tableWidget(ip, port, type, country, speed)

            i+=1
        db.close()

    def delete_bd(self):
        d = Database()
        d.delete()
    def Test(self):
        FastProxy.show()
        tablebd.window.show()
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
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    sys.exit(app.exec())
