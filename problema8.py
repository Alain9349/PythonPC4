import pandas as pd
from pymongo import MongoClient
from datetime import datetime

ventas = pd.read_csv('ventas.csv')

client = MongoClient('mongodb+srv://handradenato:<db_password>@clustermongodb.bzv3s.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDb') 
db = client['mi_base_de_datos'] 
tipo_cambio_collection = db['sunat_info']

def obtener_tipo_cambio(fecha):
    tipo_cambio = tipo_cambio_collection.find_one({'fecha': fecha})
    return tipo_cambio['tipo_de_cambio'] if tipo_cambio else None

resultados = []


for index, row in ventas.iterrows():
    fecha_compra = row['fecha'] 
    id_producto = row['id_producto']  
    precio_dolares = row['precio_dolares'] 
    
 
    tipo_cambio = obtener_tipo_cambio(fecha_compra)
    
    if tipo_cambio is not None:
        precio_soles = precio_dolares * tipo_cambio
        total_producto = {
            'id_producto': id_producto,
            'precio_dolares': precio_dolares,
            'precio_soles': precio_soles,
            'fecha_compra': fecha_compra
        }
        resultados.append(total_producto)
    else:
        print(f"Tipo de cambio no encontrado para la fecha: {fecha_compra}")

resultados_df = pd.DataFrame(resultados)
print(resultados_df)