from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    LOGIN_EMAIL_TEXTBOX = (By.XPATH, '//input[@name="login-username"]')
    LOGIN_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="login-password"]')
    LOGIN_FORGOT_PASSWORD_TEXT_LINK = (By.XPATH, "//p/a")
    LOGIN_BUTTON_TO_LOGIN = (By.XPATH, '//button[@name="login_submit"]')
    REGISTER_EMAIL_TEXTBOX = (By.XPATH, '//input[@name="registration-email"]')
    REGISTER_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_TEXTBOX = (By.XPATH, '//input[@name="registration-password2"]')
    REGISTER_BUTTON_TO_REGISTER = (By.XPATH, '//button[@name="registration_submit"]')
