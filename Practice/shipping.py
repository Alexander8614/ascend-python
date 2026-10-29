def shipping_discount(order_total, items):
    if order_total < 0:
        raise ValueError('Order Total cannot be negative')
    if order_total > 200000:
        return 0
    if items < 3:
        return 5000
    return 15000

try:
    print(shipping_discount(150000, 5))
    print(shipping_discount(250000, 1))
    print(shipping_discount(-800, 5))

except Exception as err:
    print('An exception happened: ' + str(err))