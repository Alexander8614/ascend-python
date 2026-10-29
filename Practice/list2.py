valid = False
name_list = []
while not valid:
    print("type the name you want in the list or 'fin' to finishing registering")
    entry = input('>')
    print(entry)
    
    if entry.lower() != 'fin':
        name_list.append(entry)
        print(name_list)

    else:
        valid = True

print(name_list)
print(f'Total: {len(name_list)}')
name_list.reverse()
print(f'Al revés: {name_list}')
