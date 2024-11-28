import pytest  
import unittest

from utils.config_reader import ConfigReader
from pages.loginPage import LoginPage
from pages.productPage import ProductPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()
    
    # Test for valid login flow using the standard user account    
    @pytest.mark.login
    def test_valid_login(self):
        username = self.lp.enterUsername(self.cr.getStandardUser())
        password = self.lp.enterPassword(self.cr.getPassword())
        self.lp.login(username, password)
        self.lp.clickLoginButton()
        # self.pp.assertProductPageTitle()
        self.lp.logout() # TBD on product page
        
    # Test for invalid login flow using the locked out user account    
    @pytest.mark.login
    def test_invalid_login(self):
        username = self.lp.enterUsername(self.cr.getLockedOutUser())
        password = self.lp.enterPassword(self.cr.getPassword())
        self.lp.login(username, password)
        errorMessage = self.lp.getLoginErrorMessageText()
        expectedErrorMessage = "Epic sadface: Sorry, this user has been locked out."
        assert errorMessage == expectedErrorMessage