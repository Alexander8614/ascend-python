valid = False
while not valid:
    print('Type the number you want to check')
    entry = input('>')
    if entry.isdigit():
        salary = int(entry)
        if salary == 0:
            print('Salary must be greater than 0')
        else:
            valid = True
    else:
        print('Please type a number')

print(f'{"Month":<8}{"Pension":>14}{"Health":>14}{"Total":>14}')
annual_total = 0
pension = salary * .12
health = salary * .08
total = pension + health
for month in range(1,13):
    annual_total = annual_total + total
    print(f'{month:<8}{pension:>14,.0f}{health:>14,.0f}{total:>14,.0f}')    
print()
print(f'{"Annual Total:":<13}{annual_total:>37,.0f}')