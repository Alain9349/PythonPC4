import requests
import zipfile
import os

URL = "https://images.unsplash.com/photo-1723843095320-c5eedd1b1ab5?q=80&w=1376&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

image_name = "imagen_mascota.jpg"

response = requests.get(URL)

with open(image_name, "wb") as file:
    file.write(response.content)

zip_name = "mascota_zip.zip"
with zipfile.ZipFile(zip_name, 'w') as zip_file:
    zip_file.write(image_name)

print(f"Archivo ZIP '{zip_name}' creado con éxito.")

# Función para descomprimir el archivo ZIP
def unzip_file(zip_name, extract_to="."):
    with zipfile.ZipFile(zip_name, 'r') as zip_file:
        zip_file.extractall(extract_to)
    print(f"Archivos extraídos en '{extract_to}'.")

unzip_file(zip_name)












