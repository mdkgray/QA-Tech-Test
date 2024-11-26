import os
import logging
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class SeleniumDriver:
  SCREENSHOT_DIR = "../screenshots/"
  DEFAULT_TIMEOUT = 10

  def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
    self.driver = driver
    self.timeout = timeout
    self.log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)

  def generateTimestamp(self) -> str:
    return datetime.now().strftime("%d%m%Y%H%M%S")

  def screenShot(self):
    fileName = f"Screenshot_{self.generateTimestamp()}.png"
    destinationFile = os.path.join(os.path.dirname(__file__), self.SCREENSHOT_DIR, fileName)
    try:
      os.makedirs(os.path.dirname(destinationFile), exist_ok=True)
      self.driver.save_screenshot(destinationFile)
      self.log.info(f"Screenshot saved at: {destinationFile}")
    except Exception as e:
      self.log.error(f"Failed to save screenshot: {str(e)}")

  def getByType(self, locatorType: str):
    locatorType = locatorType.lower()
    return {
      "id": By.ID,
      "name": By.NAME,
      "xpath": By.XPATH,
      "css": By.CSS_SELECTOR,
      "class": By.CLASS_NAME,
      "link": By.LINK_TEXT,
    }.get(locatorType, None)

  def getElement(self, locator: str, locatorType: str = "id") -> WebElement:
    try:
      byType = self.getByType(locatorType)
      return self.driver.find_element(byType, locator)
    except Exception as e:
      self.log.error(f"Failed to find element with locator: {locator}, type: {locatorType}, error: {str(e)}")
    return None
