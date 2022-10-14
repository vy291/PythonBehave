from behave import when, then
from features.pages.LeftMenuPage import Logout
from features.pages.LeftMenuPage import LeftMenu
from features.pages.LoginPage import Login
from utilities.BaseDriver import WebDriverBase


@when('we click log out on left menu page')
def step(context):
    LeftMenu(WebDriverBase(context.browser)).clickLeftMenuButton()
    Logout(WebDriverBase(context.browser)).clickLogoutButton()


@then('it should logout successfully and back to login page')
def step(context):
    Login(WebDriverBase(context.browser)).verifyLoginPageDisplays()
