import urllib3
import logging
from base.baseAPI import BaseAPI
from utils.config_reader import ConfigReader

class PetAPI(BaseAPI):
    instance = None
    
    def __new__(cls, base_url):
        if cls.instance is None:
            cls.instance = super(PetAPI, cls).__new__(cls)
            cls.instance._initialize(base_url)
        return cls.instance
    
    def _initialize(self, base_url):
        super().__init__(base_url)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def addNewPet(self, pet_data):
        """Adds a new pet to the store."""
        try:
            endpoint = ConfigReader.getAddNewPetEndpoint()
            headers = self.get_header_details()
            response = self.api_POST(endpoint, headers=headers, json=pet_data)
            if response:
                logging.info(f"Successfully added new pet: {response}")
                return response
            else:
                logging.error("Failed to add new pet")
                return None
        except Exception as e:
            logging.error(f"Error adding new pet: {e}")
            return None
    
    def getPetById(self, pet_id):
        """Retrieves a pet by its ID."""
        try:
            endpoint = ConfigReader.getPetByIdEndpoint().format(pet_id=pet_id)
            headers = self.get_header_details()
            response = self.api_GET(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully retrieved pet with ID {pet_id}: {response}")
                return response
            else:
                logging.error(f"Failed to retrieve pet with ID {pet_id}")
                return None
        except Exception as e:
            logging.error(f"Error retrieving pet with ID {pet_id}: {e}")
            return None

    def updatePet(self, pet_data):
        """Updates an existing pet in the store."""
        try:
            endpoint = ConfigReader.getUpdatePetEndpoint()
            headers = self.get_header_details()
            response = self.api_PUT(endpoint, headers=headers, json=pet_data)
            if response:
                logging.info(f"Successfully updated pet: {response}")
                return response
            else:
                logging.error("Failed to update pet")
                return None
        except Exception as e:
            logging.error(f"Error updating pet: {e}")
            return None

    def deletePet(self, pet_id):
        """Deletes a pet by its ID."""
        try:
            endpoint = ConfigReader.getDeletePetByIdEndpoint().format(pet_id=pet_id)
            headers = self.get_header_details()
            response = self.api_DELETE(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully deleted pet with ID {pet_id}")
                return response
            else:
                logging.error(f"Failed to delete pet with ID {pet_id}")
                return None
        except Exception as e:
            logging.error(f"Error deleting pet with ID {pet_id}: {e}")
            return None