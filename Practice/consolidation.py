# Print the multiples of 3 between 1 and 50   Print the multiples of 3 between 1 and 50
# for i in range (3,51,3):
#     print(i)

# Sum the even numbers from 1 to 100
# total = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         total= total + i

# print('# Sum the even numbers from 1 to 100')
# print(total)

# Print the numbers 10 down to 1

# print('the numbers 10 down to 1') 
# for i in range(10,0,-1):
#     print(i)

# Ask for numbers until the user types 'fin'. Print the total and the average.

print ('Total and average')
total = 0
counter = 0
valid = False

while not valid:
    print("Type a number or 'fin' to finish")
    entry = input('>')
    if entry == 'fin':
        valid = True
    else:
        number = int(entry)
        total = total + number
        counter = counter + 1
        average = total / counter

try:  
    print (f'The total is: {total} and the average is {average}')
except:
    print (f'The total is: 0 and the average is 0')

# Roll a die 100 times and count how many sixes come up

import random
counter = 0
for i in range (0,99):
    number = random.randint(1,6)
    if number == 6:
        counter = counter + 1
    else:
        continue

print(counter)
        