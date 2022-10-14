from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox import options
from selenium import webdriver


def getBrowser(browser):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(options=chrome_options)

    if browser == "firefox":
        firefox_options = options.Options()
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Firefox(options=firefox_options)




