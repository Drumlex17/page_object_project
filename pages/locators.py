from selenium.webdriver.common.by import By
class MainPageLocators(): # Данный класс будет соответствовать каждому классу PageObject
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Теперь каждый селектор — это пара: как искать и что искать
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class PageProductLocator():
    PRODUCT_LINK = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    NAME_PRODUCT = (By.XPATH, "//h1[text()='Coders at Work']")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    NAME_ALERT_PRODUCT = (By.XPATH, "//strong[text()='Coders at Work']")
    PRICE_ALERT_PRODUCT = (By.XPATH, "//strong[text()='£19.99']")