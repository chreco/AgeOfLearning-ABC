from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage

"""
    Shadow DOM code here
"""


class SubscriptionPage(BasePage):
    __register_page_url = 'https://www.abcmouse.com/abt/subscription'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__register_page_url

