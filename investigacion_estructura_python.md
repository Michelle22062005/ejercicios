#Estructuras de Datos en Python

##1. Listas
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