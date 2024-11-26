from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from utils.appConfig import AppConfig

class WebDriver():
  def __init__(self, browser):
    """
    Initialize the WebDriver class with the desired browser type.
    """
    self.browser = browser

  def useWebDriverInstance(self):
    """
    Create and return a WebDriver instance based on the specified browser.
    """
    baseURL = AppConfig.getBaseURL()
    if self.browser == 'chrome':
        # Use webdriver-manager to manage the ChromeDriver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif self.browser == 'firefox':
        # Use webdriver-manager to manage the GeckoDriver
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    elif self.browser == 'iexplorer':
        # Use webdriver-manager to manage the IEDriver
        driver = webdriver.Ie(
            service=IEService(IEDriverManager().install())
        )
    else:
        raise ValueError(f"Unsupported browser: {self.browser}")

    # Common setup for all browsers
    driver.implicitly_wait(3)  # Set implicit wait
    driver.maximize_window()   # Maximize the browser window
    driver.get(baseURL)        # Navigate to the base URL
    return driver
