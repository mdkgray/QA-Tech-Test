import pytest
import logging
from pages.userAPI import UserAPI
from utils.config_reader import ConfigReader

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.user
class TestUser:
    
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.user_api = UserAPI(self.baseURL)

    # Test to create a new user
    @pytest.mark.createuser
    def test_create_user(self):
        logging.info("Starting test: test_create_user")
        user_data = {
            "id": 1,
            "username": "johndoe",
            "firstName": "John",
            "lastName": "Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "phone": "0000000000",
            "userStatus": 1
        }
        response = self.user_api.createUser(user_data)
        logging.info(f"Create user response: {response}")
        assert response is not None
        assert response['code'] == 200
        assert response['message'] == str(user_data['id'])
        logging.info("Finished test: test_create_user")

    @pytest.mark.getuser
    def test_get_user_by_username(self):
        logging.info("Starting test: test_get_user_by_username")
        username = "johndoe"
        response = self.user_api.getUserByUsername(username)
        logging.info(f"Get user response: {response}")
        assert response is not None
        assert response['username'] == username
        logging.info("Finished test: test_get_user_by_username")

    @pytest.mark.updateuser
    def test_update_user(self):
        logging.info("Starting test: test_update_user")
        
        # Create a new user
        user_data = {
            "id": 2,
            "username": "janedoe",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "janedoe@example.com",
            "password": "password123",
            "phone": "0987654321",
            "userStatus": 1
        }
        create_response = self.user_api.createUser(user_data)
        logging.info(f"Create user response: {create_response}")
        assert create_response is not None
        
        # Update the user
        updated_user_data = {
            "id": 2,
            "username": "janedoe",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "janedoe@example.com",
            "password": "newpassword123",
            "phone": "0987654321",
            "userStatus": 1
        }
        response = self.user_api.updateUser("janedoe", updated_user_data)
        logging.info(f"Update user response: {response}")
        assert response is not None
        assert response['code'] == 200
        assert response['message'] == str(updated_user_data['id'])
        logging.info("Finished test: test_update_user")

    @pytest.mark.deleteuser
    def test_delete_user_by_username(self):
        logging.info("Starting test: test_delete_user_by_username")
        
        # Create a new user
        user_data = {
            "id": 3,
            "username": "janedoe",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "janedoe@example.com",
            "password": "password123",
            "phone": "0987654321",
            "userStatus": 1
        }
        create_response = self.user_api.createUser(user_data)
        logging.info(f"Create user response: {create_response}")
        assert create_response is not None
        
        # Delete the user
        response = self.user_api.deleteUserByUsername("janedoe")
        logging.info(f"Delete user response: {response}")
        assert response is not None
        assert response['code'] == 200
        assert response['message'] == str(user_data['username'])
        logging.info("Finished test: test_delete_user_by_username")

    @pytest.mark.login
    def test_login_user(self):
        logging.info("Starting test: test_login_user")
        username = "johndoe"
        password = "password123"
        response = self.user_api.loginUser(username, password)
        logging.info(f"Login user response: {response}")
        assert response is not None
        assert 'code' in response and response['code'] == 200
        logging.info("Finished test: test_login_user")

    @pytest.mark.logout
    def test_logout_user(self):
        logging.info("Starting test: test_logout_user")
        response = self.user_api.logoutUser()
        logging.info(f"Logout user response: {response}")
        assert response is not None
        assert 'code' in response and response['code'] == 200
        logging.info("Finished test: test_logout_user")