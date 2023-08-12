print("--------------------------------")
print("CALCULADORA DE RESISTENCIAS 3000")
print("--------------------------------")
print("COLORES DE RESISTENCIAS")
print("--------------------------------")
print("Opcion 1: Negro")
print("Opcion 2: Cafe")
print("Opcion 3: Rojo")
print("Opcion 4: Naranja")
print("Opcion 5: Amarillo")
print("Opcion 6: Verde")
print("Opcion 7: Azul")
print("Opcion 8: Violeta")
print("Opcion 9: Gris")
print("Opcion 10: Blanco")
print("--------------------------------")
print("TOLERANCIA DE RESISTENCIAS")
print("--------------------------------")
print("Opcion 11: Toletancia cafe")
print("Opcion 12: Tolerancia roja")
print("Opcion 13: Tolerancia dorado")
print("Opcion 14: Tolerancia plata")
print("--------------------------------")

print("Elija su primer color")
c1= int(input("Numero de opcion >> "))
while c1 < 1 or c1 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    c1 = int(input("Ingrese nuevo numero de opcion >> "))
print("Elija su segundo color")
c2= int(input("Numero de opcion >> "))
while c2 < 1 or c2 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    c2 = int(input("Ingrese nuevo numero de opcion >> "))
print("Elija su tercer color")
c3= int(input("Numero de opcion >> "))
while c3 < 1 or c3 > 10:
    print("Opcion erronea, opcion no valida para color de resistencia")
    c3 = int(input("Ingrese nuevo numero de opcion >> "))
print("Elija su tolerancia")
t= int(input("Numero de opcion >> "))
while t < 11 or t > 14:
    print("Opcion erronea, opcion no valida para una tolerancia")
    t = int(input("Ingrese nuevo numero de opcion >> "))

#tanda de if de c1
if (c1 == 1):
    c1 = 0
if (c1 == 2):
    c1 = 1
if (c1 == 3):
    c1 = 2
if (c1 == 4):
    c1 = 3
if (c1 == 5):
    c1 = 4
if (c1 == 6):
    c1 = 5
if (c1 == 7):
    c1 = 6
if (c1 == 8):
    c1 = 7
if (c1 == 9):
    c1 = 8
if (c1 == 10):
    c1 = 9
#tanda de if de c2
if (c2 == 1):
    c2 = 0
if (c2 == 2):
    c2 = 1
if (c2 == 3):
    c2 = 2
if (c2 == 4):
    c2 = 3
if (c2 == 5):
    c2 = 4
if (c2 == 6):
    c2 = 5
if (c2 == 7):
    c2 = 6
if (c2 == 8):
    c2 = 7
if (c2 == 9):
    c2 = 8
if (c2 == 10):
    c2 = 9
#tanda de if c3
if (c3 == 1):
    c3 = 1
if (c3 == 2):
    c3 = 10
if (c3 == 3):
    c3 = 100
if (c3 == 4):
    c3 = 1000
if (c3 == 5):
    c3 = 10000
if (c3 == 6):
    c3 = 100000
if (c3 == 7):
    c3 = 1000000
if (c3 == 8):
    c3 = 10000000
if (c3 == 9):
    c3 = 100000000
if (c3 == 10):
    c3 = 1000000000
#tanda de if de t
if (t == 11):
    t = 1
if (t == 12):
    t = 2
if (t == 13):
    t = 5
if (t == 14):
    t = 10


def resistencia(c1, c2):
    x=c1+c2
    return x
x=resistencia (str(c1), str(c2))
x=(int(x))*c3
print("---------------------------------")
print("Valor de la resistencia es: " + str(x))
print("Porcentaje de tolerancia de " + str(t))
print("---------------------------------")
print("░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█")
print("░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█")
print("░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█")
print("░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌")
print("░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█")
print("▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌")
print("█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█")
print("█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█")
print("▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌")
print("▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌")
print("█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█")
print("HAY UN POCO DE CODIGO EN TU IF")
print("----------------------------------")