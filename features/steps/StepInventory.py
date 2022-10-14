from behave import when, then
from features.pages.InventoryPage import Inventory
from utilities.BaseDriver import WebDriverBase


@when('we add new item "{itemName}" from inventory')
def step(context, itemName):
    Inventory(WebDriverBase(context.browser)).addNewItem(itemName)


@when('cart icon should be updated')
def step(context):
    Inventory(WebDriverBase(context.browser)).verifyShoppingCartIconUpdated()
