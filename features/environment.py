from utilities.BrowserSelection import getBrowser
from utilities.Common import getBrowserName


def before_scenario(context, scenario):
    context.browser = getBrowser(getBrowserName())


def after_scenario(context, scenario):
    scenarioName = str(context.scenario).replace('-- @1.1', '').replace('"', '').replace('<', '').replace('>', '').strip()
    if str(context.failed) != 'False':
        context.browser.get_screenshot_as_file('./screenShot/%s.png' % scenarioName)
    context.browser.quit()


def after_all(context):
    pass
