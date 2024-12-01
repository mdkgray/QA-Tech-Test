import logging
from base.seleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.loginPage import LoginPage

class ProductPage(SeleniumDriver):
    _instance = None
    
    # Page locators
    _PRODUCT_PAGE_TITLE_LOCATOR = "//div[@class='app_logo']"
    _PRODUCT_MENU_HAMBURGER_LOCATOR = "//button[@id='react-burger-menu-btn']"
    _LOGOUT_BUTTON_LOCATOR = "//a[@id='logout_sidebar_link']"
    _PRODUCT_NAME_LOCATOR = "//div[@data-test='inventory-item-name']"
    _ADD_OR_REMOVE_FROM_CART_BUTTON_LOCATOR = "//div[text()='PRODUCT_NAME']/ancestor::div[@class='inventory_item']//button[contains(@class, 'btn_inventory')]"
    _CART_COUNT_LOCATOR = "//span[@class='shopping_cart_badge']"
    
    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(ProductPage, cls).__new__(cls)
            cls._instance._initialize(driver)
        return cls._instance

    def _initialize(self, driver):
        self.driver = driver
    
    def getProductPageTitleText(self):
        """Returns the product page title text."""
        try:
            self.waitForElement(self._PRODUCT_PAGE_TITLE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._PRODUCT_PAGE_TITLE_LOCATOR)
            logging.info("Retrieved product page title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving product page title text: {e}")
            return None
    
    def assertProductPageTitle(self):
        """Validates the product page title matches the expected value."""
        try:
            product_title_text = self.getProductPageTitleText()
            if product_title_text:
                logging.info(f"Product Page Header Text: {product_title_text}")
                assert product_title_text == "Swag Labs", f"Expected 'Swag Labs', but got '{product_title_text}'"
            else:
                logging.error("Product page title text could not be found.")
                raise AssertionError("Product page title assertion failed")
        except AssertionError as ae:
            logging.error(f"Assertion error validating product page title: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating product page title: {e}")
            raise
        
    def clickHamburgerMenu(self):
        """Clicks the hamburger menu."""
        try:
            self.clickElement(self._PRODUCT_MENU_HAMBURGER_LOCATOR, locatorType="xpath")
            logging.info("Clicked on hamburger menu")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking hamburger menu: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking hamburger menu: {e}")
            raise
        
    def clickToLogout(self):
        """Clicks the logout button."""
        try:
            self.clickElement(self._LOGOUT_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on logout button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking logout button: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking logout button: {e}")
            raise
        
    def logout(self):
        """Logs out of the application."""
        try:
            self.clickHamburgerMenu()
            self.clickToLogout()
            self.loginObject = LoginPage(self.driver)
            self.loginHeaderText = self.loginObject.getLoginPageTitleText()
            logging.info(f"Successfully logged out. Login Page Header Text: {self.loginHeaderText}")
        except Exception as e:
            logging.error(f"Error during logout: {e}")
            raise
        
    def getProductName(self):
        """Returns the product name to append to list of items."""
        try:
            productListing = self.driver.find_elements(By.XPATH, self._PRODUCT_NAME_LOCATOR)
            productNames = []
            for element in productListing:
                productNames.append(element.text)
            return productNames
        except Exception as e:
            logging.error(f"Error retrieving product names: {e}")
            return []
    
    def isProductListed(self, productName):
        """Checks if the product is listed."""
        try:
            productListing = self.getProductName()
            return any(productName == product for product in productListing)
        except Exception as e:
            logging.error(f"Error checking if product is listed: {e}")
            return False
        
    def addProductToCart(self, product):
        """Adds a product to the cart."""
        try:
            locator = self._ADD_OR_REMOVE_FROM_CART_BUTTON_LOCATOR.replace("PRODUCT_NAME", product)
            self.scrollToElement(locator)
            element = self.driver.find_element(By.XPATH, locator)
            if element.text == "Add to cart":
                self.clickElement(locator, locatorType="xpath")
                logging.info(f"Added {product} to cart")
                return True
            else:
                logging.info(f"Failed to add {product} to cart")
                return False
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error adding {product} to cart: {e}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error adding {product} to cart: {e}")
            return False

    def removeProductFromCart(self, product):
        """Removes a product from the cart."""
        try:
            locator = self._ADD_OR_REMOVE_FROM_CART_BUTTON_LOCATOR.replace("PRODUCT_NAME", product)
            self.scrollToElement(locator)
            element = self.driver.find_element(By.XPATH, locator)
            if element.text == "Remove":
                self.clickElement(locator, locatorType="xpath")
                logging.info(f"Removed {product} from cart")
                return True
            else:
                logging.info(f"Failed to remove {product} from cart")
                return False
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error removing {product} from cart: {e}")
            return False
        except Exception as e:
            logging.error(f"Unexpected error removing {product} from cart: {e}")
            return False
        
    def getNumberOfItemsInCart(self):
        """Returns the number of items in the cart."""
        try:
            self.waitForElement(self._CART_COUNT_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._CART_COUNT_LOCATOR)
            logging.info("Retrieved cart count")
            return int(element.text) if element.text else 0
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving cart count: {e}")
            return 0