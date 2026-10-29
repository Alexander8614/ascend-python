from pathlib import Path
import csv
import sys 
import json

DEBUG = True

DATA_DIR = Path('data')
JOBS_PATH = DATA_DIR / 'jobs.csv'
BIG_JOBS_PATH = DATA_DIR / 'big_jobs.csv'
SUMMARY_PATH = DATA_DIR / 'summary.json'
LOG_PATH = DATA_DIR / 'run.log'

RATES = {'install': 95000, 'service': 65000,'repair':80000 }
COLUMNS = ['date', 'client', 'job_type', 'hours', 'labour', 'parts_cost', 'total']

DATA_DIR.mkdir(exist_ok=True)

print(JOBS_PATH.absolute())
print(BIG_JOBS_PATH.absolute())
print(SUMMARY_PATH.absolute())  
print(LOG_PATH.absolute())

def validate_client(client_data):
    client = client_data.strip()
    if client == '':
        raise ValueError('client is empty')
    return client

def validate_job_type(job_type_data):
    job_type = job_type_data.lower().strip()
    if job_type in RATES:
        return job_type
    raise ValueError(f'unknown job type: {job_type_data}')

def validate_hours(hours_data):
        hours = float(hours_data)
        if hours > 0 and hours <= 12:
            return hours
        raise ValueError('hours must be between 0 and 12')

def validate_parts_cost(parts_cost_data):
     parts_cost = int(parts_cost_data)
     if parts_cost < 0:
        raise ValueError('parts cost cannot be negative')
     return parts_cost
    

jobs = []
errors = []
try:
    with open(JOBS_PATH, newline='',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, start=1):
            job = {}
            date = row['date'].strip()
            try:
                job['date'] = date
                job['client'] = validate_client(row['client'])
                job['job_type'] = validate_job_type(row['job_type'])
                job['hours'] = validate_hours(row['hours'])
                job['parts_cost'] = validate_parts_cost(row['parts_cost'])
                jobs.append(job)
            
            except ValueError as err:
                errors.append(f'Line {n} ({date}): {err}')
except FileNotFoundError:
    print(f"""Could not find the file.
    Looked for {JOBS_PATH.absolute()}
    Put the jobs file in that folder,
    or check the filename is exactly jobs.csv, then run this again.""")
    sys.exit(1)


def calculate_labour(job_type, hours):
     labour_cost = int(RATES[job_type] * hours)
     return labour_cost
    

def calculate_total(labour_cost, parts_cost):
    total = labour_cost + parts_cost
    return total

total_revenue = 0
revenue_per_job_type = {}
hours_per_job_type = {}
biggest_job = None

for job in jobs:
    job['labour'] = calculate_labour(job['job_type'],job['hours'])
    job['total'] = calculate_total(job['labour'], job['parts_cost'])
    total_revenue = total_revenue + job['total']
    revenue_per_job_type[job['job_type']] = revenue_per_job_type.get(job['job_type'], 0) + job['total']
    hours_per_job_type[job['job_type']] = hours_per_job_type.get(job['job_type'], 0.0) + job['hours']
    if biggest_job is None or job['total'] > biggest_job['total']:
        biggest_job = job
        

print(f'Jobs read: {len(jobs)+len(errors)}')
print(f'Valid: {len(jobs)}')
print(f'Rejected: {len(errors)}')
print('')
print(f"{'CLIENT':<30}{'TYPE':<10}{'HOURS':>6}{'LABOUR':>12}{'PARTS':>12}{'TOTAL':>12}")
for job in jobs:
       print(f"{job['client']:<30}{job['job_type']:<10}{job['hours']:>6}{job['labour']:>12,}{job['parts_cost']:>12,}{job['total']:>12,}")
print(f"{'TOTAL':>70}{total_revenue:>12,}")
print('')
print('BY JOB TYPE')
for job_type in sorted(revenue_per_job_type):
  print(f"  {job_type:<12}{hours_per_job_type[job_type]:>4}{'h':>2}{revenue_per_job_type[job_type]:>14,}")
print('')
print(f"Biggest job: {biggest_job['client']} — {biggest_job['total']:,}")
print('')
print('REJECTED')
for error in errors:
    print(f'  {error}')

with open(BIG_JOBS_PATH, 'w', newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=COLUMNS)
    writer.writeheader()
    for job in jobs:
        if job['total'] > 200000:
            writer.writerow(job)

if DEBUG :
    with open(LOG_PATH, 'a',encoding='utf-8') as f:
        f.write('--- run start ---\n')
        for error in errors:
            f.write(f'REJECTED {error}\n')
        f.write(f'--- run end: {len(jobs)} valid, {len(errors)} rejected, {total_revenue:,} total ---\n')

summary = {'jobs_read': (len(jobs)+len(errors)), 'valid': len(jobs), 'rejected':len(errors), 'total_revenue': total_revenue}
summary['revenue_by_type'] = revenue_per_job_type
summary['hours_by_type'] = hours_per_job_type
summary['biggest_job'] = {'client': biggest_job['client'],'total':biggest_job['total']}
summary['rejected_lines'] = errors
print(summary)

json_summary = json.dumps(summary,indent=2)
print(json_summary)


with open(SUMMARY_PATH,'w',encoding='utf-8') as f:
    f.write(json_summary)   

    

try:
    with open(SUMMARY_PATH, 'r', encoding='utf-8') as f:
        summary_text = f.read()   
    new_summary = json.loads(summary_text)
    print(type(new_summary))
    print(new_summary['total_revenue'])
    print(new_summary['biggest_job']['client'])
    print(summary == new_summary)
except ValueError as err:
    print(f'The file is not valid JSON:{err}')    
except FileNotFoundError as err:
    print(print(f'Could not find the file. Looked for {SUMMARY_PATH.absolute()} \nPut the summary file in that folder,\nor check the filename is exactly summary.json, then run this again.'))

def print_dir_content(dir_to_print):
    
    print(f"{'Kind':<8}{'Name':<20}{'Stem':<10}{'Suffix':<8}{'Size':>10}")
    for entry in sorted(dir_to_print.glob('*')):
        kind = 'File' if entry.is_file() else 'Folder'
        print(f"{kind:<8}{entry.name:<20}{entry.stem:<10}{entry.suffix:<8}{entry.stat().st_size:>10,}")

print_dir_content(DATA_DIR)