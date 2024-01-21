from robocorp.tasks import task
from challenge import Challenge
from openpyxl.utils.exceptions import IllegalCharacterError
from requests.exceptions import RequestException

@task
def main():
    """
    Main function to execute the web scraping process.

    This function initializes the Challenge class, runs the scraping process, and handles potential exceptions.

    Raises:
    - KeyboardInterrupt: If the user interrupts the process manually.
    - RequestException: If there is an issue with the HTTP request during the scraping process.
    - PermissionError: If the program does not have the necessary permissions for a specific operation.
    - FileNotFoundError: If a file or directory specified in the code is not found.
    - ValueError: If there is an issue with the data or its format during processing.
    - IllegalCharacterError: If illegal characters are encountered while working with data.
    - OSError or IOError: If there is an Input/Output error, such as issues writing or reading files.
    - Exception: If an unexpected error occurs during the scraping process.
    """
    try:
        print("Starting the scraping process.")
        challenge = Challenge()
        challenge.run()
        print("Scraping process completed successfully.")

    except KeyboardInterrupt as interruption_err:
        print(f"Process interrupted by the user: {interruption_err}.")
        raise interruption_err
    
    except RequestException as req_err:
        print(f'Failed to download image. Request error: {req_err}')
        raise req_err
    
    except PermissionError as perm_err:
        print(f"Permission error: {perm_err}")
        raise perm_err
    
    except FileNotFoundError as not_found_err:
        print(f"File not found error: {not_found_err}")
        raise not_found_err
    
    except ValueError as val_err:
        print(f"Value error: {val_err}")
        raise val_err
    
    except IllegalCharacterError as char_err:
        print(f"Illegal character error: {char_err}")
        raise char_err
    
    except (OSError, IOError) as io_err:
        print(f'Failed to download image. IO error: {io_err}')
        raise io_err
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise e
