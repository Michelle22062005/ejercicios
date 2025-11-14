#Estructuras de Datos en Python

#1. Listas
-**Que son:**

*Las listas son colecciones ordenadas y mutables de elementos.*
*Pueden almacenar distintos tipos de datos: números, cadenas, booleanos, etc.*
*frutas = ["manzana", "pera", "uva"]*

-**Porque son mutables**
*Porque se pueden modificar después de creadas:*
-Agregar elementos
-Eliminar
-Cambiar valores

-**Situaciones donde resultan útiles.**
-Cuando necesitas guardar datos que cambian, como una lista de compras.
-Para recorrer y procesar información en bucles.

-**Un ejemplo de creación, lectura, modificación y eliminación.**
---
# Crear lista
compras = ["pan", "leche", "huevos"]

# Leer elemento
print(compras[0])  # pan

# Modificar elemento
compras[1] = "café"

# Agregar elemento
compras.append("azúcar")

# Eliminar elemento
compras.remove("pan")

print(compras)
---

##2. Tuplas
-**Qué son.**
*Las tuplas son colecciones ordenadas e inmutables.*
*Una vez creadas, no se pueden cambiar.*
*coordenadas = (10, 20)*

-**Por qué son inmutables.**
*Porque no permiten modificar sus valores.*
*Esto garantiza que los datos permanezcan constantes durante la ejecución.*

-**Situaciones donde resultan útiles.**
*Cuando necesitas datos que no cambian, como coordenadas geográficas, fechas o configuraciones fijas.*

-**Un ejemplo de acceso y recorrido.**
---
# Crear tupla
*punto = (3, 5, 7)*

# Acceder a un elemento
*print(punto[1])  # 5*

# Recorrer la tupla
*for valor in punto:*
    *print(valor)*
---

