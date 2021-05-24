from pages.search import DuckDuckGoSearchPage
from pages.results import DuckDuckGoResultPage


class TestWeb:
    def test_basico_busqueda_duckduckgo(self, chrome_driver):
        BUSQUEDA = 'Automation'
        search_page = DuckDuckGoSearchPage(chrome_driver)
        result_page = DuckDuckGoResultPage(chrome_driver)

        search_page.load()
        search_page.search(BUSQUEDA)

        assert result_page.link_div_count() > 0
        assert result_page.phrase_result_count(BUSQUEDA) > 0
        assert result_page.search_input_value() == BUSQUEDA
