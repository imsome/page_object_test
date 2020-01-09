from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_have_empty_list_text(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_LIST_REPORTER), "There is no report about empty list"

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_CART), "Cart list is not empty"
