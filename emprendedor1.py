print("\neste programa calcula las utilidades de un proyecto")
precioSuscripcion = int(input("ingrese precio de suscripcion:"))
usuarios = int(input("ingrese numero de Usuarios: "))
gastosTotales=int(input("ingrese gastos totales: "))

utilidades = precioSuscripcion * usuarios - gastosTotales

print(f"las utilidades del proyecto son {utilidades}")

