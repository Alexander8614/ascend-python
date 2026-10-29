DEBUG = True    # Just one line controls the whole Logging of the program
def validate_salary(salary_entry):
    salary = float(salary_entry)
    if salary <= 0:
        raise ValueError('Salary must be positive')
    elif salary < 1300000:
        return(salary,'salary below minimum wage')
    else:
         return(salary,None)

def validate_contract_type(contratc_type_entry):
     if contratc_type_entry.lower() in ('fixed','indefinite', 'apprentice'):
        contract_type = contratc_type_entry
        return contract_type
     else:
          raise ValueError(f'unknown contract type: {contratc_type_entry}')

def validate_hours(hours_entry):
    hours = float(hours_entry)
    if hours >= 1 and hours <=60:
        return hours
    else:
        raise ValueError ('Hours must be between 1 and 60')

def validate_months(start_month_entry, end_month_entry):
    start_month = int(start_month_entry)
    end_month = int(end_month_entry)
    if start_month >=1 and start_month <= 12 and end_month >=1 and end_month <= 12 and start_month <= end_month:
        return (start_month, end_month)
    else:
        raise ValueError ('Months should be between 1 and 12, and start month must be less than or equal to end month')

def calculate_transport_allowance(salary):
    if salary < 1300000:
        transport_allowance = 140000
        return transport_allowance
    else:
        transport_allowance = 0

    return transport_allowance

def calculate_prorated_days(start_month, end_month):
    months_worked = end_month - start_month + 1
    prorated_days = months_worked * 30
    return (prorated_days, months_worked)

def calculate_annual_cost(salary, transport_allowance, months_worked):
    annual_cost =  months_worked * (salary + transport_allowance )
    assert annual_cost >= 0, "Annual cost must be greater than or equal to 0"
    return annual_cost

employees_processed = 0
valid_employees = 0
rejected = 0
warnings = 0
valid = False
errors_text = ''
warnings_text = ''
Total_annual_cost = 0
while not valid:
    receive_warning = False
    print('Type the name of the Employee')
    name_entry = input('>')
    if name_entry.strip() != '':
        name = name_entry.strip()
    else:
        print("Name can't be empty")
        continue
    print('Type the employee salary')
    try:
        salary,warning = validate_salary(input('>'))
        if warning != None:
            warnings_text = warnings_text + '  ' + name + ' — ' + str(warning) + '\n'
            receive_warning = True
            warnings = warnings + 1
        print('Type the contract Type: fixed, indefinite or apprentice')
        contract_type = validate_contract_type(input('>'))
        print('Type the hours of the contract: between 1 and 60')
        hours = validate_hours(input('>'))
        print("Type the contract's start month")
        start_month_entry = input('>')
        print("Type the contract's end month")
        end_month_entry = input('>')
        start_month,end_month = validate_months(start_month_entry, end_month_entry)
        transport_allowance = calculate_transport_allowance(salary)
        prorated_days, months_worked = calculate_prorated_days(start_month, end_month)
        annual_cost = calculate_annual_cost(salary, transport_allowance, months_worked)
        Total_annual_cost = Total_annual_cost + annual_cost
        valid_employees = valid_employees + 1
        if DEBUG:
            print(f'[LOG] {name} Valid Employee -> salary={salary}, annual_cost={annual_cost}, warning={warning}')
    except ValueError as err:
        errors_text = errors_text + '  ' + name + ' — ' + str(err) + '\n'
        rejected = rejected + 1
        if DEBUG:
            print(f'[LOG] {name} rejected -> {err}')
        if receive_warning == True:
            warnings = warnings - 1

    
    employees_processed = rejected + valid_employees


    valid_2 = False
    while not valid_2:
        print('Do you need to add an Employee? Type Yes or Not')
        aditional_employee = input('')
        if aditional_employee.lower() == 'not':
            valid = True
            valid_2 = True
        elif aditional_employee.lower() == 'yes':
            valid_2 = True

    
        


print('--- REPORT ---')
print(f'Employees processed: {employees_processed}')
print(f'Valid: {valid_employees}')
print(f'Rejected: {rejected}')
print(f'Warnings: {warnings}')
print('')
print('ERRORS') 
print(errors_text) 
print('')
print('WARNINGS')     
print(warnings_text)
print(f'Total annual cost: {Total_annual_cost:,.0f}')


