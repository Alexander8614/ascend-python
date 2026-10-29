def average(numbers_entered, total):
        if numbers_entered == 0:
            return 'No average, type at least one number'
        else:
            return total / numbers_entered
  
    
total = 0
count = 0
while True:
    entry = input('Number (or "fin"): ')
    if entry == 'fin':
        break
    total = total + int(entry)
    count = count + 1


print('Average:', average(count, total))