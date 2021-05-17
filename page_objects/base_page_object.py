from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import pass_locator_params

class PageObjectBase:

    def __init__(self, driver: WebDriver, url: str) -> None:
        self.url = url
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.url)

    def get_elements(self, locator, wait_time: int = 10) -> list[WebElement]:
        try:
            locator = pass_locator_params(locator)
            wait = WebDriverWait(self.driver, timeout=wait_time)
            return wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise Exception("Elements not found")

    def get_first_element(self, locator, wait_time: int = 10) -> WebElement:
        return self.get_elements(locator, wait_time)[0]

    def get_page_title(self) -> str:
        return self.driver.title

