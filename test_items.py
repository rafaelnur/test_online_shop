import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_button_add_to_basket_is_visible(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button is not None, "Not found"
