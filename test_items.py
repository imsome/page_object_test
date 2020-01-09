from selenium.common.exceptions import NoSuchElementException


def test_page_should_contain_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    browser.get(link)
    try:
        button = browser.find_element_by_xpath('//button[@type="submit"][@class="btn btn-lg btn-primary btn-add-to-basket"]')
    except NoSuchElementException:
        return False
