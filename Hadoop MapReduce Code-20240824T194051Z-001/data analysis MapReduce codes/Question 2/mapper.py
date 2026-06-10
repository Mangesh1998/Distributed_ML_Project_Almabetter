#!/usr/bin/env python
import sys

for line in sys.stdin:
    # Strip whitespace and split by comma
    line = line.strip()
    fields = line.split(',')

    # Skip header or malformed lines
    if len(fields) != 17 or fields[0] == 'age':
        continue

    # Extract relevant fields
    age = int(fields[0])  # Client's age
    balance = float(fields[5])  # Client's balance

    # Emit key-value pair: "age" -> (balance, 1)
    print(f'{age}\t{balance}\t1')
