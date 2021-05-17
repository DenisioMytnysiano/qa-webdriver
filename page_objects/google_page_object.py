from page_objects import PageObjectBase
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .locators import GoogleLocators


class GooglePageObject(PageObjectBase):

    def __init__(self, driver: WebDriver):
        super().__init__(driver, "https://www.google.com/?hl=en")

    def search(self, query: str) -> None:
        search = self.get_first_element(
            GoogleLocators.SEARCH
        )
        search.send_keys(query)
        search.send_keys(Keys.ENTER)

    def open_wikipedia(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(
            GoogleLocators.ARTICLE
        )).click()


