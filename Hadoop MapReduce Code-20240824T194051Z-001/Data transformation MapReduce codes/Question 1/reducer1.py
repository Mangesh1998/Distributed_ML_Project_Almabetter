#!/usr/bin/env python
import sys

current_job_type = None
current_balance_total = 0
current_count = 0

for line in sys.stdin:
    # Split the input from mapper
    job_type, account_balance = line.strip().split('\t')
    account_balance = float(account_balance)

    # Check if we are still on the same job type
    if current_job_type == job_type:
        current_balance_total += account_balance
        current_count += 1
    else:
        if current_job_type:
            # Calculate and print the average for the previous job type
            average_balance = current_balance_total / current_count
            print(f'{current_job_type}\t{average_balance}')
        
        # Reset for the new job type
        current_job_type = job_type
        current_balance_total = account_balance
        current_count = 1

# Output the last job type's average if there were any records processed
if current_job_type == job_type:
    average_balance = current_balance_total / current_count
    print(f'{current_job_type}\t{average_balance}')
