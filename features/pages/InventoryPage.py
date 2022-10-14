from features.locators import Locator
from selenium.common.exceptions import NoSuchElementException


class Inventory(object):

    def __init__(self, WebDriverBase):
        self.web_driver = WebDriverBase

    def addNewItem(self, itemName):
        return self.web_driver.findByXpath(Locator.inventoryItemXpath(itemName)).click()

    def verifyShoppingCartIconUpdated(self):
        try:
            self.web_driver.findByXpath(Locator.inventoryShoppingCartBadgeXpath)
        except NoSuchElementException:
            return False
        return True
