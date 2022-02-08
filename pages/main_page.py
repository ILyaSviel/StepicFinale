from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):

	def go_to_login_page(this):
		login_link = this.browser.find_element(By.ID, "login_link")
		login_link.click()