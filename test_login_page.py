from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage


def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
