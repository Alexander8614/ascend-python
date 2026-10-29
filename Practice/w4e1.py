
#this is excersise 2
frase = 'El perro y yo nos fuimos, y yo me quede con el perro para siempre'
frase_list = frase.split()
new_frase_list = []
for item in frase_list:
    new_frase_list.append(item.lower().strip(',.!?'))

words_quantity = {}
for n in new_frase_list:
    if words_quantity.get(n, 0) == 0:
        words_quantity[n] = 1
    else:
        words_quantity[n] = words_quantity[n] + 1


print(words_quantity)