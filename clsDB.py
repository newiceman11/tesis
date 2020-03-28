import sqlite3
from datetime import datetime
import os.path

class Input:
        os.chdir("/home/juampi/Escritorio/Python/Sistema")
        def __init__(self, description, earning):
            self.description = description
            self.earning = earning
    #-----------------------------------------------------------------------    
        def setting(self):
            conn = sqlite3.connect('daily_earning.db')
            print("Opened database successfully")
            try:
                conn.execute('''CREATE TABLE DAILY_EARNING_CHART
                     (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     DESCRIPTION    TEXT (50)   NOT NULL,
                     EARNING    TEXT  NOT NULL,
                     TIME   TEXT NOT NULL);''')
            except:
                pass
            print("Table created successfully")
            conn.close()

        #---------------------------------------------------------------------------------------------
        def submit(self): # Insert values into earning table
            try:
                sqliteConnection = sqlite3.connect('daily_earning.db')
                cursor = sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                count = cursor.execute("INSERT INTO PASAJEROS VALUES (NULL,'"+miNombre.get()+
                "','" +miTipo.get()+
                "','" +miNum.get()+
                "','" +miFec.get()+
                "','" +miPais.get()+
                "','" +miTel.get()+
                "','" +miEmail.get()+
                "','" +miClave.get()+"')")

                sqliteConnection.commit()
                print("Record inserted successfully into DAILY_EARNING_CHART table", cursor.rowcount)
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert earning data into sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("The SQLite connection is closed")