import sqlite3
from datetime import datetime
import os.path

class Input():


        os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
        def __init__(self,nombre,cmbDni,numDni,fecNac,tel,email,clave,cmbPais):
            self.nombre = nombre
            self.cmbDni= cmbDni
            self.numDni= numDni
            self.fecNac=fecNac
            self.cmbPais=cmbPais
            self.tel=tel
            self.email=email
            self.clave=clave
            
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
            try:
                conn.execute('''CREATE TABLE PAISES(
                ID_PASAJERO INTEGER PRIMARY KEY AUTOINCREMENT, 
                NOMBRE CHAR(50))''')
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
                "','" +self.cmbDni+
                "','" +self.numDni+
                "','" +self.fecNac+
                "','" +self.cmbPais+
                "','" +self.tel+
                "','" +self.email+
                "','" +self.clave+"')")

                sqliteConnection.commit()
                print("Se ha insertado correctamente", cursor.rowcount)
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert earning data into sqlite table", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                print("The SQLite connection is closed")
            sqliteConnection.close
        