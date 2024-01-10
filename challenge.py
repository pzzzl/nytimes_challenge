from imports import *

class Challenge:
    def __init__(self):
        self.driver = Selenium()
        self.start_date = get_start_date(Variables.MONTHS)
        self.end_date = get_end_date()
        
    def open_browser(self, url: str) -> None:
        self.driver.open_available_browser(url, maximized = True)

    def accept_cookies(self) -> None:
        self.driver.click_button_when_visible(Home.Button.ACCEPT_COOKIES)
    
    def search(self, text: str) -> None:
        self.driver.click_button(Home.Button.SEARCH)
        self.driver.input_text_when_element_is_visible(Home.Input.SEARCH, text)
        self.driver.click_element_when_clickable(Home.Button.GO)

    def sort_news(self) -> None:
        self.driver.select_from_list_by_value(News.Select.SORT, News.Select.VALUE)
        sleep(3)

    def show_more(self) -> None:
        print("Clicking button 'Show More'")
        self.driver.click_element_when_clickable(News.Button.SHOW_MORE)

    def run(self) -> None:
        self.open_browser(Variables.URL)
        self.accept_cookies()
        self.search(Variables.SEARCH_PHRASE)
        self.sort_news()

        self.dates_elements = self.driver.find_elements(News.Span.DATES)

        self.last_date = self.dates_elements[-1].get_attribute('aria-label')

        print(self.last_date)
        self.need_to_show_more = is_date_between(self.start_date, self.last_date, self.end_date)
        print("Need to show more:", self.need_to_show_more)

        if self.need_to_show_more:
            self.show_more()

        sleep(999)