#Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
#la tabla de multiplicar de ese número, donde n es el número introducido.

numero_entero = int(input('Introducir un número entero entre 1 y 10: '))
fichero = 'tabla-' + str(numero_entero) + '.txt'
with open(fichero, 'w') as f:
    for i in range(1, 11):
        f.write(str(numero_entero) + ' x ' + str(i) + ' = ' + str(numero_entero * i) + '\n')


#Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar 
#de ese número, donde “n” es el número introducido, y la muestre por pantalla. 
#Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)

#Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar 
#de ese número, y muestre por pantalla la línea m del fichero. 
#Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello

n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as f:
        lineas = f.readlines()
    print(lineas[m - 1])
except FileNotFoundError:
    print('No existe el fichero con la tabla del ', n)