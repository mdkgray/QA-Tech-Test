import pytest  
import unittest
import logging

from utils.config_reader import ConfigReader
from pages.loginPage import LoginPage
from pages.productPage import ProductPage

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.lp = LoginPage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cr = ConfigReader()
    
    # Test for valid login flow using the standard user account    
    @pytest.mark.login
    def test_valid_login(self):
        logging.info("Starting test: test_valid_login")
        username = self.cr.getStandardUser()
        password = self.cr.getPassword()
        self.lp.enterUsername(username)
        self.lp.enterPassword(password)
        self.lp.clickLoginButton()
        self.pp.assertProductPageTitle()
        self.pp.logout() 
        logging.info("Finished test: test_valid_login")
        
    # Test for invalid login flow using the locked out user account    
    @pytest.mark.login
    def test_invalid_login(self):
        logging.info("Starting test: test_invalid_login")
        username = self.cr.getLockedUser()
        password = self.cr.getPassword()
        self.lp.enterUsername(username)
        self.lp.enterPassword(password)
        self.lp.clickLoginButton()
        errorMessage = self.lp.getLoginErrorMessageText()
        expectedErrorMessage = "Epic sadface: Sorry, this user has been locked out."
        assert errorMessage == expectedErrorMessage
        logging.info("Finished test: test_invalid_login")
