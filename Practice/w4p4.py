employees = [{'name': 'Ana', 'salary': 1000000},{'name': 'Carlos', 'salary': 2500000},{'name': 'Maria', 'salary': 850000}]              
for employee in employees:
    print(f'{employee['name']:<15}{employee['salary']:>12,}')