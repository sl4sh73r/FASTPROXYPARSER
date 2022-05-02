import re
import requests
import sqlite3
from bs4 import BeautifulSoup as bsoup


def bd(user_ip_list,user_port_list, user_type_list, user_country_list, user_speed_list):
    con = sqlite3.connect('mydatabase.db')
    cursorObj = con.cursor()
    cursorObj.execute("""CREATE TABLE IF NOT EXISTS users (
            IP TEXT,
            port TEXT,
            type TEXT,
            country TEXT,
            speed TEXT   
        )""")
    con.commit()
    for i in range(0, len(user_ip_list), 1):
        con.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user_ip_list[i], user_port_list[i],user_type_list[i], user_country_list[i], user_speed_list[i]))
        con.commit()


def screb(url):
    page = requests.get(url)
    result = bsoup(page.text, 'lxml')

    user_ip_list = []
    user_country_list = []
    user_speed_list = []
    user_port_list = []
    user_type_list=[]
    for el0 in result.find_all('td', class_='ip'):
        for el1 in el0.find_all('a'):
            user_IP = ((el1.text).split("\t")[0])
            user_ip_list.append(user_IP)

    for el00 in result.find_all('td', class_='country'):
        user_country = (el00.text.split()[0])
        user_country_list.append(user_country)

    for el00 in result.find_all('td'):
        for el0 in result.find_all('div', class_='progress-bar blue stripes'):
            for el1 in el0.find_all('i'):
                user_speed = (el1.text).split(" мс")[0]
                if user_speed != "":
                    user_speed_list.append(user_speed)

    for el0 in result.find_all('div', class_='kc-elm kc-css-517022 kc-raw-code'):
        el0 = re.sub(r'\s+', ' ', str(el0))
        _start = [i for i in range(len(el0)) if el0.startswith('attrPorts = attrPorts + "," + ', i)]
        _end = [i for i in range(len(el0)) if el0.startswith('</script>', i)]
        for i in range(len(_start)):
            user_port_list.append(int(el0[_start[i] + 30:_end[i] - 2]))

    for el0 in result.find_all('td'):
        for el1 in el0.find_all('a'):
            temp=((el1.text).split('\t')[0])
            temp1=(temp.split('\n')[0])
            user_type=((re.sub('[^A-Z]', '', temp1)))
            user_type_list.append(user_type)
    bd(user_ip_list,user_port_list, user_type_list, user_country_list, user_speed_list)

def main():
    screb(url='https://free.proxy-sale.com/')


if __name__ == "__main__":
    main()
