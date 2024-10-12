
with open('temperaturas.txt', 'r') as archivo:
    lineas = archivo.readlines()

temperaturas = []
for linea in lineas:
    fecha, temperatura = linea.strip().split(',')
    temperaturas.append(float(temperatura))

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
temperatura_promedio = round(sum(temperaturas) / len(temperaturas),2)


with open('resumen_temperaturas.txt', 'w') as resumen:
    resumen.write(f'Temperatura máxima: {temperatura_maxima}\n')
    resumen.write(f'Temperatura mínima: {temperatura_minima}\n')
    resumen.write(f'Temperatura promedio: {temperatura_promedio}\n')


