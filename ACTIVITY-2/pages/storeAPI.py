import urllib3
import logging
from base.baseAPI import BaseAPI
from utils.config_reader import ConfigReader

class StoreAPI(BaseAPI):
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(StoreAPI, cls).__new__(cls)
            cls.instance._initialize()
        return cls.instance
    
    def _initialize(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def placeOrder(self, order_data):
        """Places an order in the store."""
        try:
            endpoint = ConfigReader.getPlaceOrderEndpoint()
            headers = self.get_header_details()
            response = self.api_POST(endpoint, headers=headers, json=order_data)
            if response:
                logging.info(f"Successfully placed order: {response}")
                return response
            else:
                logging.error("Failed to place order")
                return None
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return None
    
    def getOrderById(self, order_id):
        """Retrieves an order by its ID."""
        try:
            endpoint = ConfigReader.getOrderByIdEndpoint().format(order_id=order_id)
            headers = self.get_header_details()
            response = self.api_GET(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully retrieved order with ID {order_id}: {response}")
                return response
            else:
                logging.error(f"Failed to retrieve order with ID {order_id}")
                return None
        except Exception as e:
            logging.error(f"Error retrieving order with ID {order_id}: {e}")
            return None

    def deleteOrderById(self, order_id):
        """Deletes an order by its ID."""
        try:
            endpoint = ConfigReader.getDeleteOrderByIdEndpoint().format(order_id=order_id)
            headers = self.get_header_details()
            response = self.api_DELETE(endpoint, headers=headers)
            if response:
                logging.info(f"Successfully deleted order with ID {order_id}")
                return response
            else:
                logging.error(f"Failed to delete order with ID {order_id}")
                return None
        except Exception as e:
            logging.error(f"Error deleting order with ID {order_id}: {e}")
            return None