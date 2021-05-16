from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXPLICIT_WAIT = 30


class Base:
    def __init__(self, driver, by, locator):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_WAIT, poll_frequency=1)

    def by_type(self, locator_type):
        locator_type = locator_type.lower()
        locator = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT
        }
        return locator[locator_type]

    def get_element(self, locator, locator_type="xpath"):
        element = None
        try:
            by_type = self.by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
        except Exception as e:
            print(e)
        return element

    def wait_for_element(self, locator, locator_type="xpath", timeout=10, poll_frecuency=0.5):
        element = None
        try:
            by_type = self.by_type(locator)
            print(f"Waiting for maximun {timeout} seconds")
            element = self.wait.until(EC.element_to_be_clickable((by_type, locator)))
            return element
        except Exception as e:
            print(f"ERROR: {e}")
            return element

    def click_element(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        element.click()

    def input_text(self, text, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        element.send_keys(text)

    def clear_element_text(self, locator, locator_type="xpath"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
        except:
            print(f"Element {locator} Not Found")

    def is_element_present(self, locator, locator_type="xpath"):
        """
        Verify if element is visible
        :param locator_type: str, type of locator
        :param locator: str, string locator
        :return: bool,
        """
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element Not Found")
                return False
        except Exception as e:
            print(f"Element Not Found. ERROR: {e}")
            return False
