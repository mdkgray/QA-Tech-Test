import logging
from selenium import webdriver
from base.seleniumDriver import SeleniumDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CheckoutPage(SeleniumDriver):
    instance = None
    
    # Page locators
    _CHECKOUT_STAGE_TITLE_LOCATOR = "//span[@class='title']"
    # Checkout: Your Information 
    _FIRST_NAME_INPUT_LOCATOR = "//input[@id='first-name']"
    _LAST_NAME_INPUT_LOCATOR = "//input[@id='last-name']"
    _POSTAL_CODE_INPUT_LOCATOR = "//input[@id='postal-code']"
    _CANCEL_BUTTON_LOCATOR = "//button[@id='cancel']"
    _CONTINUE_BUTTON_LOCATOR = "//input[@id='continue']"
    # Checkout: Overview
    _INVENTORY_ITEM_NAME_LOCATOR = "//div[@class='inventory_item_name']"
    _PAYMENT_INFO_VALUE_LOCATOR = "//div[@data-test='payment-info-value']"
    _SHIPPING_INFO_VALUE_LOCATOR = "//div[@data-test='shipping-info-value']"
    _TOTAL_AMOUNT_LOCATOR = "//div[@data-test='total-label']"
    _FINISH_BUTTON_LOCATOR = "//button[@id='finish']"
    # Checkout: Complete
    _SUCCESSFUL_ORDER_TEXT_LOCATOR = "//h2[@class='complete-header']"
    _BACK_TO_HOME_BUTTON_LOCATOR = "//button[@id='back-to-products']"

    def __new__(cls, driver):
        if cls.instance is None:
            cls.instance = super(CheckoutPage, cls).__new__(cls)
            cls.instance._initialize(driver)
        return cls.instance

    def _initialize(self, driver):
        self.driver = driver
    
    def getCheckoutStageTitleText(self):
        """Returns the checkout stage title text."""
        try:
            self.waitForElement(self._CHECKOUT_STAGE_TITLE_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._CHECKOUT_STAGE_TITLE_LOCATOR)
            logging.info("Retrieved checkout stage title text")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving checkout stage title text: {e}")
            return None
    
    def assertCheckoutInformationPageTitle(self):
        """Validates the checkout information page title matches the expected value."""
        try:
            checkout_info_title_text = self.getCheckoutStageTitleText()
            if checkout_info_title_text:
                logging.info(f"Checkout Information Page Header Text: {checkout_info_title_text}")
                assert checkout_info_title_text == "Checkout: Your Information", f"Expected 'Checkout: Your Information', but got '{checkout_info_title_text}'"
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving checkout information page title text: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error validating checkout information page title: {ae}")
            raise

    def assertCheckoutOverviewPageTitle(self):
        """Validates the checkout overview page title matches the expected value."""
        try:
            checkout_overview_title_text = self.getCheckoutStageTitleText()
            if checkout_overview_title_text:
                logging.info(f"Checkout Overview Page Header Text: {checkout_overview_title_text}")
                assert checkout_overview_title_text == "Checkout: Overview", f"Expected 'Checkout: Overview', but got '{checkout_overview_title_text}'"
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving checkout overview page title text: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error validating checkout overview page title: {ae}")
            raise
        
    def assertCheckoutCompletePageTitle(self):
        """Validates the checkout complete page title matches the expected value."""
        try:
            checkout_complete_title_text = self.getCheckoutStageTitleText()
            if checkout_complete_title_text:
                logging.info(f"Checkout Complete Page Header Text: {checkout_complete_title_text}")
                assert checkout_complete_title_text == "Checkout: Complete!", f"Expected 'Checkout: Complete!', but got '{checkout_complete_title_text}'"
            else:
                logging.error("Checkout complete page title text could not be found.")
                raise AssertionError("Checkout complete page title assertion failed")
        except AssertionError as ae:
            logging.error(f"Assertion error validating checkout complete page title: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating checkout complete page title: {e}")
            raise
    
    def enterCheckoutInformation(self, first_name, last_name, postal_code):
        """Fills in the checkout information."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        
    def clickContinueButton(self):
        """Clicks the continue button."""
        self.driver.find_element(By.ID, "continue").click()
    
    def clickCancelButton(self):
        """Clicks the cancel button."""
        try:
            self.clickElement(self._CANCEL_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on cancel button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking cancel button: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking cancel button: {e}")
            raise
        
    def clickFinishButton(self):
        """Clicks the finish button."""
        try:
            self.clickElement(self._FINISH_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on finish button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking finish button: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking finish button: {e}")
            raise
        
    def clickBackToHomeButton(self):
        """Clicks the back to home button."""
        try:
            self.clickElement(self._BACK_TO_HOME_BUTTON_LOCATOR, locatorType="xpath")
            logging.info("Clicked on back to home button")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error clicking back to home button: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error clicking back to home button: {e}")
            raise
        
    def getOrderSuccessMessage(self):
        """Returns the order success message."""
        try:
            self.waitForElement(self._SUCCESSFUL_ORDER_TEXT_LOCATOR, locatorType="xpath")
            element = self.driver.find_element(By.XPATH, self._SUCCESSFUL_ORDER_TEXT_LOCATOR)
            logging.info("Retrieved order success message")
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error retrieving order success message: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error retrieving order success message: {e}")
            return None
    
    def assertOrderSuccessMessage(self):
        """Validates the order success message matches the expected value."""
        try:
            order_success_message = self.getOrderSuccessMessage()
            if order_success_message:
                logging.info(f"Order Success Message: {order_success_message}")
                assert order_success_message == "Thank you for your order!", f"Expected 'Thank you for your order!', but got '{order_success_message}'"
            else:
                logging.error("Order success message could not be found.")
                raise AssertionError("Order success message assertion failed")
        except AssertionError as ae:
            logging.error(f"Assertion error validating order success message: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error validating order success message: {e}")
            raise
    
    def assertCheckoutItems(self, expected_products):
        """Asserts that the products in the checkout overview are the expected products."""
        try:
            self.waitForElement(self._INVENTORY_ITEM_NAME_LOCATOR, locatorType="xpath")
            elements = self.driver.find_elements(By.XPATH, self._INVENTORY_ITEM_NAME_LOCATOR)
            product_names_in_checkout = [element.text for element in elements]
            logging.info(f"Products in checkout: {product_names_in_checkout}")
            
            expected_product_names = [product["name"] for product in expected_products]
            logging.info(f"Expected products: {expected_product_names}")
            
            assert sorted(product_names_in_checkout) == sorted(expected_product_names), \
                f"Expected products {expected_product_names}, but got {product_names_in_checkout}"
            logging.info("Checkout items match the expected products")
        except (TimeoutException, NoSuchElementException) as e:
            logging.error(f"Error asserting checkout items: {e}")
            raise
        except AssertionError as ae:
            logging.error(f"Assertion error during checkout items validation: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during checkout items validation: {e}")
            raise
        
    def completeCheckout(self, first_name, last_name, postal_code, expected_products):
        """Completes the checkout process."""
        try:
            self.assertCheckoutInformationPageTitle()
            self.enterCheckoutInformation(first_name, last_name, postal_code)
            self.clickContinueButton()
            self.assertCheckoutOverviewPageTitle()
            self.assertCheckoutItems(expected_products)
            self.screenShot()
            self.clickFinishButton()
            self.assertCheckoutCompletePageTitle()
            self.clickBackToHomeButton()
            logging.info("Completed checkout process")
        except AssertionError as ae:
            logging.error(f"Assertion error during checkout process: {ae}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error during checkout process: {e}")
            raise
