print("Tarea 1")

age= int(input("Ingrese su edad : "))

if age >= 18:
    print("Por favor ingrese su voto")
else :
    print("Usted es menor de edad, no puede votar")

print("////////////////////////")

print("Tarea 2")

temp= float(input("Ingrese la temperatura del agua : "))

if temp <=0 :
    print("Su agua esta congelada, es un hielo")
elif temp <= 100:
    print("Su agua esta en estado liquido")
else : print("Su agua ya no es agua, es puro vapor")

print("////////////////////////")

print("Tarea 3")

num= int(input("Ingrese su numero : "))

if num >= 1:
    print(f"El {num} es positivo")
elif num == 0:
    print("Su numero es 0")
else :
    print(f"El {num} es negativo")