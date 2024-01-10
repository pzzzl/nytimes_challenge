from imports import *

class Challenge:
    def __init__(self):
        self.driver = Selenium()
        self.start_date = get_start_date(Variables.MONTHS)
        self.end_date = get_end_date()
        
    def open_browser(self, url: str) -> None:
        self.driver.open_available_browser(url, maximized = True)
    
    def search(self, text: str) -> None:
        self.driver.click_button(Home.Button.SEARCH)
        self.driver.input_text_when_element_is_visible(Home.Input.SEARCH, text)
        self.driver.click_element_when_clickable(Home.Button.GO)

    def sort_news(self) -> None:
        self.driver.select_from_list_by_value(News.Select.SORT, News.Select.VALUE)
        sleep(3)

    def run(self) -> None:
        self.open_browser(Variables.URL)
        self.search(Variables.SEARCH_PHRASE)
        self.sort_news()

        self.dates_elements = self.driver.find_elements(News.Span.DATES)

        show_more = True

        while show_more:
            for date_element in self.dates_elements:
                try:
                    date_to_analyze = date_element.get_attribute("aria-label")
                    result = is_date_between(self.start_date, date_to_analyze, self.end_date)
                    print(f"Analyzing date {date_to_analyze}\nResult: {result}")
                except:
                    pass

        sleep(999)