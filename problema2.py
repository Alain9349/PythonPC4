import pyfiglet
import random

texto = input("Por favor, ingresa el texto que deseas convertir: ")

nombre_fuente = input("Por favor, ingresa el nombre de una fuente (deja vacío para seleccionar aleatoriamente): ")

fuentes_disponibles = pyfiglet.FigletFont.getFonts()

if not nombre_fuente:
    nombre_fuente = random.choice(fuentes_disponibles)

figlet = pyfiglet.Figlet(font=nombre_fuente)


texto_convertido = figlet.renderText(texto)

print(texto_convertido)


