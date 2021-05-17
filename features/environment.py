from behave import fixture, use_fixture
from selenium import webdriver
from page_objects import GooglePageObject, WikipediaPageObject


@fixture
def init_browser_firefox(context):
    browser = webdriver.Firefox()

    context.google = GooglePageObject(browser)
    context.wikipedia = WikipediaPageObject(browser)

    yield context

    browser.quit()


def before_all(context):
    use_fixture(init_browser_firefox, context)
