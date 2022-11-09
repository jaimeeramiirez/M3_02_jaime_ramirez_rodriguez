# 1) Código a evaluar:

x=7
y=0
try:
  numero=7/0
except ZeroDivisionError:
    print("No se ha podido realizar la división")


#El error en este primer código es que no podemos dividir un número entre 0 ya que no está definido. Al ejecutarlo nos saltará el error "ZeroDivisionError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"

print("\n\n")
  
# 2) Código a evaluar:
lista = [4, 7, 30, 23, 5]

try:
  lista[10]
except IndexError:
  print("El índice de la lista se encuentra fuera del rango")
  