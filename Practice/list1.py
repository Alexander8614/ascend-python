numeros = [45,156,21,76,98]
max_value = numeros[0]
min_value = numeros[0]
for i in range(len(numeros)):
    if numeros[i] >= max_value:
        max_value = numeros[i]
    if numeros[i]<= min_value:
        min_value = numeros[i]

print(F'Min={min_value}')
print(F'Max={max_value}')



