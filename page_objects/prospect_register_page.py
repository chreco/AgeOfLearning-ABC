from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage

"""
    Shadow DOM method
"""


class ProspectRegisterPage(BasePage):
    __email_field = (By.CSS_SELECTOR, '')
    __submit_button = (By.CSS_SELECTOR, '')
    __opt_out_checkbox = (By.CSS_SELECTOR, '')
    __register_page_url = 'https://www.abcmouse.com/abt/register'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__register_page_url

    def enter_email_and_submit(self, email):
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__email_field))
        self._driver.find_element(self.__email_field).send_keys(email)
        wait.until(ec.visibility_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()
