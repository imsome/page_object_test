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

    def compare_product_names(self):
        product_base_name = str(self.browser.find_element(*ProductPageLocators.PRODUCT_ITEM_NAME).text)
        product_alert_name = str(self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_RESPONSE).text)
        assert product_base_name == product_alert_name, "Product name is {product}, alert name is {alert}".format(
            product=product_base_name, alert=product_alert_name)

    def compare_solo_item_and_cart_price(self):
        item_price = str(self.browser.find_element(*ProductPageLocators.PRODUCT_ITEM_PRICE).text)
        cart_price = str(self.browser.find_element(*ProductPageLocators.PRODUCT_FINAL_CART_PRICE).text)
        assert item_price == cart_price, "Item price is {item}, cart price is {cart}".format(item=item_price,
                                                                                             cart=cart_price)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_ALERT_RESPONSE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_ALERT_RESPONSE), "Success message should disappear, but it didn't"
