import pytest
import logging
from pages.productPage import ProductPage
from pages.loginPage import LoginPage
from utils.config_reader import ConfigReader
from utils.product_data import get_product_data, get_invalid_product_data

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestProductPage:
    
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()

    # Test to validate products are shown on the product page
    @pytest.mark.productPage
    def test_get_all_products(self):
        logging.info("Starting test: test_get_all_products")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.assertProductPageTitle()
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
        self.pp.assertProductPageTitle()
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
        self.pp.assertProductPageTitle()
        assert self.pp.isProductListed(product["name"]) == False
        self.pp.logout()
        logging.info(f"Finished test: test_is_product_invalid for {product['name']}")

    # Test to add a product to the cart
    @pytest.mark.productPage
    def test_add_product_to_cart(self):
        logging.info("Starting test: test_add_product_to_cart")
        product = get_product_data()[0]  # Get the first product from the data
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.assertProductPageTitle()
        assert self.pp.addProductToCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 1
        # Remove the product from the cart after the assertion
        assert self.pp.removeProductFromCart(product["name"]) == True
        cart_count = self.pp.getNumberOfItemsInCart()
        logging.info(f"Cart count after removal: {cart_count}")
        assert cart_count == 0
        self.pp.logout()
        logging.info("Finished test: test_add_product_to_cart")

    # Test to remove a product from the cart
    @pytest.mark.productPage
    def test_remove_product_from_cart(self):
        logging.info("Starting test: test_remove_product_from_cart")
        product = get_product_data()[0]  # Get the first product from the data
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.assertProductPageTitle()
        assert self.pp.addProductToCart(product["name"]) == True
        assert self.pp.getNumberOfItemsInCart() == 1
        assert self.pp.removeProductFromCart(product["name"]) == True
        cart_count = self.pp.getNumberOfItemsInCart()
        logging.info(f"Cart count after removal: {cart_count}")
        assert cart_count == 0
        self.pp.logout()
        logging.info("Finished test: test_remove_product_from_cart")