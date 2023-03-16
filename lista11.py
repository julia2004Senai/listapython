numeros = [10, 20, 30, 40, 50]

maior_numero = numeros[0]

for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
        
print("O maior número da lista é:", maior_numero)