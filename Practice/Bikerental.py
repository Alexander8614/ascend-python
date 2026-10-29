RATES = {
    'city':     {'hourly': 8000,  'daily_cap': 40000},
    'mountain': {'hourly': 12000, 'daily_cap': 60000},
    'electric': {'hourly': 20000, 'daily_cap': 100000}
}
MEMBERS = ['ana', 'luis', 'sofia']
HELMET_FEE = 5000
DAMAGE_FEE = 50000

DEBUG = True

def validate_bike_type(bike_type_entry):
    if bike_type_entry.strip().lower() in RATES:
       bike_type = bike_type_entry.strip().lower()
       return bike_type
    else:
        raise ValueError(f'unknown bike type: {bike_type_entry.strip()}')

def validate_hours(hours_entry):
    hours = int(hours_entry)
    if hours <= 0 or hours > 48:
        raise ValueError('hours must be between 1 and 48')
    return hours

def validate_yes_no(answer, field_name):
    if answer.strip().lower() == 'yes':
        return True
    elif answer.strip().lower() == 'no':
        return False
    else: 
        raise ValueError(f'{field_name} must be yes or no')

def is_member(name):
    return name.strip().lower() in MEMBERS

def calculate_rental_cost(bike_type, hours):
    rate = RATES[bike_type]
    full_blocks = hours // 24
    leftover_hours = hours % 24
    leftover_cost = min(leftover_hours * rate['hourly'], rate['daily_cap'])
    return full_blocks * rate['daily_cap']+ leftover_cost


def calculate_total(rental):
    if rental['helmet']:
        helmet_fee = HELMET_FEE
    else:
        helmet_fee = 0
    if rental['damage']:
        damage_fee = DAMAGE_FEE
    else:
        damage_fee = 0
    if rental['member']:
        discount = rental['rental_cost'] * 10 // 100
    else: 
        discount = 0
    total = rental['rental_cost'] - discount + helmet_fee + damage_fee
    assert total > 0, 'Total cost must be greater than 0'
    return total

def get_warnings(rental):
    rental_warnings = []
    if rental['hours'] > 24:
        rental_warnings.append(rental['name'] + ' — ' + 'long rental: confirm return date')
    if rental['bike_type'] == 'electric' and rental['helmet'] == False:
         rental_warnings.append(rental['name'] + ' — ' + 'electric bike without helmet')
    return rental_warnings
        

rental_warnings = []
rental_errors = []
valid = False
valid_rentals = []
while not valid:
    rental = {}
    print('Type the name of the customer')
    name_entry = input('>')
    if name_entry.strip() != '':
        name = name_entry.strip()
        rental['name']= name
    else:
        print("Name can't be empty")
        continue
    print("What's the type of the bike")
    bike_type_entry = input('>')
    try: 
        bike_type = validate_bike_type(bike_type_entry)
        rental['bike_type'] = bike_type
        print('How many hours rented?')
        hours_entry = input('>')
        hours = validate_hours(hours_entry)
        rental['hours'] = hours
        print('Rented helmet? yes/no')
        helmet = validate_yes_no(input(''),'helmet')
        rental['helmet'] = helmet
        print('Is there damage? yes/no')
        damage = validate_yes_no(input(''),'damage')
        rental['damage'] = damage
        member = is_member(name)
        rental['member'] = member
        rental_cost = calculate_rental_cost(bike_type,hours)
        rental['rental_cost'] = rental_cost
        total = calculate_total(rental)
        rental['total'] = total
        valid_rentals.append(rental)
        if DEBUG:
            print(f'Valid rental: {rental['name']} Total: {rental['total']}')
        rental_warnings = rental_warnings + get_warnings(rental)
    except ValueError as err:
        if DEBUG:
            print(f'Error: {name} — {str(err)}')
        rental_errors.append(rental['name'] + ' — ' + str(err))
    
        

    valid_2 = False
    while not valid_2:
        print('Register another rental? (yes/no)')
        aditional_registration = input('')
        if aditional_registration.lower().strip() == 'no':
            valid = True
            valid_2 = True
        elif aditional_registration.lower().strip() == 'yes':
            valid_2 = True

revenue_bike_type= {}
revenue_bike_type['city'] = 0
revenue_bike_type['mountain'] = 0
revenue_bike_type['electric'] = 0
for n in range(len(valid_rentals)):
    if valid_rentals[n]['bike_type'] == 'city':
        revenue_bike_type['city'] = revenue_bike_type['city'] + valid_rentals[n]['total']
    if valid_rentals[n]['bike_type'] == 'mountain':
        revenue_bike_type['mountain'] = revenue_bike_type['mountain']+ valid_rentals[n]['total']
    if valid_rentals[n]['bike_type'] == 'electric':
        revenue_bike_type['electric'] = revenue_bike_type['electric']+ valid_rentals[n]['total']
most_expensive = 0
for n in range(len(valid_rentals)):
    if valid_rentals[n]['total'] > most_expensive:
        most_expensive_name = valid_rentals[n]['name']
        most_expensive = valid_rentals[n]['total']
longest_rental = 0
for n in range(len(valid_rentals)):
    if valid_rentals[n]['hours'] > longest_rental:
        longest_rental_name = valid_rentals[n]['name']
        longest_rental = valid_rentals[n]['hours']


    


print('--- DAILY REPORT ---')
print(f'Rentals processed: {len(valid_rentals) + len(rental_errors)}')
print(f'Valid: {len(valid_rentals)}')
print(f'Rejected: {len(rental_errors)}')
print(f'Warnings: {len(rental_warnings)}')
print('')
print('REVENUE BY BIKE TYPE')
print(f'  city: {revenue_bike_type['city']:,.0f}')
print(f'  mountain: {revenue_bike_type['mountain']:,.0f}')
print(f'  electric: {revenue_bike_type['electric']:,.0f}')
print(f'Total revenue: {revenue_bike_type['city']+revenue_bike_type['electric']+revenue_bike_type['mountain']:,.0f}')
print('')
if not valid_rentals:
    print(f'Most expensive rental: none')
    print('Longest rental: none')
else:
    print(f'Most expensive rental: {most_expensive_name} — {most_expensive:,.0f}')
    print(f'Longest rental: {longest_rental_name} — {longest_rental} hours')

    
    
    
print('')
print('ERRORS')
if len(rental_errors) != 0:     
    for n in rental_errors:
        print(f'  {n}')
else:
    print('')
print('')
print('WARNINGS')
if len(rental_warnings) != 0:
  for n in rental_warnings:
      print(f'  {n}')