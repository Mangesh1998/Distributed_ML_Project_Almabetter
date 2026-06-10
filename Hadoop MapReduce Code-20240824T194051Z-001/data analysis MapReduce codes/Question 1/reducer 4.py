#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionaries to store the sum of durations and the count of contacts per poutcome
poutcome_duration_sum = defaultdict(int)
poutcome_count = defaultdict(int)

# Process each line of input from the mapper
for line in sys.stdin:
    line = line.strip()
    poutcome, duration, count = line.split('\t')
    
    # Accumulate the sum of durations and the count of contacts
    poutcome_duration_sum[poutcome] += int(duration)
    poutcome_count[poutcome] += int(count)

# Output the average duration per poutcome
for poutcome in poutcome_duration_sum:
    total_duration = poutcome_duration_sum[poutcome]
    total_count = poutcome_count[poutcome]
    average_duration = total_duration / total_count
    print(f'{poutcome}\t{average_duration:.2f}')
