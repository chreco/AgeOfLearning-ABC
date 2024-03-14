import pytest
from selenium import webdriver


# from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def driver():
    # Adding arguments to handle when site sometimes blocks automation with 403
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    my_driver = webdriver.Chrome(options=options)
    yield my_driver  # yield will allow commands after; return will end method immediately
