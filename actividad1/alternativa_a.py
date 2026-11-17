#GEMENI
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

# Aseguramos que 'a' sea menor que 'b'
if a > b:
    a, b = b, a

# Aseguramos que 'a' sea menor que 'c' (aquí 'a' ya es garantizado el menor de todos)
if a > c:
    a, c = c, a

# Solo queda ordenar los dos mayores ('b' y 'c')
if b > c:
    b, c = c, b

print(a, b, c)
