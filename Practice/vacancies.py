valid = False
import random

while not valid:
    print('How many vacancies?')
    entry = input('>')
    if entry.isdigit():
        vacancies = int(entry)
        if vacancies == 0:
            print('At least one vacancie')
        else:
            valid = True
    else:
        print('Pease type a number')

for month in range(1,13):
    
    for vac in range(1,vacancies + 1):
        month = random.randint(1, 12)
    if month == 1:
        month1= month1+1
    
