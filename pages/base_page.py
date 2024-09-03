from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)
    def is_element_present(self, how, what): # Создали новый метод, который будет перехватывать исключения. Передаём в него два аргумента (как искать - css, id, xpath и т.д.; и что искать - строку-селектор)
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException: # Тут указываем имя исключения
            return False
        return True