print('How many hours did you work this week?')
week_hours = int(input('>'))
if week_hours < 20 :
    print('Part-time')
    print(f'Hours below the standard: {20 - week_hours}')
elif    week_hours <= 46:
    print('Full-time')
    print('Standard week')
else:
    print('Overtime')
    print(f'{week_hours - 46} hours over the limit')