##3. Diccionarios
-**Qué son y cómo almacenan la información.**
*Los diccionarios almacenan información en pares clave : valor.*
*Cada clave debe ser única, y se accede a los datos usando esa clave.*
*persona = {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"}*

-**Diferencias clave frente a listas y tuplas.**
|Estructura	|Ordenada |	Mutable	  |Acceso por           |Permite duplicados
|-------------------|-----------------|------------------|------------------------------|---------------------------------
|Lista	         |Sí	          | Sí	            |Índice numérico   | Sí                             
|Tupla	        |Sí	             |No	          |Índice numérico	 |Sí
|Diccionario|SI	              |Sí               |Clave	                   |No

-**Un ejemplo de agregar, consultar, modificar y eliminar elementos.**
---
# Crear diccionario
*persona = {"nombre": "Carlos", "edad": 30}*

# Agregar elemento
*persona["profesion"] = "Ingeniero"*

# Consultar elemento
*print(persona["nombre"])*

# Modificar valor
*persona["edad"] = 31*

# Eliminar elemento
*del persona["profesion"]*

*print(persona)*
---
##4. Match-case
-**Qué es y desde qué versión existe.**
*match-case es una estructura de control condicional indroducida en Python 3.10. Permite comparar un valor con multiplespatrones de forma mas clara que if-elif**

-**Para qué se usa.**
*Se usa para evaluar diferentes casos segun el valor de una variable, como si fuera un "swich" en otros lenguajes*

-**Diferencias frente a if y elif.**
|Aspecto   |if / elif	                                    |match-case
|----------------|--------------------------------------------------|----------------------------------------
Sintaxis     |Usa condiciones lógicas          |Usa patrones específicos
Claridad    |Más general pero repetitivo	|Más limpio y legible
Potencia    |Lógica compleja	                   |Coincidencia estructurada

-**Situaciones donde usarlo puede ser más claro.**
-Menús por consola
-Clasificación de valores
-Procesamiento de comandos o respuestas

-**Un ejemplo sencillo representando decisiones distintas según el valor ingresado.**
*opcion = input("Elige una fruta (1: Manzana, 2: Pera, 3: Uva): ")*

*match opcion:*
    *case "1":*
        *print("Elegiste una Manzana ")*
    *case "2":*
        *print("Elegiste una Pera ")*
    *case "3":*
        *print("Elegiste una Uva ")*
    *case _:*

        *print("Opción no válida ")*



#P1. Listas — Gestión de nombres
#Crear una lista con al menos cinco nombres. El usuario ingresa una opción y se ejecuta solo una acción:

#Agregar un nombre nuevo que no se encuentre ya en la lista.
#Mostrar todos los nombres.
#Cambiar un nombre existente por otro.
#Eliminar un nombre por su posición.
#Debe validarse que la posición sea correcta y que no existan duplicados.

lista=["Ana", "Luis", "Carlos", "Marta", "Sofía"]

opcion= int(input("Seleccione una opción:\n1. Agregar un nombre nuevo\n2. Mostrar todos los nombres\n3. Cambiar un nombre\n4. Eliminar un nombre por posición\n"))
if opcion==1:
    nuevo_nombre= input("Ingrese el nombre que desea agregar: ")
    if nuevo_nombre in lista:
        print("El nombre ya existe en la lista.")
    else:
        lista.append(nuevo_nombre)
        print(f"Nombre '{nuevo_nombre}' agregado exitosamente.")
elif opcion==2:
    print("Nombres en la lista:")
    for nombre in lista:
        print(nombre)
elif opcion==3:
        nombre_viejo= input("Ingrese el nombre que desea cambiar: ")
        if nombre_viejo in lista:
            nombre_nuevo= input("Ingrese el nuevo nombre: ")
            if nombre_nuevo in lista:
                print("El nuevo nombre ya existe en la lista.")
            else:
                indice= lista.index(nombre_viejo)
                lista[indice]= nombre_nuevo
                print(f"Nombre '{nombre_viejo}' cambiado por '{nombre_nuevo}'.")
elif opcion==4:
    posicion= int(input("Ingrese la posición del nombre que desea eliminar: "))
    if posicion < 1 or posicion > len(lista):
        print("Posición inválida.")
    else:
        nombre_eliminado= lista.pop(posicion - 1)
        print(f"Nombre '{nombre_eliminado}' eliminado de la lista.")




#P2. Diccionarios — Inventario básico
#Crear un diccionario con al menos cuatro productos y sus precios. El usuario elige una acción:

#Agregar un nuevo producto con su precio.
#Consultar el precio de un producto existente.
#Modificar el precio de un producto existente.
#Eliminar un producto del inventario.
#Al terminar la acción seleccionada, mostrar cuántos productos hay actualmente y el promedio de precios.

productos = {
    "arroz": 2000, 
    "carne": 15000, 
    "pollo": 8000, 
    "leche": 3500}

opcion= int(input("Seleccione una opción:\n1. Agregar un producto nuevo\n2. Consultar el precio de un producto existente\n3. Modificar el precio de un producto existente\n4. Eliminar un producto del inventario\n"))

if opcion == 1:
    producto_nuevo= input("Ingrese el nombre del producto que desea agregar: ")
    producto_precio= int(input("Ingrese el precio del producto: "))
    productos[producto_nuevo]= producto_precio
    print(f"Producto '{producto_nuevo}' agregado exitosamente con precio {producto_precio}.")
    for i in productos:
        print(f"{i}: {productos[i]}")
elif opcion == 2:
    producto_consulta= input("Ingrese el nombre del producto que desea consultar: ")
    if producto_consulta in productos:
        print(f"El precio de '{producto_consulta}' es {productos[producto_consulta]}.")
    else:
        print("El producto no existe en el inventario.")
elif opcion == 3:
    producto_modificar= input("Ingrese el nombre del producto que desea modificar: ")
    if producto_modificar in productos:
        nuevo_precio= int(input("Ingrese el nuevo precio del producto: "))
        productos[producto_modificar]= nuevo_precio
        print(f"El precio de '{producto_modificar}' ha sido modificado a {nuevo_precio}.")
    else:
        print("El producto no existe en el inventario.")
elif opcion == 4:
    producto_eliminar= input("Ingrese el nombre del producto que desea eliminar: ")
    if producto_eliminar in productos:
        del productos[producto_eliminar]
        print(f"Producto '{producto_eliminar}' eliminado del inventario.")
    else:
        print("El producto no existe en el inventario.")






#P3. Tuplas — Catálogo estático
#Crear una tupla con seis valores numéricos distintos. Debido a que no se puede modificar directamente, se debe mostrar el resultado de cada operación sin alterar la tupla original:

#Cómo quedaría si se agregara un nuevo valor al final.
#Cómo quedaría si un valor se reemplazara por otro.
#Cómo quedaría si se eliminara un valor por su posición.
#Mostrar todos los valores con sus posiciones.
#Además, se debe determinar manualmente:

#El valor mayor.
#El valor menor.
#La suma total.
#La posición del mayor.

catalogo_estatico=(1,2,3,4,5)

catalogo_valor_al_final=(1,2,3,4,5,6)
catalogo_remplazado=(1,2,3,4,9,5,6)
catalogo_valor_eleiminado=(1,2,3,4,9,5)
catalogo_ordenado=(1,2,3,4,5,9)

catalogo_mayor=9
catalogo_menor=1    
catalogo_suma_total=24
catalogo_posicion_mayor=5


        
        

