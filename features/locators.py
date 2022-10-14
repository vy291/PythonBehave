class Locator(object):
    # loginPage
    loginUsernameId = "user-name"
    loginPasswordId = "password"
    loginSubmitButtonId = "login-button"
    loginErrorXpath = "//div[@class='error-message-container error']"

    # inventoryPage
    def inventoryItemXpath(itemName):
         return "//div[@class='inventory_item_description']//div[contains(text(), '%s')]//ancestor::div[@class='inventory_item_description']//button[contains(@id, 'add-to-cart')]" % itemName

    inventoryShoppingCartBadgeXpath = "//a[@class='shopping_cart_link']//span[@class='shopping_cart_badge']"
    inventoryProductHeaderXpath = "//span[@class='title' and text()='Products']"

    # cartPage
    def cartAddedItemXpath(itemName):
        return "//div[@class='inventory_item_name' and text()='%s']" % itemName

    cartShoppingIconId = "shopping_cart_container"
    cartCheckoutButtonId = "checkout"
    cartInformationFirstNameId = "first-name"
    cartInformationLastNameId = "last-name"
    cartInformationZipCodeId = "postal-code"
    cartContinueButtonId = "continue"
    cartFinishButtonId = "finish"
    cartCompleteOrderMessageXpath = "//h2[@class='complete-header' and text()='THANK YOU FOR YOUR ORDER']"

    # leftMenuPage
    leftMenuButtonId = "react-burger-menu-btn"
    leftMenuLogoutButtonId = "logout_sidebar_link"
