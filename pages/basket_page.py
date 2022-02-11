from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def is_basket_empty(self):
		return self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)

	def should_be_basket_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM),\
		"Basket should be empty"

	def is_basket_empty_message(self):
		return self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)

	def should_be_basket_empty_message(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE),\
		"Should be message for empty basket"