from base.base import Base


class DuckDuckGoSearchPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_FIELD = 'search_form_input_homepage'

    def __init__(self, webdriver):
        self.driver = webdriver
        self.base = Base(self.driver)

    def load(self):
        return self.base.open_browser(self.URL)

    def search(self, text_to_search):
        self.base.input_text(text_to_search, self.SEARCH_FIELD, "id")
        self.base.click_element("//input[@id='search_button_homepage']", "xpath")
