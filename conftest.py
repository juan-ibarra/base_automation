import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def chrome_driver():
    driver = Chrome()
    driver.implicitly_wait(10)
    # driver.maximize_window()

    yield driver
    driver.quit()
