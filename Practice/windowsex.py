def delivery_window_days(order_hour, priority):
    if order_hour <= 9 and priority == 'express':
        days = 1
    elif order_hour > 9 and priority == 'express':
        days = 2
    elif order_hour >= 9 and priority == 'standard':
        days = 5
    elif order_hour < 9 and priority == 'standard':
            days = 4
    return days

print(delivery_window_days(8, 'standard'))
print(delivery_window_days(11, 'express'))
print(delivery_window_days(8, 'standard'))