

def collatz(number):

    if number % 2 == 0:
        result = number // 2
    else:    
        result = 3 * number + 1
    print(result)
    return result

print('Type an integer')
entry = int(input('>'))

current_number = collatz(entry)

while current_number != 1:    
    current_number = collatz(current_number)
   
