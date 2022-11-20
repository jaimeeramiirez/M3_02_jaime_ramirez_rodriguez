print("\n\n")

# 1) Código a evaluar:

def division(x,y):
  try:
    solucion= x/y
  except ZeroDivisionError:
      print("*No se ha podido realizar la división*")
  else:
    print(solucion)

  return

division(7,0)
division(7,1)

#El error en este primer código es que no podemos dividir un número entre 0 ya que no está definido. Al ejecutarlo nos saltará el error "ZeroDivisionError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




# 2) Código a evaluar:

lista = [4, 7, 30, 23, 5]
def posicion_lista(num):
  try:
    lista[num]
  except IndexError:
    print("*El índice de la lista se encuentra fuera del rango*")
  else:
    print("Se encuentra en el rango de la lista")
  return

posicion_lista(7)
posicion_lista(2)


#El error en este segundo código es que no podemos encontrar la posición 11 de ls lista  ya que no está definida. Al ejecutarlo nos saltará el error "IndexError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




# 3) Código a evaluar:

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
def diccionario(pais):
  try:
    paises[pais]
  except KeyError:
    print("*Clave no encontrada dentro del diccionario*")
  else:
    print("Sí se encuentra en el diccionario; el idioma del país introducido es el: {}".format(paises[pais]))

  return
diccionario("alemania")
diccionario("españa")

#El error en este tercer código es que no podemos encontrar la clave alemania dentro del diccionario, por consiguiente no podemos encontrar su valor; ya que ninguno de los dos está definido. Al ejecutarlo nos saltará el error "KeyError"; para solucinarlo utilizaremos "try" y "except". Dentro de la función "try" introduciremos aquello que queremos probar; si el resultado no se puede ejecutar directamente pasará al "except" donde, si el tipo de error, es el que nosotros hemos indicado se imprimirá por pantalla aquello que hay dentro del "except"
print("\n\n")




#  EJERCICIO 4

  # resultado= "2" + 10
  # El error en este bloque de código es que estamos tratando de sumar una cadena de texto con un número entero. Cuando ponemos entre comillas un número, el programa lo detecta como si fuera un "string" y no podemos sumarlo. Para arreglarlo haremos lo mismo que en los tres códigos anteriores.

def suma(x,y):
  try:
    resultado=(x+y)
  except TypeError:
    print("*No se pudo realizar la operación debido a que los tipos de datos son incorrectos*")
  else:
    print(resultado)
  return

suma("2",10)
suma(2, 10)