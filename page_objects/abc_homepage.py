from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage


class HomePage(BasePage):
    """
    Trying to figure out shadow root :/

    # Find the shadow root element
    shadow_root = driver.execute_script("return document.querySelector('your_shadow_root_selector').shadowRoot")

    # Use the shadow root to find elements within the shadow DOM
    element_within_shadow_dom = shadow_root.find_element_by_css_selector('your_element_selector_within_shadow_dom')

    # Perform actions on the element
    element_within_shadow_dom.click()

    # Shadow DOM
    sign_up_button = driver.execute_script(
        'return document.querySelector("body > route-view").shadowRoot.querySelector('
        '"#page-component").shadowRoot.querySelector("main-layout > header > home-header > '
        'authstate-context:nth-child(3) > signup-button")')
    driver.execute_script('arguments[0].click();', sign_up_button)

    """

    __sign_up_button = (By.CSS_SELECTOR, '<shadow_sign_up_button>')
    __url = "https://www.abcmouse.com"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_sign_up(self):
        super()._click(self.__sign_up_button)
