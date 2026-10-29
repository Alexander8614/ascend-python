def lookup(data, key, default=None):
    if key in data:
        return data[key]
    return default


print(lookup({'a':1,'b':2,'c':3},0,'g'))