import pytest
import unittest
import logging
from pages.petAPI import PetAPI
from utils.config_reader import ConfigReader

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.pet
class TestPet(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.pet_api = PetAPI()

    @pytest.mark.addpet
    def test_add_new_pet(self):
        logging.info("Starting test: test_add_new_pet")
        pet_data = {
            "id": 12345,
            "name": "Hank",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://unsplash.com/photos/adorable-white-bulldog-puppy-portrait-fBwMiyEagG"],
            "tags": [{"id": 1, "name": "Cute"}],
            "status": "available"
        }
        response = self.pet_api.addNewPet(pet_data)
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], "Hank")
        self.assertEqual(response['id'], 12345)
        logging.info("Finished test: test_add_new_pet")

    @pytest.mark.getpet
    def test_get_pet_by_id(self):
        logging.info("Starting test: test_get_pet_by_id")
        pet_id = 12345
        response = self.pet_api.getPetById(pet_id)
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], pet_id)
        logging.info("Finished test: test_get_pet_by_id")

    @pytest.mark.updatepet
    def test_update_pet(self):
        logging.info("Starting test: test_update_pet")
        
        # Add a new pet
        pet_data = {
            "id": 54321,
            "name": "Buddy",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://unsplash.com/photos/selective-focus-photography-of-golden-labrador-retriever-pgUbpDLJh3E"],
            "tags": [{"id": 1, "name": "portrait"}],
            "status": "available"
        }
        add_response = self.pet_api.addNewPet(pet_data)
        self.assertIsNotNone(add_response)
        
        # Retrieve the pet by ID
        pet_id = 12345
        get_response = self.pet_api.getPetById(pet_id)
        self.assertIsNotNone(get_response)
        self.assertEqual(get_response['id'], pet_id)
        
        # Update the pet
        updated_pet_data = {
            "id": 54321,
            "name": "Buddy Updated",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://unsplash.com/photos/a-golden-retriever-sitting-on-a-sandy-beach-FTbC150wV8Q"],
            "tags": [{"id": 1, "name": "beach"}],
            "status": "pending"
        }
        update_response = self.pet_api.updatePet(updated_pet_data)
        self.assertIsNotNone(update_response)
        self.assertEqual(update_response['name'], "Buddy Updated")
        logging.info("Finished test: test_update_pet")

    @pytest.mark.deletepet
    def test_delete_pet(self):
        logging.info("Starting test: test_delete_pet")
        
        # Add a new pet
        pet_data = {
            "id": 33212,
            "name": "Tom",
            "category": {"id": 1, "name": "Dogs"},
            "photoUrls": ["https://unsplash.com/photos/long-coated-brown-dog-KZv7w34tluA"],
            "tags": [{"id": 1, "name": "glasses"}],
            "status": "available"
        }
        add_response = self.pet_api.addNewPet(pet_data)
        self.assertIsNotNone(add_response)
        
        # Retrieve the pet by ID
        pet_id = 33212
        get_response = self.pet_api.getPetById(pet_id)
        self.assertIsNotNone(get_response)
        self.assertEqual(get_response['id'], pet_id)
        
        # Delete the pet
        delete_response = self.pet_api.deletePet(pet_id)
        self.assertIsNotNone(delete_response)
        logging.info("Finished test: test_delete_pet")

if __name__ == "__main__":
    unittest.main()