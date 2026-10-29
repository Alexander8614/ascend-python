DEBUG = True    # Just one line controls the whole Logging of the program

def calculate_shipping_cost(weight_entry, destination_entry, fragile_entry):
    weight = float(weight_entry)
    if DEBUG:
        print(f'[LOG] Weight: {weight}')
    if destination_entry.lower() in ('local','national', 'international'):
        destination = destination_entry.lower()
        if DEBUG:
            print(f'[LOG] Destination: {destination}')
    else:
        raise ValueError(f'unknown destination: {destination_entry}')
    if fragile_entry.lower() in ('true','false'):
        fragile = fragile_entry.lower()
        if DEBUG:
            print(f'[LOG] Fragile: {fragile}')
    else:
        raise ValueError (f'Fragile must be either True or False')

    if weight <= 0:
        raise ValueError('Weight should be greater than 0')
    elif weight <= 1:
        if DEBUG:
            print(f'[LOG] Weight <=1')

        if destination == 'local':
            if fragile == 'true':
                shipping_cost = 8000 * 1.2
                return shipping_cost
            else:
                 shipping_cost = 8000
                 return shipping_cost
        if destination == 'national':
            if fragile == 'true':
                shipping_cost = 15000 * 1.2
                return shipping_cost
            else:
                shipping_cost = 15000
                return shipping_cost
        if destination == 'international':
            if fragile == 'true':
                shipping_cost = 60000 * 1.2
                return shipping_cost
            else:
                shipping_cost = 60000
                return shipping_cost

    elif weight <= 5:
        if destination == 'local':
            if fragile == 'true':
                shipping_cost = 15000 * 1.2
                return shipping_cost
            else:
                 shipping_cost = 15000
                 return shipping_cost
        if destination == 'national':
            if fragile == 'true':
                shipping_cost = 28000 * 1.2
                return shipping_cost
            else:
                shipping_cost = 28000
                return shipping_cost
        if destination == 'international':
            if fragile == 'true':
                shipping_cost = 120000 * 1.2
                return shipping_cost
            else:
                shipping_cost = 120000
                return shipping_cost

    elif weight <= 30:
        if destination == 'local':
            if fragile == 'true':
                shipping_cost = (15000 + (3000 * (30 - weight)))  * 1.2
                return shipping_cost
            else:
                 shipping_cost = (15000 + (3000 * (30 - weight)))
                 return shipping_cost
        if destination == 'national':
            if fragile == 'true':
                shipping_cost = (28000 + (5000 * (30 - weight)))  * 1.2
                return shipping_cost
            else:
                shipping_cost = (28000 + (5000 * (30 - weight)))
                return shipping_cost
        if destination == 'international':
                raise ValueError ('We do not accept international shipments over 5kg')
    else:
        raise ValueError('We do not accept shipments over 30kg')
    assert shipping_cost > 0, "Shipping cost must be greater tha 0"
            
try:
    shipping_cost = calculate_shipping_cost(6, 'Local', 'true')
    print(shipping_cost)
except ValueError as err: 
    print(str(err))