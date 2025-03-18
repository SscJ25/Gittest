from datetime import datetime

# a function that calculates the days between two dates
def days_between_dates(date1, date2):
    return date2 - date1
# Example usage
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 1, 10)
days = days_between_dates(date1, date2).days
print(f"Days between dates: {days}")