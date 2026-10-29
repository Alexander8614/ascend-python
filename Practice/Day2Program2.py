print("Please insert the first number")
number1 = int(input('>'))
print("Please insert the second number")
number2 = int(input('>'))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
if number2 == 0:
    print("Division not possible")
else:
    print(number1 / number2)