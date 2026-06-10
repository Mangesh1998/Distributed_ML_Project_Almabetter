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
    month = fields[10]
    subscription_status = fields[16]

    # Output the key-value pair
    print(f'{month}\t{subscription_status}')