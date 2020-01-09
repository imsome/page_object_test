from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_EMAIL_TEXTBOX = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_FORGOT_PASSWORD_TEXT_LINK = (By.XPATH, "//p/a")
    LOGIN_BUTTON_TO_LOGIN = (By.XPATH, '//button[@name="login_submit"]')
    REGISTER_EMAIL_TEXTBOX = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_BUTTON_TO_REGISTER = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_BUTTON_ADD_ITEM_TO_CART = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_ALERT_RESPONSE = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_ITEM_NAME = (By.XPATH, '//div/h1')
    PRODUCT_ITEM_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    PRODUCT_FINAL_CART_PRICE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]//strong')
    PRODUCT_SUCCESS_MESSAGE = (By.XPATH, '')

