class Home:
    class Button:
        SEARCH = "xpath://button[@aria-controls='search-input' and @data-testid='search-button']"
        GO = "xpath://button[@data-testid='search-submit']"
    class Input:
        SEARCH = "xpath://input[@data-testid='search-input']"

class News:
    class Select:
        SORT = "xpath://select[@data-testid='SearchForm-sortBy']"
        VALUE = "newest"
    class List_Item:
        RESULTS = "xpath://li[@data-testid='search-bodega-result']"
    class Span:
        DATES = "xpath://li[@data-testid='search-bodega-result']/descendant::span[@data-testid='todays-date']"