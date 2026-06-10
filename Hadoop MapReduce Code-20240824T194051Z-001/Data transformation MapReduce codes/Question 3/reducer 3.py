#!/usr/bin/env python
import sys

current_month = None
subscription_counts = {'yes': 0, 'no': 0}

for line in sys.stdin:
    # Parse the input from the mapper
    line = line.strip()
    month, subscription_status = line.split('\t', 1)

    # Check if the month has changed
    if current_month == month:
        # Increment count based on subscription status
        subscription_counts[subscription_status] += 1
    else:
        if current_month:
            # Output counts for the previous month
            print(f'{current_month}\t{subscription_counts["yes"]}\t{subscription_counts["no"]}')
        current_month = month
        # Reset counts for the new month
        subscription_counts = {'yes': 0, 'no': 0}

# Output counts for the last month
if current_month:
    print(f'{current_month}\t{subscription_counts["yes"]}\t{subscription_counts["no"]}')