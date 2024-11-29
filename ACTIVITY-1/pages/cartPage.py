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
            self.waitForElement(self._CART_BUTTON_LOCATOR, locatorType="xpath")
            self.clickElement(self._CART_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on cart icon")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking cart icon: {e}")
            return False
    
    def getCartTitleText(self):
        """Returns the cart title text."""
        try:
            self.waitForElement(self._CART_TITLE_TEXT_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._CART_TITLE_TEXT_LOCATOR)
            logging.info("Retrieved cart title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving cart title text: {e}")
            return None
                
    def clickContinueShoppingButton(self):
        """Clicks the continue shopping button."""
        try:
            self.waitForElement(self._CART_CONTINUE_SHOPPING_BUTTON_LOCATOR, locatorType="xpath")
            self.clickElement(self._CART_CONTINUE_SHOPPING_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on continue shopping button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking continue shopping button: {e}")
            return False
        
        
    def clickCheckoutButton(self):
        """Clicks the checkout button."""
        try:
            self.waitForElement(self._CART_CHECKOUT_BUTTON_LOCATOR, locatorType="xpath")
            self.clickElement(self._CART_CHECKOUT_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on checkout button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking checkout button: {e}")
            return False
        
    def validateCartTitle(self):
        """Validates the cart title matches the expected value."""
        try:
            cart_title_text = self.getCartTitleText()
            if cart_title_text:
                logging.info(f"Cart Title Text: {cart_title_text}")
                assert cart_title_text == "Your Cart", f"Expected 'Your Cart', but got '{cart_title_text}'"
            else:
                logging.error("Cart title text could not be found.")
                raise AssertionError("Cart title assertion failed")
        except AssertionError as ae:
            logging.error(f"Assertion error validating cart title: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating cart title: {e}")
            raise
        
    def validateItemsInCart(self, productDetails):
        """Validates the items in the cart match the expected values."""
        try:
            products_added = list(productDetails.keys())
            for product in products_added:
                productName = productDetails[product]["name"]
                productPrice = productDetails[product]["price"]
                productQuantity = productDetails[product]["quantity"]
                logging.info(f"Product Name: {productName}, Price: {productPrice}, Quantity: {productQuantity}")
                
                product_price_locator = self._CART_ITEM_PRICE_LOCATOR.replace("ITEM_NAME", productName)
                product_quantity_locator = self._CART_ITEM_QUANTITY_LOCATOR.replace("ITEM_NAME", productName)
                
                self.waitForElement(product_price_locator, locatorType="xpath")
                element = self.driver.find_element(By.XPATH, product_price_locator)
                productPriceInCart = element.text
                logging.info(f"Product Price in Cart: {productPriceInCart}")
                
                self.waitForElement(product_quantity_locator, locatorType="xpath")
                element = self.driver.find_element(By.XPATH, product_quantity_locator)
                productQuantityInCart = element.text
                logging.info(f"Product Quantity in Cart: {productQuantityInCart}")
                
                assert productPriceInCart == productPrice, f"Expected price: {productPrice}, but got: {productPriceInCart}"
                assert productQuantityInCart == productQuantity, f"Expected quantity: {productQuantity}, but got: {productQuantityInCart}"
            
            self.screenShot()
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error validating items in cart: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error validating items in cart: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating items in cart: {e}")
            raise
            
    def validateCart(self, products):
        """Validates the cart navigation and accuracy."""
        try:
            self.clickCartIcon()
            logging.info("Clicked on cart icon")
            self.validateCartTitle()
            self.validateItemsInCart(products)
            self.screenShot()
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error validating cart accuracy: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error during cart validation: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during cart validation: {e}")
            raise