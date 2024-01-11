from imports import *

class Challenge:
    def __init__(self):
        close_all_browsers()
        self.driver = Selenium()
        self.start_date = get_start_date(Variables.MONTHS)
        self.end_date = get_end_date()
        print("Months:", Variables.MONTHS)
        print("Start date:", self.start_date)
        print("End date:", self.end_date)
        
    def open_browser(self, url: str) -> None:
        print("Opening browser")
        self.driver.open_available_browser(url, maximized = True)

    def accept_cookies(self) -> None:
        print("Accepting cookies")
        self.driver.click_element_when_clickable(Home_Page.Button.ACCEPT_COOKIES)
    
    def search(self, text: str) -> None:
        print(f"Searching for phrase '{text}'")
        self.driver.click_button(Home_Page.Button.SEARCH)
        self.driver.input_text_when_element_is_visible(Home_Page.Input.SEARCH, text)
        self.driver.click_element_when_clickable(Home_Page.Button.GO)

    def sort_news(self) -> None:
        print("Sorting news by latest")
        self.driver.select_from_list_by_value(News_Page.Select.SORT, News_Page.Select.VALUE)
        sleep(3)

    def check_if_last_date_is_between_start_and_end_dates(self):
        print("Checking if last date is between start and end dates")
        self.dates_elements = self.driver.find_elements(News_Page.Span.DATES)
        self.last_date = self.dates_elements[-1].get_attribute('aria-label')
        self.need_to_show_more = is_date_between(self.start_date, self.last_date, self.end_date)
        print(f"Need to show more: {self.need_to_show_more}")

    def show_more_news_routine(self) -> None:
        self.check_if_last_date_is_between_start_and_end_dates()

        while self.need_to_show_more:
            self.driver.click_element_when_clickable(News_Page.Button.SHOW_MORE)
            self.check_if_last_date_is_between_start_and_end_dates()
        sleep(3)

    def get_info(self, result_xpath_index):
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
            description = "Missing description"
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
        "image_file_name": image_file_name
        }

        return obj

    def get_news(self):
        self.news = []
        all_news = self.driver.find_elements(News_Page.List_Item.RESULTS)

        index = 0
        for result in all_news:
            index = index + 1
            info = self.get_info(index)
            if not is_date_between(self.start_date, info['date'], self.end_date):
                print(f"The date {info['date']} is not valid. Finishing extraction.")
                break
            else:
                self.news.append(info)
                print(json.dumps(info, indent = 2, ensure_ascii = False))

        print("Found news:", len(self.news))
            


    def run(self) -> None:
        self.open_browser(Variables.URL)
        self.accept_cookies()
        self.search(Variables.SEARCH_PHRASE)
        self.sort_news()
        self.show_more_news_routine()
        self.get_news()
        create_excel_file("C:/git/nytimes_challenge/result.xlsx", self.news)
        close_all_browsers()