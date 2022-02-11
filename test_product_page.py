from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
import time
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, url)
	product_page.open()
	product_page.add_to_basket()

	product_page.should_be_equal_product_price_and_basket_total()
	product_page.should_be_product_title_in_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, url)
	product_page.open()
	product_page.add_to_basket()
	product_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
	url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	product_page = ProductPage(browser, url)
	product_page.open()
	product_page.add_to_basket()
	product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
	page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty(), "Basket is not empty"
    basket_page.should_be_basket_empty_message(), "Tere is not message for empty basket"

class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		url = "http://selenium1py.pythonanywhere.com/accounts/login/"
		login_page = LoginPage(browser, url)
		login_page.open()

		email = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(email, "abcd1234F")
		login_page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, url)
		product_page.open()
		product_page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		product_page = ProductPage(browser, url)
		product_page.open()
		product_page.add_to_basket()

		product_page.should_be_equal_product_price_and_basket_total()
		product_page.should_be_product_title_in_success_message()

		