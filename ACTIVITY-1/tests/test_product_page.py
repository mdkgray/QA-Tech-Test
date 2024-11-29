import logging
import pytest
import unittest
from selenium import webdriver
from pages.productPage import ProductPage
from pages.loginPage import LoginPage
from utils.config_reader import ConfigReader

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProductPageTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()

    # Test to validate there are products listed on the product page
    @pytest.mark.productPage
    def test_get_all_products(self):
        logging.info("Starting test: test_get_all_products")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        productNames = self.pp.getProductName()
        print('Products:', productNames)
        assert len(productNames) > 0
        self.pp.logout()
        logging.info("Finished test: test_get_all_products")
        
    # Test to validate listed products are valid products
    @pytest.mark.productPage
    def test_is_product_valid(self):
        logging.info("Starting test: test_is_product_valid")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.isProductListed("Sauce Labs Backpack") == True
        self.pp.logout()
        logging.info("Finished test: test_is_product_valid")
        
    # Test to ensure invalid products are not listed     
    @pytest.mark.productPage
    def test_is_product_invalid(self):
        logging.info("Starting test: test_is_product_invalid")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.isProductListed("Light Bike Onesie") == False
        self.pp.logout()
        logging.info("Finished test: test_is_product_invalid")
        
    # Test to add a product to the cart 
    @pytest.mark.productPage
    def test_add_product_to_cart(self):
        logging.info("Starting test: test_add_product_to_cart")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.addProductToCart("Sauce Labs Backpack") == True
        assert self.pp.getNumberOfItemsInCart() == 1
        self.pp.logout()
        logging.info("Finished test: test_add_product_to_cart")
    
    # Test to remove a product from the cart
    @pytest.mark.productPage
    def test_remove_product_from_cart(self):
        logging.info("Starting test: test_remove_product_from_cart")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.addProductToCart("Sauce Labs Backpack") == True
        assert self.pp.getNumberOfItemsInCart() == 1
        assert self.pp.removeProductFromCart("Sauce Labs Backpack") == True
        assert self.pp.getNumberOfItemsInCart() == 0
        self.pp.logout()
        logging.info("Finished test: test_remove_product_from_cart")