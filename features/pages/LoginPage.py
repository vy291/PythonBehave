from features.locators import Locator
from selenium.common.exceptions import NoSuchElementException


class Login(object):

    def __init__(self, WebDriverBase):
        self.web_driver = WebDriverBase

    def inputUsername(self, username):
        return self.web_driver.findById(Locator.loginUsernameId).send_keys(username)

    def inputPassword(self, password):
        return self.web_driver.findById(Locator.loginPasswordId).send_keys(password)

    def clickSubmitButton(self):
        return self.web_driver.findById(Locator.loginSubmitButtonId).click()

    def verifyLoginSuccessfully(self, context):
        try:
            self.web_driver.findByXpath(Locator.inventoryProductHeaderXpath)
        except NoSuchElementException:
            return False
        return True

    def verifyLoginError(self):
        return str(self.web_driver.findByXpath(Locator.loginErrorXpath).text)

    def verifyLoginPageDisplays(self):
        try:
            self.web_driver.findById(Locator.loginSubmitButtonId)
        except NoSuchElementException:
            return False
        return True
