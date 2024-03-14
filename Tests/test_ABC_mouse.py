import pytest
from selenium.webdriver.common.by import By

from page_objects.abc_homepage import HomePage


class Tests:

    @pytest.mark.signup
    def test_abc_mouse_new_signup(self, driver):

        # Go to https://www.abcmouse.com
        # Click the 'Sign Up' button
        sign_up = HomePage(driver)
        HomePage.open()

        # Verify that 'https://www.abcmouse.com/abt/register'page is returned
        actual_register_url = driver.current_url
        expected_register_url = 'https://www.abcmouse.com/abt/register'
        assert actual_register_url == expected_register_url

        # Enter Email address (any email address) - *** Use 'send_keys' here

        # Click “Submit” button

        # Verify that 'https://www.abcmouse.com/abt/subscription' page is returned.
        actual_subscription_url = driver.current_url
        expected_subscription_url = 'https://www.abcmouse.com/abt/subscription'
        assert actual_subscription_url == expected_subscription_url

        # Verify that on subscription page, “Become a Member!” text is rendered.
        expected_text = "Become a Member!"
        actual_text = driver.find_element(By.LINK_TEXT, "Become a Member!")
        assert actual_text.is_displayed()
