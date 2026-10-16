for letra in "Nicol":
    print (letra)

print("===========")
for numero in range (1,11):
    print (numero)

print("===========")
for numero in range (200,301,2):
    print (numero)

print("============")
for numero in range (10,0,-1):
    print (numero)
print("despegue")

print("=============")
for numero in range (1,11):
    resultado = 3*numero
    print("3 X",numero, "=", resultado)

print("===========")
notas = [10,8]
sumatoria = 0
for nota in notas: 
    sumatoria += nota # sumatoria = sumatoria + nota
cantNotas = len (notas)
promedio = sumatoria / cantNotas

print ("promedio es:" ,promedio)