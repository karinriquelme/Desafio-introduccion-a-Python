print("\neste programa calcula las utilidades de un proyecto")
precioSuscripcion = float(input("ingrese precio de suscripcion:"))
usuarios = int(input("ingrese numero de Usuarios: "))
gastosTotales=float(input("ingrese gastos totales: "))
utilidadAnterior=float(input("ingrese las utilidades del año anterior y que sea distinta de cero: "))


utilidades = precioSuscripcion*usuarios-gastosTotales

razon=utilidadAnterior/ utilidades
razoConDosDecimales=round(razon,2)
print(f"las utilidades son {utilidades}")
print(f"la razon entre las utilidades actuales y del año pasado son :{razoConDosDecimales}")

