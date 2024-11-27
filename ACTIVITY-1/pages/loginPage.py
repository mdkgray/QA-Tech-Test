import logging
from base.seleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setting up logging configuration globally
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoginPage(SeleniumDriver):
    _instance = None
    
    # Constants for locators (uppercase to indicate constants)
    LOGIN_PAGE_TITLE_LOCATOR = "//div[@class='login_logo']"
    USERNAME_INPUT_LOCATOR = "//input[@id='user-name']"
    PASSWORD_INPUT_LOCATOR = "//input[@id='password']"
    LOGIN_BUTTON_LOCATOR = "//input[@id='login-button']"
    LOGIN_ERROR_MESSAGE_LOCATOR = "//div[@class='error-message-container error']/h3"

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(LoginPage, cls).__new__(cls)
            cls._instance._initialize(driver)
        return cls._instance

    def _initialize(self, driver):
        self.driver = driver

    def clearAndSendKeys(self, locator, data):
        """Clears a field and sends keys to it."""
        try:
            self.clearField(locator)
            self.sendKeys(data, locator)
            logging.info(f"Sent data to element with locator: {locator}")
        except Exception as e:
            logging.error(f"Error in clearAndSendKeys for locator: {locator}. Error: {e}")
            raise

    def enterUsername(self, username):
        """Clears and enters username."""
        self.clearAndSendKeys(self.USERNAME_INPUT_LOCATOR, username)

    def enterPassword(self, password):
        """Clears and enters password."""
        self.clearAndSendKeys(self.PASSWORD_INPUT_LOCATOR, password)

    def clickLoginButton(self):
        """Clicks the login button."""
        try:
            self.elementClick(self.LOGIN_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on login button")
        except Exception as e:
            logging.error(f"Error clicking login button: {e}")
            raise

    def getLoginErrorMessageText(self):
        """Gets the error message text if login fails."""
        try:
            self.waitForElement(self.LOGIN_ERROR_MESSAGE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self.LOGIN_ERROR_MESSAGE_LOCATOR)
            logging.info("Retrieved login error message")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving login error message: {e}")
            return None

    def getLoginPageTitleText(self):
        """Gets the login page title text."""
        try:
            self.waitForElement(self.LOGIN_PAGE_TITLE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self.LOGIN_PAGE_TITLE_LOCATOR)
            logging.info("Retrieved login page title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving login page title text: {e}")
            return None

    def validateLoginPageTitleText(self):
        """Validates that the login page title text matches expected value."""
        title_text = self.getLoginPageTitleText()
        if title_text:
            logging.info(f"Login Page Header Text: {title_text}")
            assert title_text == "Swag Labs", f"Expected 'Swag Labs', but got '{title_text}'"
        else:
            logging.error("Login page title text could not be retrieved.")
            raise AssertionError("Login page title text is missing.")

    def login(self, username='', password=''):
        """Performs the login action."""
        self.validateLoginPageTitleText()
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()
