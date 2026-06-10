#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Strip whitespace and split by comma
    line = line.strip()
    fields = line.split(',')

    # Skip the header or malformed lines
    if len(fields) != 17 or fields[0] == 'age':
        continue

    # Extract relevant fields
    poutcome = fields[15]  # Outcome of the previous campaign
    duration = int(fields[11])  # Duration of the contact in seconds

    # Emit key-value pair: "poutcome" -> (duration, 1)
    print(f'{poutcome}\t{duration}\t1')
