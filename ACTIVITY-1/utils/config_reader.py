import configparser
import os

configReader = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
configReader.read(config_path)

class ConfigReader:
  @staticmethod
  def getBaseURL():
    url=configReader.get('testData', 'baseURL')
    return url
  
  @staticmethod
  def getStandardUser():
    username=configReader.get('testdata', 'standardUser')
    return username
  
  @staticmethod
  def getLockedUser():
    username=configReader.get('testdata', 'lockedUser')
    return username 
  
  @staticmethod
  def getPassword():
    password=configReader.get('testdata', 'password')
    return password 