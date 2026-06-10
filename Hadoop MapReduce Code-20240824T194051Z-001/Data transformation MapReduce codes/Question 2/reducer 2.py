#!/usr/bin/env python
import sys

current_education = None
with_housing_loan_count = 0
without_housing_loan_count = 0

for line in sys.stdin:
    # Parse the input from the mapper
    line = line.strip()
    education, housing_loan = line.split('\t', 1)

    # Check if the education category has changed
    if current_education == education:
        # Increment count based on housing loan status
        if housing_loan == 'yes':
            with_housing_loan_count += 1
        elif housing_loan == 'no':
            without_housing_loan_count += 1
    else:
        if current_education:
            # Output counts for the previous education category
            print(f'{current_education}\t{with_housing_loan_count}\t{without_housing_loan_count}')
        current_education = education
        # Reset counts for the new education category
        with_housing_loan_count = 0
        without_housing_loan_count = 0

# Output counts for the last education category
if current_education == education:
    print(f'{current_education}\t{with_housing_loan_count}\t{without_housing_loan_count}')