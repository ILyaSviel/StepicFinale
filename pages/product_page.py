from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def should_be_add_to_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'Add to bascet is not found'"

	def should_be_basket_mini(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_MINI), "Mini basket is not found"
	
	def get_inner_allert_added_to_basket_total(self):
		return self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET_TOTAL).text

	def get_product_price(self):
		return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

	def get_product_title(self):
		return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

	def get_inner_allert_added_to_basket_title(self):
		return self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET_TITLE).text

	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		button.click()

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"There is success message, that is not should be there"

	def should_disappear_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
		"Success message is not disapearing"

	def should_be_equal_product_price_and_basket_total(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_total = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET_TOTAL).text
		assert product_price == basket_total, "Product price is not equal basket total"

	def should_be_product_title_in_success_message(self):
		product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
		success_message_title = self.browser.find_element(*ProductPageLocators.ALERT_ADDED_TO_BASKET_TITLE).text
		assert product_title == success_message_title,\
		 f"Product title '{product_title}' is not equal product title in the success message"


