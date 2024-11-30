import json 
import os
import logging
import requests
from utils.config_reader import ConfigReader

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_header_details(self):
        content_type = ConfigReader.getContentType()
        api_key = ConfigReader.getAPIKey()
        headers = {
            'Content-Type': f"{content_type}",
            'api_key': f"{api_key}"
        }
        return headers
    
    def api_GET(self, endpoint, headers=None, params=None):
        """Makes a GET request to the specified endpoint."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            if response.status_code == 200:
                logging.info(f"GET request to {url} successful")
                return response.json()  # Return the parsed JSON response
            else:
                logging.error(f"GET request to {url} returned status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error during GET request to {url}: {e}")
            return None

    def api_POST(self, endpoint, headers=None, data=None, json=None):
        """Makes a POST request to the specified endpoint."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.post(url, headers=headers, data=data, json=json)
            response.raise_for_status()  # Raise an exception for HTTP errors
            if response.status_code == 200:
                logging.info(f"POST request to {url} successful")
                return response.json()  # Return the parsed JSON response
            else:
                logging.error(f"POST request to {url} returned status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error during POST request to {url}: {e}")
            return None

    def api_PUT(self, endpoint, headers=None, data=None, json=None):
        """Makes a PUT request to the specified endpoint."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.put(url, headers=headers, data=data, json=json)
            response.raise_for_status()  # Raise an exception for HTTP errors
            if response.status_code == 200:
                logging.info(f"PUT request to {url} successful")
                return response.json()  # Return the parsed JSON response
            else:
                logging.error(f"PUT request to {url} returned status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error during PUT request to {url}: {e}")
            return None

    def api_DELETE(self, endpoint, headers=None, params=None):
        """Makes a DELETE request to the specified endpoint."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.delete(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            if response.status_code == 200:
                logging.info(f"DELETE request to {url} successful")
                return response.json()  # Return the parsed JSON response
            else:
                logging.error(f"DELETE request to {url} returned status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            logging.error(f"Error during DELETE request to {url}: {e}")
            return None