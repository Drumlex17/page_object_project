import math

from.base_page import BasePage
from .locators import PageProductLocator
from selenium.common.exceptions import NoAlertPresentException
class PageProduct(BasePage):
    def should_be_product_page(self):
        self.adding_to_cart()
        self.solve_quiz_and_get_code()
        self.text_name_product()
        self.text_price_product()
    def adding_to_cart(self):
        cart_link = self.browser.find_element(*PageProductLocator.PRODUCT_LINK)
        cart_link.click()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def text_name_product(self):
        name_product = self.browser.find_element(*PageProductLocator.NAME_PRODUCT)
        alert_name_product = self.browser.find_element(*PageProductLocator.NAME_ALERT_PRODUCT)
        assert name_product.text == "Coders at Work"
        assert alert_name_product.text == name_product.text
        return name_product
    def text_price_product(self):
        price = self.browser.find_element(*PageProductLocator.PRICE_PRODUCT)
        alert_price = self.browser.find_element(*PageProductLocator.PRICE_ALERT_PRODUCT)
        assert price.text == "£19.99"
        assert alert_price.text == price.text
        return price