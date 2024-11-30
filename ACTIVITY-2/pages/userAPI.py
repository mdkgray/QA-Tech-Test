import urllib3
import logging
from base.baseAPI import BaseAPI
from utils.config_reader import ConfigReader

class UserAPI(BaseAPI):
    instance = None
    
    def __new__(cls, base_url):
        if cls.instance is None:
            cls.instance = super(UserAPI, cls).__new__(cls)
            cls.instance._initialize(base_url)
        return cls.instance
    
    def _initialize(self, base_url):
        super().__init__(base_url)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def createUser(self, user_data):
        """Creates a new user."""
        try:
            endpoint = ConfigReader.getCreateUserEndpoint()
            headers = self.get_header_details()
            response = self.api_POST(endpoint, headers=headers, json=user_data)
            if response:
                logging.info(f"Successfully created user: {response}")
                return response
            else:
                logging.error("Failed to create user")
                return None
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return None
    
    def getUserByUsername(self, username):
        """Retrieves a user by username."""
        try:
            endpoint = ConfigReader.getUserByUsernameEndpoint().format(username=username)
            headers = self.get_header_details()
            response = self.api_GET(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully retrieved user with username {username}: {response}")
                return response
            else:
                logging.error(f"Failed to retrieve user with username {username}")
                return None
        except Exception as e:
            logging.error(f"Error retrieving user with username {username}: {e}")
            return None

    def updateUser(self, username, user_data):
        """Updates an existing user."""
        try:
            endpoint = ConfigReader.getUpdateUserEndpoint().format(username=username)
            headers = self.get_header_details()
            response = self.api_PUT(endpoint, headers=headers, json=user_data)
            if response:
                logging.info(f"Successfully updated user: {response}")
                return response
            else:
                logging.error("Failed to update user")
                return None
        except Exception as e:
            logging.error(f"Error updating user: {e}")
            return None

    def deleteUserByUsername(self, username):
        """Deletes a user by username."""
        try:
            endpoint = ConfigReader.getDeleteUserByUsernameEndpoint().format(username=username)
            headers = self.get_header_details()
            response = self.api_DELETE(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully deleted user with username {username}")
                return response
            else:
                logging.error(f"Failed to delete user with username {username}")
                return None
        except Exception as e:
            logging.error(f"Error deleting user with username {username}: {e}")
            return None

    def loginUser(self, username, password):
        """Logs in a user."""
        try:
            endpoint = ConfigReader.getLoginUserEndpoint()
            headers = self.get_header_details()
            params = {'username': username, 'password': password}
            response = self.api_GET(endpoint, headers=headers, params=params)
            if response:
                logging.info(f"Successfully logged in user: {response}")
                return response
            else:
                logging.error("Failed to log in user")
                return None
        except Exception as e:
            logging.error(f"Error logging in user: {e}")
            return None

    def logoutUser(self):
        """Logs out the current user."""
        try:
            endpoint = ConfigReader.getLogoutUserEndpoint()
            headers = self.get_header_details()
            response = self.api_GET(endpoint, headers=headers)
            if response:
                logging.info("Successfully logged out user")
                return response
            else:
                logging.error("Failed to log out user")
                return None
        except Exception as e:
            logging.error(f"Error logging out user: {e}")
            return None