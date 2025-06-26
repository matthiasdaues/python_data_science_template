from datetime import datetime, timedelta

# Function to generate a list of date strings from start_date to end_date (inclusive)
def create_date_series(start_date, end_date):
    """
    Returns a list of date strings (YYYY-MM-DD) from start_date to end_date (inclusive).
    """
    dates = []
    current_date = start_date
    end = end_date
    while current_date <= end:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates

