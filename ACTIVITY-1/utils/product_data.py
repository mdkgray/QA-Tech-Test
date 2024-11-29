# utils/product_data.py
def get_product_data():
    return [
        {"name": "Sauce Labs Backpack", "price": "$29.99", "quantity": "1"},
        {"name": "Sauce Labs Bike Light", "price": "$9.99", "quantity": "1"},
        {"name": "Sauce Labs Bolt T-Shirt", "price": "$15.99", "quantity": "1"},
        {"name": "Sauce Labs Fleece Jacket", "price": "$49.99", "quantity": "1"},
        {"name": "Sauce Labs Onesie", "price": "$7.99", "quantity": "1"},
        {"name": "Test.allTheThings() T-Shirt (Red)", "price": "$15.99", "quantity": "1"},
    ]
    
def get_invalid_product_data():
    return [
        {"name": "Lab Source Pack Back"},
        {"name": "Twosie Sauce Labs"},
    ]