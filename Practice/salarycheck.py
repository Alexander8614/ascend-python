def is_valid_salary(salary):
    if salary > 1300000:
        return True
    else:
        return False

def apply_increment(salary,percent):
   new_salary = salary * (1 + (percent/100))
   return new_salary

valid = False
while not valid:
    try:
        print('Please type salary')
        entry = float(input('>'))
        valid = is_valid_salary(entry)
        if valid == True:
            salary = entry
        else:
            print('Salary should be positive and above 1.300.000')
    except:
        print('You must type a number.')

valid = False

while not valid:
    try:
        print('please type the increment percent')
        entry = float(input('>'))
        percent = entry
        new_salary = apply_increment(salary,percent)
        print(f'The new salary is: {new_salary:.2f}')
        valid = True
    except:
        print('the increment percent must be a number')

        
