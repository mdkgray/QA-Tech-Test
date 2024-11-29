import logging
import pytest
import unittest
from selenium import webdriver
from pages.productPage import ProductPage
from pages.loginPage import LoginPage
from utils.config_reader import ConfigReader
from utils.product_data import get_product_data, get_invalid_product_data

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestProductPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()

    # Test to validate there are products listed on the product page
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
    @pytest.mark.parametrize("product", get_product_data())
    def test_is_product_valid(self, product):
        logging.info(f"Starting test: test_is_product_valid for {product['name']}")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.isProductListed(product["name"]) == True
        self.pp.logout()
        logging.info(f"Finished test: test_is_product_valid for {product['name']}")
        
    # Test to ensure invalid products are not listed     
    @pytest.mark.productPage
    @pytest.mark.parametrize("product", get_invalid_product_data())
    def test_is_product_invalid(self, product):
        logging.info(f"Starting test: test_is_product_invalid for {product['name']}")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.isProductListed(product["name"]) == False
        self.pp.logout()
        logging.info(f"Finished test: test_is_product_invalid for {product['name']}")

    # Test to add a product to the cart
    @pytest.mark.productPage
    @pytest.mark.parametrize("product", get_product_data())
    def test_add_product_to_cart(self, product):
        logging.info(f"Starting test: test_add_product_to_cart for {product['name']}")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.addProductToCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 1
        # Remove the product from the cart after the assertion
        assert self.pp.removeProductFromCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 0
        self.pp.logout()
        logging.info(f"Finished test: test_add_product_to_cart for {product['name']}")

    # Test to remove a product from the cart
    @pytest.mark.productPage
    @pytest.mark.parametrize("product", get_product_data())
    def test_remove_product_from_cart(self, product):
        logging.info(f"Starting test: test_remove_product_from_cart for {product['name']}")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.validateProductPageTitle()
        assert self.pp.addProductToCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 1
        assert self.pp.removeProductFromCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 0
        self.pp.logout()
        logging.info(f"Finished test: test_remove_product_from_cart for {product['name']}")