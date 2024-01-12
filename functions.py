from datetime import datetime, timedelta
import os
import openpyxl
import requests
import uuid
import shutil
import re
from time import sleep

def today() -> str:
    """
    Get the current date in the format 'MM/DD/YYYY'.

    Returns:
    - str: The current date.
    """
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
    if "hours" in target_date_str:
        return True

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
    """
    Get the start date based on the specified number of previous months.

    Parameters:
    - months (int): The number of previous months.

    Returns:
    - str: The start date in the format MM/DD/YYYY.
    """
    return get_previous_months(months)[-1]

def get_end_date() -> str:
    """
    Get the current date as the end date.

    Returns:
    - str: The end date in the format MM/DD/YYYY.
    """
    return today()

def close_all_browsers() -> None:
    """
    Close all open Google Chrome instances forcefully.
    """
    from config import Variables
    if Variables.CLOSE_ALL_OPEN_CHROME_INSTANCES:
        print("Closing every Google Chrome opened - if any")
        os.system("taskkill /f /im chrome.exe")

def stop() -> None:
    """
    Stop job execution with a sleep duration of 999999 seconds.
    """
    print("Stopped job execution")
    sleep(999999)

def download_image(url: str, folder: str) -> str:
    """
    Download an image from the given URL and save it to the specified folder.

    Parameters:
    - url (str): The URL of the image to download.
    - folder (str): The folder where the image will be saved.

    Returns:
    - str: The filename of the downloaded image or False if the download fails.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(folder, f"{str(uuid.uuid4())}.jpg")
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f'Image downloaded successfully: {file_name}')
        return file_name
    else:
        print(f'Failed to download image. Status code: {response.status_code}')
        return False

def create_excel_file(file_path: str, data: list[dict]) -> None:
    """
    Create an Excel file with the provided data.

    Parameters:
    - file_path (str): The path to save the Excel file.
    - data (list[dict]): The list of dictionaries containing news information.
    """
    print("Creating excel file")
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ["Title", "Date", "Description", "Picture Filename", "Title Occurrences", "Description Occurrences", "Contains Money"]
    sheet.append(headers)

    for item in data:
        row_data = [
            item["title"],
            item["date"],
            item["description"],
            item["image_file_name"],
            item["count_title"],
            item["count_description"],
            item["contains_money"]
        ]
        
        sheet.append(row_data)

    workbook.save(file_path)
    print("Excel file created successfully")

def delete_paths(paths: list[str]) -> None:
    """
    Delete files or folders specified by the given paths.

    Parameters:
    - paths (list[str]): List of file or folder paths to be deleted.
    """
    for path in paths:
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"File {path} removed successfully.")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Folder {path} removed successfully.")
            else:
                print(f"The given string {path} is not a valid file or folder.")
        except Exception as e:
            print(f"Error removing {path}: {e}")

def count_occurrences(s: str, phrase: str) -> int:
    """
    Count the occurrences of a phrase in a given string.

    Parameters:
    - s (str): The input string.
    - phrase (str): The phrase to search for.

    Returns:
    - int: The total occurrences of the phrase in the string.
    """
    escaped_phrase = re.escape(phrase)
    pattern = f'\\b{escaped_phrase}\\b'
    regex = re.compile(pattern, re.IGNORECASE)
    total_occurrences = len(regex.findall(s))
    return total_occurrences

def verify_money_format(s: str) -> bool:
    """
    Verify if a string contains a valid money format.

    Parameters:
    - s (str): The input string.

    Returns:
    - bool: True if the string contains a valid money format, False otherwise.
    """
    pattern = r'\$(\d+\.\d+|\d{1,3}(,\d{3})*(\.\d{2})?)|\d+\s(dollars|USD)'
    if re.search(pattern, s):
        return True
    else:
        return False
