# Standard libraries
import json
from time import sleep
from datetime import datetime

# Third-party libraries
from RPA.Browser.Selenium import Selenium

# Local imports
from config import Variables
from challenge_resources import is_date_between, get_start_date, download_image, create_excel_file, delete_paths, count_occurrences, verify_money_format
from challenge_resources import Home_Page, News_Page, Result

class Challenge:
    def __init__(self):
        """
        Initializes the Challenge class.

        Initializes Selenium, retrieves the start and end dates,
        initializes the news list, prints relevant information,
        and deletes specific paths.
        """
        self.driver = Selenium()
        self.start_date = get_start_date(Variables.MONTHS)
        self.end_date = datetime.now().strftime("%m/%d/%Y")
        self.news = []
        delete_paths([Variables.EXCEL_FILE, Variables.IMG_FOLDER])

    def open_browser(self, url: str) -> None:
        """
        Opens a browser with the provided URL.

        Args:
        url (str): The URL to open in the browser.
        """
        print("Opening browser")
        self.driver.open_available_browser(url, maximized=True)

    def accept_cookies(self) -> None:
        """
        Accepts cookies by clicking the corresponding button if available.
        """
        print("Accepting cookies")
        try:
            self.driver.click_element_when_clickable(Home_Page.Button.ACCEPT_COOKIES)
        except:
            print("Unable to find the accept cookies button")

    def search(self, text: str) -> None:
        """
        Searches for a given phrase.

        Args:
        text (str): The text to search for.
        """
        print(f"Searching for phrase '{text}'")
        self.driver.click_button(Home_Page.Button.SEARCH)
        self.driver.input_text_when_element_is_visible(Home_Page.Input.SEARCH, text)
        self.driver.click_element_when_clickable(Home_Page.Button.GO)

    def set_sections(self, sections: list) -> None:
        """
        Sets the sections to filter news.

        Args:
        sections (list): List of sections to select.
        """
        if sections:
            print("Sections:", sections)
            self.driver.click_element_when_clickable(News_Page.Label.SECTION)
            for section in sections:
                print("Selecting section", section)
                try:
                    self.driver.click_element_when_clickable(f"xpath://span[text()='{section}']/preceding::input[1]")
                except:
                    print(f"Unable to select the '{section}' section")
        else:
            print("Keeping the default section (Any)")

    def sort_news(self) -> None:
        """
        Sorts news by the latest date.
        """
        print("Sorting news by the latest")
        self.driver.select_from_list_by_value(News_Page.Select.SORT, News_Page.Select.VALUE)
        sleep(3)

    def check_if_last_date_is_between_start_and_end_dates(self) -> bool:
        """
        Checks if the last date in the retrieved news is between the start and end dates.

        Returns:
            - bool: True if the last date is between the start and end dates (inclusive), False otherwise.
        """
        dates_elements = self.driver.find_elements(News_Page.Span.DATES)
        last_date = dates_elements[-1].get_attribute('aria-label')
        last_date_is_between_start_and_end_dates = is_date_between(self.start_date, last_date, self.end_date)
        return last_date_is_between_start_and_end_dates

    def show_more_news_routine(self) -> None:
        """
        Shows all news that match the criteria by repeatedly clicking the 'Show More' button.
        """
        print("Showing all news that match the criteria, please wait...")
        need_to_show_more = self.check_if_last_date_is_between_start_and_end_dates()

        while need_to_show_more:
            self.driver.click_element_when_clickable(News_Page.Button.SHOW_MORE)
            need_to_show_more = self.check_if_last_date_is_between_start_and_end_dates()
        sleep(3)

    def get_info(self, result_xpath_index: int) -> dict[str, any]:
        """
        Retrieves information for a specific news result.

        Args:
        result_xpath_index (int): The index of the news result in XPath format - starting at 1.

        Returns:
        dict[str, any]: A dictionary containing information about the news result.
        """
        base_xpath = f"{News_Page.List_Item.RESULTS}[{result_xpath_index}]/descendant::"
        
        title_xpath = base_xpath + Result.TITLE
        date_xpath = base_xpath + Result.DATE
        description_xpath = base_xpath + Result.DESCRIPTION
        image_xpath = base_xpath + Result.IMAGE

        title = self.driver.find_element(title_xpath).text
        date = self.driver.find_element(date_xpath).get_attribute('aria-label')
        try:
            description = self.driver.find_element(description_xpath).text
        except:
            description = ""
        try:
            image_url = self.driver.find_element(image_xpath).get_attribute('src')
            image_file_name = download_image(image_url, Variables.IMG_FOLDER)
            if not image_file_name:
                image_file_name = "Image download failed"
        except:
            image_file_name = "Missing image"

        obj = {
        "id": result_xpath_index,
        "title": title,
        "date": date,
        "description": description,
        "image_file_name": image_file_name,
        "count_title": count_occurrences(title, Variables.SEARCH_PHRASE),
        "count_description": count_occurrences(description, Variables.SEARCH_PHRASE),
        "contains_money": verify_money_format(title) or verify_money_format(description)
        }

        return obj

    def get_news(self) -> None:
        """
        Retrieves news information based on specified criteria.
        """
        all_news = self.driver.find_elements(News_Page.List_Item.RESULTS)

        for index, _ in enumerate(all_news, start=1):
            info = self.get_info(index)
            
            if not is_date_between(self.start_date, info['date'], self.end_date):
                print(f"The date {info['date']} is not valid. Finishing extraction.")
                break
            else:
                self.news.append(info)
                print(json.dumps(info, indent=2, ensure_ascii=False))

        print("Found news:", len(self.news))

    def run(self) -> None:
        """
        Executes the entire process to retrieve and process news information.
        """
        self.open_browser(Variables.URL)
        self.accept_cookies()
        self.search(Variables.SEARCH_PHRASE)
        self.set_sections(Variables.SECTIONS)
        self.sort_news()
        self.show_more_news_routine()
        self.get_news()
        create_excel_file(Variables.EXCEL_FILE, self.news)
