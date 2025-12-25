def validate_dates(start_date, end_date):
    if start_date > end_date:
        raise ValueError("Start date cannot be after end date")
