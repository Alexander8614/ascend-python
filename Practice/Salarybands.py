print('Please insert your monthly salary in COP')
salary = float(input('>'))
if salary <= 0:
    print('Invalid Salary')
else:
    if salary < 1300000:
        print('Below minimum wage — check the data')    
    if salary <= 2000000:
        print("Band 1")
        print("Increment: 9%")
        print(f"New salary: {salary * 1.09:,.0f}")
    elif salary <= 4000000:
        print("Band 2")
        print("Increment: 7%")
        print(f"New salary: {salary * 1.07:,.0f}")
    elif salary <= 8000000:
        print("Band 3")
        print("Increment: 5%")
        print(f"New salary: {salary * 1.05:,.0f}")
    else:
        print("Band 4")
        print("Increment: 3%")
        print(f"New salary: {salary * 1.03:,.0f}") 

