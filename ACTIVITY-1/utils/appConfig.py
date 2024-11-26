import configparser
import os

appConfig = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'testData', 'testData.ini')
appConfig.read(config_path)

# Base methods 
class AppConfig:
  @staticmethod
  def getBaseURL():
    url=appConfig.get('testData', 'baseURL')
    return url
  
  @staticmethod
  def getStandardUser():
    username=appConfig.get('testdata', 'standardUser')
    return username
  
  @staticmethod
  def getLockedUser():
    username=appConfig.get('testdata', 'lockedUser')
    return username 
  
  @staticmethod
  def getPassword():
    password=appConfig.get('testdata', 'password')
    return password 