numbers = [1, 2, 3, 4, 5, 6]
odd_numbers= []
for n in numbers:
    print(n)
    if n % 2 != 0:
        odd_numbers.append(n)
print(odd_numbers)