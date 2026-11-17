# Claude: código aportado por el estudiante.
# Adaptación: se añaden las entradas que faltaban en el fragmento recibido.
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
