import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
WEBSITE_URL = 'https://www.kaggle.com/'


class KaggleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def get_with_wait(self, selector: str = None, timeout: int = 10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            locator = (By.CSS_SELECTOR, selector)
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception("Could not find element")

    def test_sign_in_button(self):
        self.driver.get(WEBSITE_URL)
        sign_in_link = self.get_with_wait(
            selector='a[class="sc-pBolk kPdszo"]'
        )
        sign_in_link.click()

        header = self.get_with_wait(
            selector="span[class='sc-fznxKY sc-fznMAR cRheSr']"
        )
        assert header.text == "Sign In"

    def test_categories(self, category: str = "Code"):
        self.driver.get(WEBSITE_URL)
        category_button = self.get_with_wait(
            selector=f'a[href="/{category.lower()}"]'
        )
        category_button.click()
        header = self.get_with_wait(
            selector="h1[class='sc-fznKkj sc-fznZeY sc-pYOYC bwpFPB']"
        )
        assert header.text == "Code"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
