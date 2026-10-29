import sys
from pathlib import Path
DATA_DIR = Path('data')
READINGS_PATH = DATA_DIR / 'readings.txt'
REPORT_PATH = DATA_DIR / 'report.txt'
LOG_PATH = DATA_DIR / 'run.log'

DATA_DIR.mkdir(exist_ok=True)

READINGS = [
    '2026-03-01,18.5',
    '2026-03-02,21.0',
    '2026-03-03,abc',
    '2026-03-04,19.5',
    '2026-03-05,-40.0',
    '2026-03-06,23.5',
]

def validate_temp(raw_tem):
    temp = float(raw_tem)
    if temp < -30 or  temp > 55:
        raise ValueError('temperature out of range')
    return temp

with open(READINGS_PATH, 'w', encoding='utf-8') as f:
    for reading in READINGS:
        f.write(f'{reading}\n') 

valid_readings =[]
errors = []
try:
    with open(READINGS_PATH, 'r', encoding='utf-8') as f: 
        for n,line in enumerate(f,start=1):
            try:
                date, raw_tem = line.strip().split(',') 
                temp = validate_temp(raw_tem)
                reading= {'date': date, 'temp': temp}
                valid_readings.append(reading)
            except ValueError as err:
                errors.append(f'Line {n} — {err}')
except FileNotFoundError:
    print(f'{READINGS_PATH} does not exist')
    sys.exit()



with open(LOG_PATH, 'a', encoding='utf-8') as f: 
    f.write(f'{valid_readings[0]["date"]} to {valid_readings[-1]["date"]}: valid {len(valid_readings)}, rejected {len(errors)}\n')
total = 0
for reading in valid_readings:
    total = total + reading['temp']
average = total / len(valid_readings)

print(average)

highest_temp = valid_readings[0]['temp']
lowest_temp = valid_readings[0]['temp']
highest_temp_date = valid_readings[0]['date']
lowest_temp_date = valid_readings[0]['date']
for reading in valid_readings:
    if reading['temp'] > highest_temp:
        highest_temp = reading['temp']
        highest_temp_date = reading['date']
    if reading['temp'] < lowest_temp:
        lowest_temp = reading['temp']
        lowest_temp_date = reading['date']
print(highest_temp,highest_temp_date, lowest_temp, lowest_temp_date)  

with open(REPORT_PATH, 'w', encoding='utf-8') as f: 
    f.write('WEATHER REPORT\n')
    f.write(f'{"Readings read:":<16}{len(READINGS)}\n')
    f.write(f'{"Valid:":<16}{len(valid_readings)}\n')
    f.write(f'{"Rejected:":<16}{len(errors)}\n')
    f.write(f'{"Average:":<16}{average:.2f} C\n')
    f.write(f'{"Highest:":<16}{highest_temp} C on {highest_temp_date}\n')
    f.write(f'{"Lowest:":<16}{lowest_temp} C on {lowest_temp_date}\n')
    f.write(f'\n')
    f.write(f'ERRORS\n')
    for error in errors:
        f.write(f'  {error}\n')


def list_data_files():
    for file in sorted(DATA_DIR.glob('*.txt')):
        print(file.name, '|', file.stem, '|', file.suffix, '|', file.stat().st_size, 'bytes')

    for file in sorted(DATA_DIR.glob('*')):
        kind = 'file  ' if file.is_file() else 'folder'
        print(kind, file.name)


list_data_files()




             