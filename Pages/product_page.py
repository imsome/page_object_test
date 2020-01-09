from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def add_product_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BUTTON_ADD_ITEM_TO_CART)
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON_ADD_ITEM_TO_CART)
        button_add_to_cart.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
