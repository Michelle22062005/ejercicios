#1.  Panadería de Don Pancho — Descuentos por cantidades
#La panadería de Don Pancho vende pan a $300 cada uno.
#Reglas:
#Si compra más de 20 panes → 10% descuento
#Si compra más de 50 panes → 20% descuento
#Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
#Calcular y mostrar el total.
panes=float(input("Cunatos panes va a acompar: "))
pan= 300 
total=pan*panes

if panes > 20:
    descuento =total* 0.10
    total_final = total-descuento
    print("El total a paga", total_final)
elif panes > 50:
    descuento =total* 0.20
    total_final = total-descuento
    print("El total a paga", total_final)
else:

    print("cantidad invalida")

#2. Cine “La Estrella” — Tarifas por edad
#Pedir la edad del cliente:

#Edad	Precio
#< 5 años	Entrada gratis
#5 a 11	$5.000
#12 a 59	$8.000
#≥ 60	$4.000 (descuento adulto mayor)
#Mostrar el precio.
#Si la edad es negativa, mostrar error.
edad=int(input("Ingrese tu edad"))

if  edad <0:
    print("Es un error, la edad no puede ser negativa")
elif edad < 5:
    print("La entrada es gratis")
elif edad >5 and edad < 11:
    print("El precio es $5.000")
elif edad >12 and edad < 59:
    print("El precio es $8.000")
elif edad >=60:
    print("El precio es $4.000 (descuento adulto mayor)")

#3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
#Pedir cuántos días entrenó esta semana.
#≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
#2 o 3 → "Bien, pero puedes dar más"
#0 o 1 → "No aflojes, tú puedes mejorar"
#Mostrar mensaje y si aplica, los puntos ganados.
dias=int(input("Cuantos dias entreno esta semana: "))
puntos=0
if dias >= 4:
    puntos= puntos+dias-4
    print(f'"¡Excelente disciplina!" + ganaste {puntos}  punto de energia')
elif dias > 2 or dias < 3:
    print("Bien, pero puedes dar más")
elif dias <0 or dias >1:
    print("No aflojes, tú puedes mejorar")

#4. Heladería “Frosty” — Sabor y topping
#Sabores y precios:
#chocolate → $4.000
#vainilla → $3.500
#Opcional: topping cuesta $1.000.
#Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
#Si el sabor es válido, preguntar si quiere topping y calcular total.
print('Heladeria "Frody" - Sabor y topping')

sabor=input("Ingresa un sabor de helado: ").lower()
valor1= 1000
if sabor == "chocolate":
    valor = 4000
    print("El helado de chocolate cuesta", valor)
    opcional=input("¿Quiere el helado con topping?").lower()
    if opcional == "si":
        total= valor + valor1
        print("El costo seria: ",total )
elif sabor == "vainilla":
    valor = 3500
    print("El helado de vainilla cuesta", valor)
    opcional=input("¿Quiere el helado con topping?").lower()
    if opcional == "si":
        total= valor + valor1
        print("El costo seria: ",total )
else:
    print("Sabor no existe")

#5. Librería “El Saber” — Descuento estudiante + cupón
#Libro cuesta $25.000.

#Si es estudiante → 15% descuento
#Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
#Validar:

#Si no es estudiante, el cupón no aplica.
#Si ingresa cupón incorrecto, ignorarlo.
#Mostrar total.
print('Librería “El Saber” — Descuento estudiante + cupón')
estudy=input("Eres estuduantes:  ").lower()
libro=25000
cupon ="LIBRO10"
#primer descuento
descuento_estu=libro*0.15
total= libro- descuento_estu
 #segundo descuento
descuento_cupo=total*0.10
total_final=total-descuento_cupo

if estudy =="si"and cupon =="LIBRO10":
    cupon=input("Tiene el cupon: ").lower()
    print("El valor del libro con el descuento por cupo es ",total_final)
elif estudy =="no":
    print("El valor del libro es: ", total)
