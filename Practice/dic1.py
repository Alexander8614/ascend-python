def salary_is_valid(employee):
    if employee['salary'] >= 1300000:
        return True
    else:
        return False



employee = {'name': 'Alex','salary': 1500000, 'contract_type': 'fixed'}
print(salary_is_valid(employee))