print('How many hours did you study this week?')
study_hours = int(input('>'))
print('How many days of the week did you study?')
days = int(input('>'))
if study_hours < 0:
    print("Hours cannot be negative")
if days == 0:
    print("Days cannot be 0")
if study_hours >= 0 and days != 0:
    average = study_hours / days
    print("Tu promedio de horas de estudio es " + str(average))