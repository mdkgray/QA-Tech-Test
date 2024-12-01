import configparser
import os

class ConfigReader:
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
    config.read(config_path)

    @staticmethod
    def getBaseURL():
        return ConfigReader.config.get('testdata', 'baseURL')

    @staticmethod
    def getStandardUser():
        return ConfigReader.config.get('testdata', 'standardUser')

    @staticmethod
    def getLockedUser():
        return ConfigReader.config.get('testdata', 'lockedUser')

    @staticmethod
    def getPassword():
        return ConfigReader.config.get('testdata', 'password')