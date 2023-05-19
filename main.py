import json
from collections import defaultdict


def calculate_balance_sheet(input_file):
    with open(input_file) as f:
        data = json.load(f)

    balancesheet = defaultdict(int)

    start_date = data['startDate']

    for entry in data['revenue']:
        timestamp = entry.get('timestamp', start_date)
        amount = entry['amount']
        year_month = timestamp[:7]  # Extract year and month
        balancesheet[year_month] += amount

    for entry in data['expense']:
        timestamp = entry.get('timestamp', start_date)
        amount = entry['amount']
        year_month = timestamp[:7]  # Extract year and month
        balancesheet[year_month] -= amount

    sorted_sheet = sorted(balancesheet.items(), key=lambda x: x[0])  # Sort by timestamp

    for timestamp, balance in sorted_sheet:
        print(f"{timestamp}: {balance}")


# Usage example

calculate_balance_sheet('1-input.json')
