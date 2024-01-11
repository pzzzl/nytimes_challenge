class Home_Page:
    class Button:
        SEARCH = "xpath://button[@aria-controls='search-input' and @data-testid='search-button']"
        GO = "xpath://button[@data-testid='search-submit']"
        ACCEPT_COOKIES = "xpath://button[text()='Accept all']"
    class Input:
        SEARCH = "xpath://input[@data-testid='search-input']"

class News_Page:
    class Select:
        SORT = "xpath://select[@data-testid='SearchForm-sortBy']"
        VALUE = "newest"
    class List_Item:
        RESULTS = "xpath:(//li[@data-testid='search-bodega-result'])"
    class Span:
        DATES = "xpath://li[@data-testid='search-bodega-result']/descendant::span[@data-testid='todays-date']"
    class Button:
        SHOW_MORE = "xpath://button[@data-testid='search-show-more-button']"

class Result:
    TITLE = "h4[1]"
    DESCRIPTION = "p[2]"
    DATE = "span[1]"
    IMAGE = "img[1]"