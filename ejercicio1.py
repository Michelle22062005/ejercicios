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