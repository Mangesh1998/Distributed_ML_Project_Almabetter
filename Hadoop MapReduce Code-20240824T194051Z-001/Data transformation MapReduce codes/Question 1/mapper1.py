#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Split the line into fields
    line = line.strip()
    fields = line.split(',')

    # Skip the header line or any malformed line
    if len(fields) != 17 or fields[0] == 'age':
        continue

    # Extract the relevant fields
    job_type = fields[1]
    account_balance = float(fields[5])

    # Output the key-value pair
    print(f'{job_type}\t{account_balance}')
