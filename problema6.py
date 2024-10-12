
def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith('.py'):
            print("El archivo debe tener una extensión .py")
            return
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        contador_lineas_codigo = 0
        
        for linea in lineas:
            linea = linea.strip() 
            if linea and not linea.startswith('#'):  
                contador_lineas_codigo += 1
        
        print(f"Número de líneas de código (sin comentarios ni líneas en blanco): {contador_lineas_codigo}")
    
    except FileNotFoundError:
        print("El archivo no existe. Por favor, verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

ruta = input("Ingresa la ruta del archivo .py: ")
contar_lineas_codigo(ruta)





