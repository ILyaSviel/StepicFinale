from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.ID, "login_form")
	REGISTER_FORM = (By.ID, "register_form")
	REGISTRATION_EMAIL_INPUT = (By.ID, "id_registration-email")
	REGISTRATION_PASSWORD_INPUT = (By.ID, "id_registration-password1")
	REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.ID, "id_registration-password2")
	REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
	BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
	ALERT_ADDED_TO_BASKET_TITLE = (By.CSS_SELECTOR, ".alert strong")
	ALERT_ADDED_TO_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items row")
	BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
