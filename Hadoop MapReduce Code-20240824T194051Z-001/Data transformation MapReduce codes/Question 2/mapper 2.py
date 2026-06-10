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
    education = fields[3]
    housing_loan = fields[7]
    

    # Output the key-value pair
    print(f'{education}\t{housing_loan}')