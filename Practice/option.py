def check(a, b):
    if b == 0:
        raise Exception('b cannot be zero')
    if a % b == 0:
        return True
    return False


print(check(2,45))