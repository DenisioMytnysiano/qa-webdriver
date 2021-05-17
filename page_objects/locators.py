from selenium.webdriver.common.by import By


def pass_locator_params(locator: tuple[str, str], **kwargs) -> tuple[str, str]:
    by, path = locator
    return by, path.format(**kwargs)


class GoogleLocators:
    SEARCH = (
        By.CSS_SELECTOR,
        "input[title='Search']"
    )

    ARTICLE = (
        By.CSS_SELECTOR,
        "a[href*='en.wikipedia']"
    )


class WikipediaLocators:

    AUTHOR = (
        By.XPATH,
        "//a[contains(@title, 'Single')]/../a[2]"
    )

    RELEASE_YEAR = (
        By.XPATH,
        "//th[text()='Recorded']/../td"
    )
