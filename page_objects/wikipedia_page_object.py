from page_objects import PageObjectBase
from selenium.webdriver.remote.webdriver import WebDriver
from .locators import WikipediaLocators, pass_locator_params

class WikipediaPageObject(PageObjectBase):

    def __init__(self, driver: WebDriver):
        super().__init__(driver, "https://en.wikipedia.org")

    def get_song_release_year(self) -> int:
        release_year_bar = self.get_first_element(
            WikipediaLocators.RELEASE_YEAR
        )
        return release_year_bar.text

    def get_song_author(self) -> str:
        author_bar = self.get_first_element(
            pass_locator_params(WikipediaLocators.AUTHOR)
        )
        return author_bar.text
