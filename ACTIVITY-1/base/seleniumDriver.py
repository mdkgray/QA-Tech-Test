import os
import logging
from traceback import print_stack
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
    StaleElementReferenceException,
    TimeoutException,
)

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

  def getTitle(self):
    return self.driver.title

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

  def clickElement(self, locator=None, locatorType="xpath", element=None):
    """
    Click on an element in the browser.    
    Args:
      locator (str): The locator string to identify the element.
      locatorType (str): The type of locator (e.g., "id", "xpath", "css").
      element (WebElement, optional): The WebElement to click. Defaults to None.
    
    Returns:
      bool: True if the click is successful, False otherwise.
    """
    try:
      if locator:
          element = self.getElement(locator, locatorType)
      
      if element:
          element.click()
          logging.info(f"Clicked on element with locator: {locator}, locatorType: {locatorType}")
          return True
      else:
          logging.error(f"Element not found for locator: {locator}, locatorType: {locatorType}")
          return False

    except Exception as e:
      logging.error(f"Cannot click on the element with locator: {locator}, locatorType: {locatorType}. Error: {str(e)}")
      print_stack()
      return False

  def sendKeys(self, data, locator=None, locatorType="xpath", element=None):
    """
    Sends keys to a web element.
    
    Args:
      data (str): The text to send to the web element.
      locator (str, optional): The locator string to identify the element.
      locatorType (str): The type of locator (e.g., "id", "xpath", "css"). Defaults to "xpath".
      element (WebElement, optional): The WebElement to send keys to. Defaults to None.
    
    Returns:
      bool: True if the keys are sent successfully, False otherwise.
    """
    try:
      if locator:
        element = self.getElement(locator, locatorType)
      
      if element:
        element.send_keys(data)
        logging.info(f"Sent data '{data}' to element with locator: {locator}, locatorType: {locatorType}")
        return True
      else:
        logging.error(f"Element not found for locator: {locator}, locatorType: {locatorType}")
        return False

    except Exception as e:
      logging.error(f"Cannot send data '{data}' to the element with locator: {locator}, locatorType: {locatorType}. Error: {str(e)}")
      print_stack()
      return False
    
  def clearField(self, locator=None, locatorType="xpath", element=None):
    """
    Clears the text of a web element field.
    
    Args:
      locator (str, optional): The locator string to identify the element.
      locatorType (str): The type of locator (e.g., "id", "xpath", "css"). Defaults to "xpath".
      element (WebElement, optional): The WebElement to clear. Defaults to None.
    
    Returns:
      bool: True if the field is cleared successfully, False otherwise.
    """
    try:
      if locator:
        element = self.getElement(locator, locatorType)
      
      if element:
        element.clear()
        logging.info(f"Cleared field with locator: {locator}, locatorType: {locatorType}")
        return True
      else:
        logging.error(f"Element not found for locator: {locator}, locatorType: {locatorType}")
        return False

    except Exception as e:
      logging.error(f"Cannot clear field with locator: {locator}, locatorType: {locatorType}. Error: {str(e)}")
      print_stack()
      return False
    
  def waitForElement(self, locator, locatorType="xpath", timeout=10, pollFrequency=0.5, condition="clickable"):
    """
    Wait for an element to meet a specific condition (e.g., clickable, visible).
    
    Args:
      locator (str): The locator string to identify the element.
      locatorType (str): The type of locator (e.g., "id", "xpath", "css"). Defaults to "xpath".
      timeout (int): Maximum time to wait for the condition (in seconds). Defaults to 10.
      pollFrequency (float): Frequency to poll the DOM for the element (in seconds). Defaults to 0.5.
      condition (str): The condition to wait for ("clickable", "visible", etc.). Defaults to "clickable".
    
    Returns:
      WebElement: The element if found within the timeout, None otherwise.
    """
    try:
      byType = self.getByType(locatorType)
      logging.info(f"Waiting for up to {timeout} seconds for element to be {condition}. Locator: {locator}, LocatorType: {locatorType}")

      # Map of supported conditions
      conditions_map = {
        "clickable": EC.element_to_be_clickable((byType, locator)),
        "visible": EC.visibility_of_element_located((byType, locator)),
        "present": EC.presence_of_element_located((byType, locator)),
      }

      if condition not in conditions_map:
        logging.error(f"Unsupported condition: {condition}")
        return None

      wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
        ignored_exceptions=[
          NoSuchElementException,
          ElementNotVisibleException,
          ElementNotSelectableException,
          StaleElementReferenceException,
      ])

      element = wait.until(conditions_map[condition])
      logging.info(f"Element found and met condition: {condition}")
      return element

    except Exception as e:
      logging.error(f"Element not found or did not meet condition: {condition}. Locator: {locator}, LocatorType: {locatorType}. Error: {str(e)}")
      print_stack()
      return None
    
  def scrollToElement(self, locator, locatorType="xpath", timeout=10):
    """
    Scroll to an element on the page utilising JavaScript's `scrollIntoView()` method.

    Args:
      locator (str): The locator string to identify the element.
      locatorType (str): The type of locator (e.g., "id", "xpath", "css"). Defaults to "xpath".
      timeout (int): Maximum time to wait for the element to be present (in seconds). Defaults to 10.

    Returns:
      bool: True if scrolling is successful, False otherwise.
    """
    try:
      # Convert locator type to Selenium's By object
      byType = self.getByType(locatorType)

      logging.info(f"Waiting for element to be present: Locator: {locator}, LocatorType: {locatorType}")
      wait = WebDriverWait(self.driver, timeout)
      element_to_scroll_to = wait.until(EC.presence_of_element_located((byType, locator)))

      # Scroll to the element using JavaScript
      self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element_to_scroll_to)
      logging.info("Successfully scrolled to the element.")
      return True

    except TimeoutException:
      logging.error(f"Timeout: Element not found. Locator: {locator}, LocatorType: {locatorType}")
    except Exception as e:
      logging.error(f"An error occurred while scrolling to the element. Locator: {locator}, LocatorType: {locatorType}. Error: {str(e)}")

    return False
  