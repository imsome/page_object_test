from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "Login not in current browser URL"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_TEXTBOX)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_TEXTBOX)
        self.browser.find_element(*LoginPageLocators.LOGIN_FORGOT_PASSWORD_TEXT_LINK)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_TO_LOGIN)
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_TEXTBOX)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_TEXTBOX)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_TEXTBOX)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_TO_REGISTER)
        assert True
