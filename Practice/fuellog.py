DEBUG = True    # Just one line controls the whole Logging of the program
def validate_km(km_entry):
    km = float(km_entry)
    if km <= 0:
        raise ValueError('km must be positive')
    else:
        return km

def validate_lt(lt_entry):
    lt = float(lt_entry)
    if lt <= 0:
        raise ValueError('lt must be positive')
    else:
        return lt

def validate_question(question_entry):
    if question_entry.lower() == 'fin':
        return True
    elif question_entry.lower() == 'yes':
        return False
    else:
        raise ValueError("Type 'yes' or 'fin'")
        
    


total_consumption = 0
total_lt = 0
total_km = 0
counter = 0
question = False
while not question:
    try:
        print('Type the kilometres')
        km_entry = input('>')
        km = validate_km(km_entry)
        if DEBUG:
            print(f'[LOG] km={km}')
        valid1 = False    
        while not valid1:    
            print('Type the liters')
            lt_entry = input('>')
            lt = validate_lt(lt_entry)
            if km >= lt:
                valid1 = True
            else:
                print('km must be greater or iqual to lt')

        if DEBUG:
            print(f'[LOG] lt={lt}')
        consumption = km / lt
        if DEBUG:
            print(f'[LOG] consumption={consumption}')

        
        total_km = total_km + km
        if DEBUG:
            print(f'[LOG] total km={total_km}')
        total_lt = total_lt + lt
        if DEBUG:
            print(f'[LOG] total lt={total_lt}')
        total_consumption = total_consumption + consumption
        if DEBUG:
            print(f'[LOG] total consumption={total_consumption}')
        counter = counter + 1
        if counter == 1:
            best_fillup  = consumption
            worst_fillup = consumption
        
        if best_fillup <= consumption:
            best_fillup = consumption
        if worst_fillup >= consumption:
            worst_fillup = consumption
        average_consumption = total_consumption / counter
    except ValueError as err:
        print(f'{str(err)}')
    valid = False    
    while not valid:
        try:
            print ("Do you want to keep registering 'yes/fin'")
            question_entry = input('>')
            question = validate_question(question_entry)
            valid = True
        except ValueError as err:
            print(f'{str(err)}')
    if DEBUG:
        print(f'[LOG] question={question}')

        
         
            

    


print(f'Total km={total_km}')
print(f'Total lt={total_lt}')
try:
    print(f'Average consumption ={average_consumption}')
except NameError as err:
    print('Average consumption=0')
try: 
    print(f'best fillup={best_fillup}')
except NameError as err:
    print(f'best fillup=0 ')
try: 
    print(f'worse fillup={worst_fillup}')
except NameError as err:
    print(f'Worst fillup=0')


