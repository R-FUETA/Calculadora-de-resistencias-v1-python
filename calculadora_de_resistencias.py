print("--------------------------------------")
print("      [COLORES DE RESISTENCIAS]       ")
print("--------------------------------------")
print("Opcion 0: Negro","   ","Opcion 1: Cafe")
print("Opcion 2: Rojo","    ","Opcion 3: Naranja")
print("Opcion 4: Amarillo","","Opcion 5: Verde")
print("Opcion 6: Azul","    ","Opcion 7: Violeta")
print("Opcion 8: Gris","    ","Opcion 9: Blanco")
print("--------------------------------------")
print("Elija su primer color")
color1= int(input("Numero de opcion >> "))
while color1 < 0 or color1 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    color1 = int(input("Ingrese nuevo numero de opcion >> "))
print("Elija su segundo color")
color2= int(input("Numero de opcion >> "))
while color2 < 0 or color2 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    color2 = int(input("Ingrese nuevo numero de opcion >> "))
print("Elija su tercer color")
color3= int(input("Numero de opcion >> "))
while color3 < 0 or color3 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    color3 = int(input("Ingrese nuevo numero de opcion >> "))
print("--------------------------------")
print("  [TOLERANCIA DE RESISTENCIAS]  ")
print("--------------------------------")
print("Opcion 10: Toletancia cafe")
print("Opcion 11: Tolerancia roja")
print("Opcion 12: Tolerancia dorado")
print("Opcion 13: Tolerancia plata")
print("--------------------------------")
print("Elija su tolerancia")
t= int(input("Numero de opcion >> "))
while t <= 9 or t > 14:
    print("Opcion erronea, opcion no valida para una tolerancia")
    t = int(input("Ingrese nuevo numero de opcion >> "))

if (t==10):
    t=1
elif (t==11):
    t=2
elif (t==12):
    t=5
elif (t==13):
    t=10

resistencia=((color1*10)+color2)*(10^color3)
print("Valor de la resistencia es:",resistencia,'Ohms')
print("Valor de la tolerancia es:",t,'%')
