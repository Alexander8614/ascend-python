ascend-python

Learning Python from the ground up, following Automate the Boring Stuff with Python (3rd edition).

This is Stage 0 of a longer plan: build enough Python to work with real data and APIs. One hour a day, one project per day.

What's here
service/ — Week 4 project

service_report.py reads a CSV of air-conditioning service jobs, validates it, calculates revenue, and writes a report plus two output files.

It covers chapters 8, 10 and 18 — strings, file handling, CSV and JSON.

What it does:

Reads data/jobs.csv and validates every row (client, job type, hours, parts cost)
Rejects bad rows with a line number and reason, without stopping
Calculates labour and totals from a rate table
Prints a formatted report
Writes data/big_jobs.csv — jobs over 200,000
Writes data/summary.json and reads it back to verify
Handles a missing input file and a corrupted JSON file
Logs every run to data/run.log
Practice/ — exercises

Day-to-day exercises from weeks 1 to 4. Working through loops, functions, lists, dictionaries, strings and files.

Running it
cd service
python service_report.py

Needs Python 3.12 or later. No external packages — standard library only.

Known limitations

Deliberate, not oversights:

No date validation — dates are treated as strings
Paths resolve against the working directory, so it must be run from service/
No duplicate detection
The log has no timestamps