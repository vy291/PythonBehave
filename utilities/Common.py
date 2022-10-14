import os
from configparser import ConfigParser

config = ConfigParser()
config.read((os.path.join(os.getcwd(), 'setup.cfg')))


def getBrowserName():
    return config.get('Environment', 'browser')


def getUrl():
    return config.get('Environment', 'url')
