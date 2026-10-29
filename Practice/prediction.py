def mystery(n):
    result = 0
    DEBUG = True
    while n > 0:
        result = result + (n % 10)
        if DEBUG == True:
            print(f'result is={result}')
        n = n // 10
        if DEBUG == True:
            print(f'n={n}')

    return result

print(mystery(12543))
