def validate_temp(raw):
    temp = float(raw)
    if temp < -30 or  temp > 55:
        raise ValueError('temperature out of range')
    return temp

raw = '-40.0'
        
try:
    print(validate_temp(raw))
except ValueError as err: 
    print(f'{raw!r:9} -> rejected: {err}')