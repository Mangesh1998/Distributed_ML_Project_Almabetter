#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionaries to store the sum of balances and the count of clients per age
age_balance_sum = defaultdict(float)
age_count = defaultdict(int)

# Process each line of input from the mapper
for line in sys.stdin:
    line = line.strip()
    age, balance, count = line.split('\t')

    # Accumulate the sum of balances and the count of clients
    age_balance_sum[age] += float(balance)
    age_count[age] += int(count)

# Output the average balance per age
for age in sorted(age_balance_sum.keys(), key=int):
    total_balance = age_balance_sum[age]
    total_count = age_count[age]
    average_balance = total_balance / total_count
    print(f'{age}\t{average_balance:.2f}')
