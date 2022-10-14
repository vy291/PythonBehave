from features.locators import Locator
from selenium.common.exceptions import NoSuchElementException


class Cart(object):

    def __init__(self, WebDriverBase):
        self.web_driver = WebDriverBase

    def clickShoppingCartIcon(self):
        return self.web_driver.findById(Locator.cartShoppingIconId).click()

    def verifyItemInShoppingCartExists(self, itemName):
        try:
            self.web_driver.findByXpath(Locator.cartAddedItemXpath(itemName))
        except NoSuchElementException:
            return False
        return True

    def clickCheckoutButton(self):
        return self.web_driver.findById(Locator.cartCheckoutButtonId).click()

    def clickContinueButton(self):
        return self.web_driver.findById(Locator.cartContinueButtonId).click()

    def clickFinishButton(self):
        return self.web_driver.findById(Locator.cartFinishButtonId).click()

    def inputFirstName(self, firstName):
        return self.web_driver.findById(Locator.cartInformationFirstNameId).send_keys(firstName)

    def inputLastName(self, lastName):
        return self.web_driver.findById(Locator.cartInformationLastNameId).send_keys(lastName)

    def inputZipCode(self, zipCode):
        return self.web_driver.findById(Locator.cartInformationZipCodeId).send_keys(zipCode)

    def verifyCheckoutCompleted(self):
        try:
            self.web_driver.findByXpath(Locator.cartCompleteOrderMessageXpath)
        except NoSuchElementException:
            return False
        return True
