import logging
import pytest
from pages.checkoutPage import CheckoutPage
from pages.loginPage import LoginPage
from pages.productPage import ProductPage
from pages.cartPage import CartPage
from utils.config_reader import ConfigReader
from utils.product_data import get_product_data

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestCheckoutPage:

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.cp = CheckoutPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cart = CartPage(self.driver)
        self.cr = ConfigReader()

    # Test to add items to cart and then proceed to checkout
    @pytest.mark.checkout
    @pytest.mark.parametrize("products", [get_product_data()])
    def test_checkout_items(self, products):
        logging.info("Starting test: test_checkout_items")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.assertProductPageTitle()

        for product in products:
            assert self.pp.addProductToCart(product["name"]) == True

        self.cart.clickCartIcon()
        self.cart.clickCheckoutButton()
        self.cp.completeCheckout("John", "Doe", "2000", products)
        logging.info("Finished test: test_checkout_items")