import pytest
import logging
from pages.storeAPI import StoreAPI
from utils.config_reader import ConfigReader

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.store
class TestStore:
   
    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.baseURL = ConfigReader.getBaseURL()
        self.store_api = StoreAPI(self.baseURL)

    @pytest.mark.placeorder
    def test_place_order(self):
        logging.info("Starting test: test_place_order")
        order_data = {
            "id": 1,
            "petId": 12345,
            "quantity": 1,
            "shipDate": "2024-11-28T12:34:56.789Z",
            "status": "placed",
            "complete": True
        }
        response = self.store_api.placeOrder(order_data)
        assert response is not None
        assert response['id'] == 1
        logging.info("Finished test: test_place_order")

    @pytest.mark.getorder
    def test_get_order_by_id(self):
        logging.info("Starting test: test_get_order_by_id")
        order_id = 1
        response = self.store_api.getOrderById(order_id)
        assert response is not None
        assert response['id'] == order_id
        logging.info("Finished test: test_get_order_by_id")

    @pytest.mark.deleteorder
    def test_delete_order_by_id(self):
        logging.info("Starting test: test_delete_order_by_id")
        
        # Place a new order
        order_data = {
            "id": 2,
            "petId": 54321,
            "quantity": 1,
            "shipDate": "2024-11-29T12:34:56.789Z",
            "status": "placed",
            "complete": True
        }
        place_response = self.store_api.placeOrder(order_data)
        assert place_response is not None
        
        # Retrieve the order by ID
        order_id = 2
        get_response = self.store_api.getOrderById(order_id)
        assert get_response is not None
        assert get_response['id'] == order_id
        
        # Delete the order
        delete_response = self.store_api.deleteOrderById(order_id)
        assert delete_response is not None
        logging.info("Finished test: test_delete_order_by_id")