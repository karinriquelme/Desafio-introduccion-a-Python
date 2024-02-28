
print("\n\neste programa calcula la velocidad de escape ")
radio= float(input ("ingrese el radio en Kilometros: "))
gravedad= float(input ("ingrese la constante g: "))

velocidadEscape=(2*gravedad*(radio*1000))**(1/2)
veconUnDecimal=round(velocidadEscape,1)

print(f"la velocidad de escape es: {(veconUnDecimal) } [m/s]\n\n")

