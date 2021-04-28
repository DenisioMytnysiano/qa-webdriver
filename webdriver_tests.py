import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
WEBSITE_URL = 'https://www.kaggle.com/'


def get_element_by_css(driver, css_selector: str, timeout: int = 10):
    try:
        wait = WebDriverWait(driver, timeout)
        locator = (By.CSS_SELECTOR, css_selector)
        return wait.until(EC.presence_of_element_located(locator))
    except TimeoutException:
        raise Exception("Could not find element")


class KaggleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_sign_in_button(self):
        self.driver.get(WEBSITE_URL)
        sign_in_link = get_element_by_css(
            driver=self.driver,
            css_selector='a[href*="SignIn"]'
        )
        sign_in_link.click()

        header = get_element_by_css(
            driver=self.driver,
            css_selector="div span"
        )
        assert header.text == "Sign In"

    def test_categories(self, category: str = "Code"):
        self.driver.get(WEBSITE_URL)
        category_button = get_element_by_css(
            driver=self.driver,
            css_selector=f'a[href="/{category.lower()}"]'
        )
        category_button.click()
        header = get_element_by_css(
            driver=self.driver,
            css_selector="div h1"
        )
        assert header.text == "Code"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
