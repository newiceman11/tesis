import sqlite3
from datetime import datetime
import os.path

class Input():


        os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
        def __init__(self,nombre,tipoDNI,numDni,fecNac,tel,email,clave,cmb):
            self.nombre = nombre
            self.tipoDNI= tipoDNI
            self.numDni= numDni
            self.fecNac=fecNac
            self.tel=tel
            self.email=email
            self.clave=clave
            self.cmb=cmb
    #-----------------------------------------------------------------------    
        def setting(self):
            os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
            conn = sqlite3.connect('daily.db')
            print("Opened database successfully")
            try:
                conn.execute('''CREATE TABLE PASAJEROS(
                ID_PASAJERO INTEGER PRIMARY KEY AUTOINCREMENT, 
                APELNOM VARCHAR(50),
                TIPO_DOC VARCHAR(3),
                NUMERO_DOC INTEGER UNIQUE,
                FEC_NAC TIMESTAMP,
                ID_PAIS INTEGER,
                TEL INTEGER,
                EMAIL VARCHAR(50),
                CLAVE VARCHAR (25))
                ''')
            except:
                pass
            print("Table created successfully")
            conn.close()

        #---------------------------------------------------------------------------------------------
        def submit(self): # Insert values into earning table
            try:
                sqliteConnection = sqlite3.connect('daily.db')
                cursor = sqliteConnection.cursor()
                print("Successfully Connected to SQLite")
                count=cursor.execute("INSERT INTO PASAJEROS VALUES (NULL,'"+self.nombre+
                "','" +self.tipoDNI+
                "','" +self.numDni+
                "','" +self.fecNac+
                "','" +self.cmb+
                "','" +self.tel+
                "','" +self.email+
                "','" +self.clave+
                "')")

                sqliteConnection.commit()
                print("Record inserted successfully into DAILY_EARNING_CHART table", cursor.rowcount)
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert earning data into sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                print("The SQLite connection is closed")

        