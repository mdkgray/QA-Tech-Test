import logging
from base.seleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Setting up logging configuration globally at the application entry point
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoginPage(SeleniumDriver):
    _instance = None
    
    # Page locators
    _LOGIN_PAGE_TITLE_LOCATOR = "//div[@class='login_logo']"
    _USERNAME_INPUT_LOCATOR = "//input[@id='user-name']"
    _PASSWORD_INPUT_LOCATOR = "//input[@id='password']"
    _LOGIN_BUTTON_LOCATOR = "//input[@id='login-button']"
    _LOGIN_ERROR_MESSAGE_LOCATOR = "//div[@class='error-message-container error']/h3"

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
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error in clearAndSendKeys for locator: {locator}. Error: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error in clearAndSendKeys for locator: {locator}. Error: {e}")
            raise

    def enterUsername(self, username):
        """Clears and enters username."""
        try:
            self.clearAndSendKeys(self._USERNAME_INPUT_LOCATOR, username)
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error entering username: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error entering username: {e}")
            raise

    def enterPassword(self, password):
        """Clears and enters password."""
        try:
            self.clearAndSendKeys(self._PASSWORD_INPUT_LOCATOR, password)
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error entering password: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error entering password: {e}")
            raise

    def clickLoginButton(self):
        """Clicks the login button."""
        try:
            self.clickElement(self._LOGIN_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on login button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking login button: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking login button: {e}")
            raise

    def getLoginErrorMessageText(self):
        """Gets the error message text if login fails."""
        try:
            self.waitForElement(self._LOGIN_ERROR_MESSAGE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._LOGIN_ERROR_MESSAGE_LOCATOR)
            logging.info("Retrieved login error message")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving login error message: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error retrieving login error message: {e}")
            return None

    def getLoginPageTitleText(self):
        """Gets the login page title text."""
        try:
            self.waitForElement(self._LOGIN_PAGE_TITLE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._LOGIN_PAGE_TITLE_LOCATOR)
            logging.info("Retrieved login page title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving login page title text: {e}")
            return None

    def assertLoginPageTitleText(self):
        """Validates that the login page title text matches the expected value."""
        try:
            login_title_text = self.getLoginPageTitleText()
            if login_title_text:
                logging.info(f"Login Page Header Text: {login_title_text}")
                assert login_title_text == "Swag Labs", f"Expected 'Swag Labs', but got '{login_title_text}'"
            else:
                logging.error("Login page title text could not be found.")
                raise AssertionError("Login page title assertion failed")
        except AssertionError as ae:
            logging.error(f"Assertion error validating login page title text: {ae}")
            raise
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving login page title text: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating login page title text: {e}")
            raise

    def login(self, username, password):
        """Performs the login action."""
        try:
            self.assertLoginPageTitleText()
            self.enterUsername(username)
            self.enterPassword(password)
            self.clickLoginButton()
            logging.info("Logged in with username: {}".format(username))
        except Exception as e:
            logging.error(f"Error during login: {e}")
            raise
