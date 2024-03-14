import pytest
from selenium.webdriver.common.by import By

from page_objects.abc_homepage import HomePage
from data import test_data
from page_objects.prospect_register_page import ProspectRegisterPage
from page_objects.subscription_page import SubscriptionPage


class Tests:

    @pytest.mark.signup
    def test_abc_mouse_new_signup(self, driver):

        # Go to https://www.abcmouse.com
        # Click the 'Sign Up' button
        sign_up = HomePage(driver)
        sign_up.open()

        # Verify that 'https://www.abcmouse.com/abt/register'page is returned
        actual_register_url = driver.current_url
        assert actual_register_url == sign_up.current_url

        # Enter Email address (any email address)
        # Click “Submit” button
        register = ProspectRegisterPage(driver)
        register.enter_email_and_submit("test@testyMcTesterson")

        # Verify that 'https://www.abcmouse.com/abt/subscription' page is returned.
        subscription = SubscriptionPage(driver)
        actual_subscription_url = driver.current_url
        assert actual_subscription_url == subscription.expected_url

        # Verify that on subscription page, “Become a Member!” text is rendered.
        expected_text = "Become a Member!"
        actual_text = driver.find_element(By.LINK_TEXT, "Become a Member!")
        assert actual_text == expected_text
