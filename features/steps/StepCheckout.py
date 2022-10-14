from behave import when, then
from features.pages.CartPage import Cart
from utilities.BaseDriver import WebDriverBase


@when('we visit cart page')
def step(context):
    print('')
    Cart(WebDriverBase(context.browser)).clickShoppingCartIcon()


@then('selected item "{itemName}" should be added in shopping cart')
def step(context, itemName):
    Cart(WebDriverBase(context.browser)).verifyItemInShoppingCartExists(itemName)


@when('we click check out button on checkout page')
def step(context):
    Cart(WebDriverBase(context.browser)).clickCheckoutButton()


@when('we put checkout information "{firstName}" "{lastName}" "{zipCode}" on checkout page')
def step(context, firstName, lastName, zipCode):
    Cart(WebDriverBase(context.browser)).inputFirstName(firstName)
    Cart(WebDriverBase(context.browser)).inputLastName(lastName)
    Cart(WebDriverBase(context.browser)).inputZipCode(zipCode)


@when('we click continue button on checkout page')
def step(context):
    Cart(WebDriverBase(context.browser)).clickContinueButton()


@when('we click finish button on checkout page')
def step(context):
    Cart(WebDriverBase(context.browser)).clickFinishButton()


@then('it should confirm the checkout is completed')
def step(context):
    Cart(WebDriverBase(context.browser)).verifyCheckoutCompleted()