else:
    print("Incorrecto")

#6. Parqueadero “RapidCar” — Tarifa escalonada
#Tarifa:

#0 a 5 horas: $2.000 x hora
#5 horas: $2.000 x hora + multa fija de $5.000

#Validar horas:

#No permitir números negativos.
#Mostrar valor total.
print("Parqueadero “RapidCar” — Tarifa escalonada")

hora=int(input("Cuantas horas vas a parquear: "))
por_hora= 2000
total= hora* por_hora
multa= 5000
total_multa= total+ multa
if hora >0 and hora <5 :
    print("El valor es", total)
elif hora >5:
    print(f"El valor es : {total_multa} por una multa fija de 5000 ")
elif hora <0 :
    print("No escribir numero negativos")


#7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA
#Menú: $12.000

#Opciones bebida:

#sí → $3.000
#no → $0
#Luego aplicar IVA del 8% al total final.
#Mostrar valor con IVA incluido.
print("Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA")

menu_base= 12000
bebida= 3000
beber= (input("Quiere tomar una bebeida: "))
if beber=="si":
    total= menu_base +bebida
    iva=total*0.08
    total_final= total + iva
    print("El total a pagar es: ",total_final)
elif beber == "no":
    iva= menu_base*0.08
    total_final1=menu_base + iva
    print("El total a pagra es:  ",total_final1)

#8. Empresa “TecnoPlus” — Evaluación compuesta
#El usuario ingresa dos notas (0.0 - 5.0):

#Prueba técnica (70%)
#Prueba lógica (30%)
#Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

#Condiciones:

#nota_final ≥ 3 → “Aprobado”
#2 ≤ nota_final < 3 → “Revisión”
#< 2 → “Reprobado”
#Validar que las notas estén en rango.
print("Empresa “TecnoPlus” — Evaluación compuesta")

nota1=float(input("Ingrresa la nota: "))
nota2=float(input("Ingrresa la otra nota: "))

prueba_tecnica= 0.70
prueba_logica = 0.30

nota_final= (nota1 * prueba_tecnica)+ (nota2 * prueba_logica)

if nota_final >= 3 and nota_final <5:
    print("Aprovado")
elif nota_final >=2 and nota_final <3 :
    print("Revision")
elif nota_final <2  and nota_final >0:
    print("Reprobado")

#9. Supermercado “AhorroMax” — Descuentos y envío
#Cada producto cuesta $2.000.

#Reglas:

#30 unidades → 15% descuento

#10 unidades → 5% descuento

#Si el total después del descuento es < $50.000 → agregar $5.000 de envío
#Calcular total final.

print("Supermercado “AhorroMax” — Descuentos y envío")
producto=int(input("Cuantos productos va a comprar: "))
valor=2000
total= producto * valor
envio=5000

if producto ==30 :
    descuento= total * 0.15
    total_final= total - descuento
    print("El valor a pagar es: ",total_final)
    if total_final <50000:
        final = total_final + envio
        print("El valor a pagar es", final )
elif producto ==10:
    descuento= total * 0.05
    total_final= total - descuento
    print("El valor a pagar es: ",total_final)
    if total_final <50000:
        final = total_final + envio
        print(f"El valor es final  a pagar es {final}" )
elif producto:
    print("El valor a pagar es: ", total)

#10. Club “Noche Estelar” — Acceso + validación documento
#Pedir edad y documento.

#Reglas:

#Edad ≥ 18 → puede entrar solo si tiene documento.
#Si la edad < 18 → "Entrada denegada"
#Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

print("Club “Noche Estelar” — Acceso + validación documento")
edad=int(input("Dime tu edad"))
documento=(input("Trae el documento"))

if edad >=18  and documento == "si" :
    print("Si puede ingresar con el documento")
elif edad <18 :
    print("Entrada denegada, eres menor de edad")
elif edad >=18 and documento == "no":
    print("No puedes ingresar, debe presentar el documeto")
