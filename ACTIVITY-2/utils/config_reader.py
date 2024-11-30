import configparser
import os

configReader = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
configReader.read(config_path)

class ConfigReader:
    @staticmethod
    def getBaseURL():
        url = configReader.get('api_info', 'baseURL')
        return url
    
    @staticmethod
    def getContentType():
        content_type = configReader.get('api_info', 'contentType')
        return content_type
    
    @staticmethod
    def getAPIKey():
        api_key = configReader.get('api_info', 'apiKey')
        return api_key
    
    @staticmethod
    def getAddNewPetEndpoint():
        endpoint = configReader.get('pet', 'addNewPet')
        return endpoint
    
    @staticmethod
    def getUpdatePetEndpoint():
        endpoint = configReader.get('pet', 'updateExistingPet')
        return endpoint
    
    @staticmethod
    def getPetByIdEndpoint():
        endpoint = configReader.get('pet', 'getPetByID')
        return endpoint
    
    @staticmethod
    def getPetByStatusEndpoint():
        endpoint = configReader.get('pet', 'getPetByStatus')
        return endpoint
    
    @staticmethod
    def getUpdatePetByIdEndpoint():
        endpoint = configReader.get('pet', 'updatePetById')
        return endpoint
    
    @staticmethod
    def getDeletePetByIdEndpoint():
        endpoint = configReader.get('pet', 'deletePetById')
        return endpoint
    
    @staticmethod
    def getOrderByIdEndpoint():
        endpoint = configReader.get('store', 'getOrderById')
        return endpoint
    
    @staticmethod
    def getPlaceOrderEndpoint():
        endpoint = configReader.get('store', 'placeOrder')
        return endpoint
    
    @staticmethod
    def getDeleteOrderByIdEndpoint():
        endpoint = configReader.get('store', 'deleteOrderById')
        return endpoint
    
    @staticmethod
    def getLoginUserEndpoint():
        endpoint = configReader.get('user', 'loginUser')
        return endpoint
    
    @staticmethod
    def getLogoutUserEndpoint():
        endpoint = configReader.get('user', 'logoutUser')
        return endpoint
    
    @staticmethod
    def getCreateUserEndpoint():
        endpoint = configReader.get('user', 'createUser')
        return endpoint
    
    @staticmethod
    def getUserByUsernameEndpoint():
        endpoint = configReader.get('user', 'getUserByUsername')
        return endpoint
    
    @staticmethod
    def getDeleteUserByUsernameEndpoint():
        endpoint = configReader.get('user', 'deleteUserByUsername')
        return endpoint
    