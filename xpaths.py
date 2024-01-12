class Home_Page:
    """
    Class representing elements on the home page.
    """
    class Button:
        """
        Subclass containing XPath strings for buttons on the home page.
        """
        SEARCH = "xpath://button[@aria-controls='search-input' and @data-testid='search-button']"
        GO = "xpath://button[@data-testid='search-submit']"
        ACCEPT_COOKIES = "xpath://button[text()='Accept all']"

    class Input:
        """
        Subclass containing XPath string for the search input on the home page.
        """
        SEARCH = "xpath://input[@data-testid='search-input']"


class News_Page:
    """
    Class representing elements on the news page.
    """
    class Select:
        """
        Subclass containing XPath strings for the sorting select element on the news page.
        """
        SORT = "xpath://select[@data-testid='SearchForm-sortBy']"
        VALUE = "newest"

    class List_Item:
        """
        Subclass containing XPath string for the list items representing search results on the news page.
        """
        RESULTS = "xpath:(//li[@data-testid='search-bodega-result'])"

    class Span:
        """
        Subclass containing XPath string for spans representing dates on the news page.
        """
        DATES = "xpath://li[@data-testid='search-bodega-result']/descendant::span[@data-testid='todays-date']"

    class Button:
        """
        Subclass containing XPath string for the 'Show More' button on the news page.
        """
        SHOW_MORE = "xpath://button[@data-testid='search-show-more-button']"

    class Label:
        """
        Subclass containing XPath string for the 'Section' label on the news page.
        """
        SECTION = "xpath://label[text()='Section']"


class Result:
    """
    Class representing elements of a search result.
    """
    TITLE = "h4[1]"
    DESCRIPTION = "p[2]"
    DATE = "span[1]"
    IMAGE = "img[1]"
