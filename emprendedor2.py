print("\neste programa calcula las utilidades de un proyecto")
precioSuscripcion = int(input("ingrese precio de suscripcion:"))
usuarios = int(input("ingrese numero de Usuarios: "))
usuariosPremium = int(input("ingrese numero de Usuarios premium: "))

gastosTotales=int(input("ingrese gastos totales: "))

utilidades = (precioSuscripcion * usuarios * 1.0) + (precioSuscripcion * 1.5 * usuariosPremium) - gastosTotales



print(f"las utilidades son {utilidades}")
