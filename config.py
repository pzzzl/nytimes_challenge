import os
from robocorp import storage
    
class Variables:
    # Challenge variables
    SEARCH_PHRASE = storage.get_text("SEARCH_PHRASE")

    MONTHS = int(storage.get_text("MONTHS"))

    # Each search may return different sections.
    # For this reason, it is not valid to map an object with all available sections.
    # In this case, here is an example of recurring sections:

    # Arts, Books, Business, New York, Opinion, Style, Technology, U.S., World

    # If you want to add a specific section,
    # just insert it into the asset "SECTIONS" separated by comma and space (in case you're using Robocorp)
    # Otherwise this variable is an array
 
    # Example:
    # SECTIONS = Arts, Books

    # If the array becomes empty, the automation will maintain
    # the default sections configuration.
    SECTIONS = storage.get_text("SECTIONS").split(", ")

    # Complementary
    URL = "https://www.nytimes.com/"
    IMG_FOLDER = os.path.join(os.getcwd(), "output")
    EXCEL_FILE = os.path.join(os.getcwd(), "output/result.xlsx")