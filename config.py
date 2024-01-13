import os
    
class Variables:
    # Challenge variables
    SEARCH_PHRASE = "Neymar"

    MONTHS = 3

    # Each search may return different sections.
    # For this reason, it is not valid to map an object with all available sections.
    # In this case, here is an example of recurring sections:

    # Arts, Books, Business, New York, Opinion, Style, Technology, U.S., World

    # If you want to add a specific section,
    # just insert it into the array below in string format.

    # Example:
    # SECTIONS = ["Arts", "Books"]

    # If the array becomes empty, the automation will maintain
    # the default sections configuration.
    SECTIONS = []

    # Complementary
    URL = "https://www.nytimes.com/"
    CLOSE_ALL_OPEN_CHROME_INSTANCES = True
    IMG_FOLDER = os.path.join(os.getcwd(), "img")
    EXCEL_FILE = os.path.join(os.getcwd(), "result.xlsx")
    # IMG_FOLDER = "C:\\git\\nytimes_challenge\\img"
    # EXCEL_FILE = "C:\\git\\nytimes_challenge\\result.xlsx"