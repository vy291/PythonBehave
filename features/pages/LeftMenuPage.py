from features.locators import Locator


class LeftMenu(object):

    def __init__(self, WebDriverBase):
        self.web_driver = WebDriverBase

    def clickLeftMenuButton(self):
        return self.web_driver.findById(Locator.leftMenuButtonId).click()


class Logout(object):

    def __init__(self, WebDriverBase):
        self.web_driver = WebDriverBase

    def clickLogoutButton(self):
        return self.web_driver.findById(Locator.leftMenuLogoutButtonId).click()
