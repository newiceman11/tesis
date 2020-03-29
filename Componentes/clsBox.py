import os.path
import sqlite3


class Box():

    def __init__(self):
        pass

    def combo_values_input(self):
            try:
                os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
                conn = sqlite3.connect("daily.db")
                cur = conn.cursor()
                query = cur.execute('SELECT ID_PAIS FROM PASAJEROS')
                data = []
                for row in cur.fetchall():
                        data.append(row[0])
                return data
                cur.close()
                conn.close()
            except:
                pass

    def combo_DNI(self):
            try:
                os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
                conn = sqlite3.connect("daily.db")
                cur = conn.cursor()
                query = cur.execute('SELECT TIPO_DOC FROM PASAJEROS')
                data = []
                for row in cur.fetchall():
                        data.append(row[0])
                return data

                cur.close()
                conn.close()
            except:
                pass
