def total_value(inventory):
    total_value = 0
    for n in range(len(inventory)):
        total_value = total_value + inventory[n]['price'] * inventory[n]['quantity']
    return total_value

def most_expensive(inventory):
    most_expensive = 0
    most_expensive_name = inventory[0]['name']
    for n in range(len(inventory)):
        if inventory[n]['price'] >= most_expensive:
            most_expensive = inventory[n]['price']
            most_expensive_name = inventory[n]['name']
    return most_expensive_name


inventory = [
    {'name': 'keyboard', 'price': 85000,  'quantity': 12},
    {'name': 'monitor',  'price': 650000, 'quantity': 3},
    {'name': 'mouse',    'price': 45000,  'quantity': 20}
]

print(f'Total value = {total_value(inventory):0,}')
print(f'Most Expensive name = {most_expensive(inventory)}')


