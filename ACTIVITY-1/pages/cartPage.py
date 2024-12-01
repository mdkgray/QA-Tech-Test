import logging
from selenium import webdriver
from base.seleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CartPage(SeleniumDriver):
    _instance = None
    
    # Page locators
    _CART_BUTTON_LOCATOR = "//div[@id='shopping_cart_container']/a"
    _CART_TITLE_TEXT_LOCATOR = "//span[@class='title']"
    _CART_CONTINUE_SHOPPING_BUTTON_LOCATOR = "//button[@id='continue-shopping']"
    _CART_CHECKOUT_BUTTON_LOCATOR = "//button[@id='checkout']"
    _CART_ITEM_PRICE_LOCATOR = "//div[text()='ITEM_NAME']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_price']"
    _CART_ITEM_QUANTITY_LOCATOR = "//div[text()='ITEM_NAME']/ancestor::div[@class='cart_item']/div[@class='cart_quantity']"

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super(CartPage, cls).__new__(cls)
            cls._instance._initialize(driver)
        return cls._instance
    
    def _initialize(self, driver):
        self.driver = driver
        
    def clickCartIcon(self): 
        """Clicks the cart icon."""
        try:
            self.waitForElement(self._CART_BUTTON_LOCATOR, locatorType="xpath", timeout=5)
            self.clickElement(self._CART_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on cart icon")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking cart icon: {e}")
            return False
    
    def getCartTitleText(self):
        """Returns the cart title text."""
        try:
            self.waitForElement(self._CART_TITLE_TEXT_LOCATOR, locatorType="xpath", timeout=5)
            element = self.driver.find_element(By.XPATH, self._CART_TITLE_TEXT_LOCATOR)
            logging.info("Retrieved cart title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving cart title text: {e}")
            return None

    def assertCartTitle(self):
        """Asserts that the cart page title matches the expected value."""
        try:
            cart_title_text = self.getCartTitleText()
            logging.info(f"Cart Page Title Text: {cart_title_text}")
            assert cart_title_text == "Your Cart", f"Expected 'Your Cart', but got '{cart_title_text}'"
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving cart page title text: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error validating cart page title: {ae}")
            raise

    def validateCart(self, products):
        """Validates the cart navigation and accuracy."""
        try:
            self.clickCartIcon()
            logging.info("Clicked on cart icon")
            self.assertCartTitle()
            self.assertCartItems(products)
        except AssertionError as ae:
            logging.error(f"Assertion error during cart validation: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during cart validation: {e}")
            raise

    def assertCartItems(self, products):
        """Asserts that the products in the cart match the expected products."""
        try:
            cart_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            cart_item_names = [item.text for item in cart_items]
            logging.info(f"Cart items: {cart_item_names}")

            expected_product_names = [product["name"] for product in products.values()]
            logging.info(f"Expected products: {expected_product_names}")

            assert sorted(cart_item_names) == sorted(expected_product_names), \
                f"Expected products {expected_product_names}, but got {cart_item_names}"
            logging.info("Cart items match the expected products")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error asserting cart items: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error during cart items validation: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during cart items validation: {e}")
            raise

    def clickContinueShoppingButton(self):
        """Clicks the continue shopping button."""
        try:
            self.waitForElement(self._CART_CONTINUE_SHOPPING_BUTTON_LOCATOR, locatorType="xpath", timeout=5)
            self.clickElement(self._CART_CONTINUE_SHOPPING_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on continue shopping button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking continue shopping button: {e}")
            return False

    def clickCheckoutButton(self):
        """Clicks the checkout button."""
        try:
            self.waitForElement(self._CART_CHECKOUT_BUTTON_LOCATOR, locatorType="xpath", timeout=5)
            self.clickElement(self._CART_CHECKOUT_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on checkout button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking checkout button: {e}")
            return False