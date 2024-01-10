from datetime import datetime, timedelta

def today():
    return datetime.now().strftime("%m/%d/%Y")

def is_date_between(start_date_str: str, target_date_str: str, end_date_str: str) -> bool:
    """
    Check if a target date falls between a given start date and end date (inclusive).

    Parameters:
    - start_date_str (str): The start date in the format 'MM/DD/YYYY'.
    - target_date_str (str): The target date in the format 'Month day, YYYY' (e.g., 'January 30, 2022').
                            If the year is missing, the current year is assumed.
    - end_date_str (str): The end date in the format 'MM/DD/YYYY'.

    Returns:
    - bool: True if the target date is between the start and end dates (inclusive), False otherwise.
    """
    try:
        # Attempt to parse the target date with the full format including the year
        target_date = datetime.strptime(target_date_str, '%B %d, %Y')
    except ValueError:
        # If parsing fails, assume the current year and try again
        current_year = datetime.now().year
        target_date_str_with_year = f"{target_date_str}, {current_year}"
        target_date = datetime.strptime(target_date_str_with_year, '%B %d, %Y')

    # Parse the start and end dates
    start_date = datetime.strptime(start_date_str, '%m/%d/%Y')
    end_date = datetime.strptime(end_date_str, '%m/%d/%Y')

    # Check if the target date is between the start and end dates (inclusive)
    return start_date <= target_date <= end_date

def get_previous_months(num_months: int) -> list[str]:
    """
    Returns a list of dates representing the previous months, in the format MM/01/YYYY,
    based on the provided number.

    Parameters:
    - num_months (int): The number of desired months.

    Returns:
    - List[str]: List of dates in the format MM/01/YYYY.
    """
    current_date = datetime.now()

    result = []

    result.append(current_date.strftime("%m/01/%Y"))

    # Subtract one month at a time and add to the list
    for i in range(1, num_months):
        current_date = current_date - timedelta(days=current_date.day)
        result.append(current_date.strftime("%m/01/%Y"))

    return result

def get_start_date(months: int) -> str:
    return get_previous_months(months)[-1]

def get_end_date() -> str:
    return today()