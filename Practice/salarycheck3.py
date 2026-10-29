def get_valid_number(prompt):
        valid = False
        while not valid:
            print(prompt)
            entry = input('>')
            try:
                valid_number = float(entry)
                valid = True
                return valid_number  
            except:
                print('You must type a number.')


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
    valid_number = get_valid_number('Please type salary')
    if is_valid_salary(valid_number):
        salary = valid_number
    else:
        print('Salary should be positive and above 1.300.000')
        continue
    percent = get_valid_number('Please type the increment percent')
    valid = True

new_salary = apply_increment(salary,percent)
print(f'The new salary is: {new_salary}')


