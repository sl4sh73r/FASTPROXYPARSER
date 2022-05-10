import re
import requests
import sqlite3
from bs4 import BeautifulSoup as bsoup
from PyQt6 import QtCore, QtGui, QtWidgets
import pingspeed
# import tablebd
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