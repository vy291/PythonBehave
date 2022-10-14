import json
from behave import when, then, given
from features.pages.LoginPage import Login
from utilities.BaseDriver import WebDriverBase


@given('we visit login page')
def step(context):
    WebDriverBase(context.browser).open()


@when('we put username "{username}" on login page')
def step(context, username):
    Login(WebDriverBase(context.browser)).inputUsername(username)


@when('we put password "{password}" on login page')
def step(context, password):
    Login(WebDriverBase(context.browser)).inputPassword(password)


@when('we click submit button on login page')
def step(context):
    Login(WebDriverBase(context.browser)).clickSubmitButton()


@then('it should login successfully')
def step(context):
    Login(WebDriverBase(context.browser)).verifyLoginSuccessfully(context)


@then('it should have error when login with wrong credential')
def step(context):
    expectedError = 'Username and password do not match any user in this service'
    actualError = Login(WebDriverBase(context.browser)).verifyLoginError()
    if expectedError in actualError:
        return True
    else:
        return False


@when('we put username on login page from data file "{fileName}"')
def step(context, fileName):
    with open('./data/%s' % fileName, 'r') as f:
        username = str(json.load(f)["username"])
    Login(WebDriverBase(context.browser)).inputUsername(username)


@when('we put password on login page from data file "{fileName}"')
def step(context, fileName):
    with open('./data/%s' % fileName, 'r') as f:
        password = str(json.load(f)["password"])
    Login(WebDriverBase(context.browser)).inputPassword(password)


@then('it should have error when login with locked out user')
def step(context):
    expectedError = 'Sorry, this user has been locked out'
    actualError = Login(WebDriverBase(context.browser)).verifyLoginError()
    if expectedError in actualError:
        return True
    else:
        return False
