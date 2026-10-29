import sys
def get_valid_number(prompt):
    valid = False
    while not valid:
        try:
            valid_number = float(prompt)
            valid = True
            return valid_number
            
        except:
            print('You must type a number.')
            return False
            
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
    print('Please type salary')
    entry = input('>')
    if get_valid_number(entry) == False:
        continue
    else:
        valid_number = get_valid_number(entry)
        valid_salary = is_valid_salary(valid_number)        
        if valid_salary == True:
            salary = valid_number

            while not valid:
                print('Please type the increment percent')
                entry = input('>')
                if  get_valid_number(entry) == False:
                    continue
                else:
                    percent = get_valid_number(entry)
                    new_salary = apply_increment(salary,percent)
                    print(f'The new salary is:{new_salary:.2f}')
                    valid = True
        else:
            print('Salary should be positive and above 1.300.000')
            



