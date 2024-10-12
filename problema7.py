import requests
import sqlite3
import pandas as pd
from pymongo import MongoClient

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=5&year=2023"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json() 
    else:
        print("Error al obtener datos del API")
        return None

def guardar_en_sqlite(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')

    for item in data:
        cursor.execute('''
            INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (item['fecha'], item['compra'], item['venta']))

    conn.commit()
    conn.close()
# Función para guardar los datos en MongoDB
def guardar_en_mongo(data):
    client = MongoClient("mongodb+srv://handradenato:<db_password>@clustermongodb.bzv3s.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDb")
    db = client["mi_base_de_datos"]  
    coleccion = db["sunat_info"]      

    coleccion.insert_many(data)

def mostrar_contenido_sqlite():
    conn = sqlite3.connect('base.db')
    df = pd.read_sql_query("SELECT * FROM sunat_info", conn)
    conn.close()
    print(df)

if __name__ == "__main__":
    
    datos = obtener_tipo_cambio()

    if datos:
        
        guardar_en_sqlite(datos)

        guardar_en_mongo(datos)

        mostrar_contenido_sqlite()

  



