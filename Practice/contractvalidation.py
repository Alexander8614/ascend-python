import sys
print("Contract type (fixed / indefinite / apprentice):")
for attempt in range(3,0,-1):
    entry = input('>')
    if entry == "fixed" or entry == "indefinite" or entry == "apprentice":
        print(f'Accepted:{entry}')
        break
    if attempt > 1:
        print(f'Invalid. {attempt - 1} attempts remaining.')
    else:
        print('Too many failed attempts. Exiting.')
        sys.exit()

    