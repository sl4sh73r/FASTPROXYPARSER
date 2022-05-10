import sqlite3
class Database:
    def __init__(self):
        self.con = sqlite3.connect('mydatabase.db')
        self.cursorObj = self.con.cursor()

        self.cursorObj.execute("""CREATE TABLE IF NOT EXISTS users (
                            IP TEXT,
                            port TEXT,
                            type TEXT,
                            country TEXT,
                            speed TEXT   
                        )""")
        self.con.commit()

    """
    # ТЕСТ ФУНКЦИЯ
    def print(self):
        rows = self.cursorObj.execute('''SELECT *
                            FROM users''').fetchall()
        if rows != []:
            i = 0
            for row in rows:
                if i == 5:
                    break

                ip = row[0]
                port = row[1]
                type = row[2]
                country = row[3]
                speed = row[4]
                print(ip, port, type, country, speed)

                i += 1
        else:
            print("Табличка пуста")
    """

    def bd(self, user_ip_list, user_port_list, user_type_list, user_country_list, user_speed_list):
        for i in range(0, len(user_ip_list), 1):
            self.con.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)",
                        (user_ip_list[i], user_port_list[i], user_type_list[i], user_country_list[i],
                         user_speed_list[i]))
            self.con.commit()

        self.con.close()

    def delete(self):
        rows = self.cursorObj.execute('''SELECT * FROM users''').fetchall()
        if rows != []:
            self.cursorObj.execute('DELETE FROM users')
            self.con.commit()
            print("Очищенно")
        else:
            print('Данных нет')

    def close(self):
        self.con.close()