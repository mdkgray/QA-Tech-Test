import logging
import pytest
from pages.loginPage import LoginPage
from pages.productPage import ProductPage
from pages.cartPage import CartPage
from utils.config_reader import ConfigReader
from utils.product_data import get_product_data

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestCartPage:

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.cart = CartPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()

    # Test to add and remove products from the cart and validate the cart is updated with the correct products
    @pytest.mark.cart
    @pytest.mark.parametrize("products", [get_product_data()])
    def test_add_remove_products_and_verify_cart(self, products):
        logging.info("Starting test: test_add_remove_products_and_verify_cart")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.login(username, password)
        self.pp.assertProductPageTitle()

        for product in products:
            assert self.pp.addProductToCart(product["name"]) == True

        print(f"Cart count: {self.pp.getNumberOfItemsInCart()}")
        assert self.pp.getNumberOfItemsInCart() == len(products)

        product_details = {f"product{i+1}": product for i, product in enumerate(products)}
        self.cart.validateCart(product_details)
        self.cart.clickContinueShoppingButton()

        for product in products:
            assert self.pp.removeProductFromCart(product["name"]) == True

        print(f"Cart count: {self.pp.getNumberOfItemsInCart()}")
        assert self.pp.getNumberOfItemsInCart() == 0
        self.pp.logout()
        logging.info("Finished test: test_add_remove_products_and_verify_cart")