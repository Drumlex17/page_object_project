# from selenium.webdriver.common.by import By
# from.base_page import BasePage
# from .locators import MainPageLocators
# class MainPage(BasePage):
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#         login_link.click()
#     def should_be_login_link(self):
#         # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid") # Специально здесь указали некорректный селектор
#         assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" # Добавили исключение и правильный селектор



from.base_page import BasePage
from .locators import MainPageLocators
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"