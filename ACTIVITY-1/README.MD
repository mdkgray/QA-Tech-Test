# Swag Labs E-Commerce Website


## Objective

The objective of this project is to provide automated testing of the Swag Labs E-Commerce website using Selenium WebDriver and Python in order to ensure that all critical flows/features are reliable. Through this automation, any issues which impact the way the user interacts with the application can be identified.  

## Scope
The following core functionalities of the E-commerce application will be tested:

### Login: 
- Verify user authentication and error handling for incorrect credentials.
### Product Inventory - Grid and Detailed Views:
- Verify product details and ensure data is consistent across listings.
### Cart:
- Test adding, removing, and updating items in the cart.
### Checkout: 
- Validate the checkout workflow, payment options, and form validation.

## Tools and Technologies
- **Python:** Programming language for writing automated tests.
- **Pytest:** Executing automated test cases.
- **Selenium WebDriver:** Automating web browser interactions.
- **ConfigParser:** Managing configuration settings.
- **HTML Reports:** Capture and display test executions in HTML format.

## Prerequisites
## Prerequisites
1. Install Python v3.13.0: [Download Python](https://www.python.org/downloads/)
2. Install Git: [Download Git](https://git-scm.com/downloads)
4. Install Pip: 

## Getting Started
Once the prerequisites are met, follow the bellow commands:

```bash 
#Clone the repo
git clone git@github.com:mdkgray/QA-Tech-Test.git

#Ensure you have the latest code
git fetch
git pull origin

#Navigate to the project 
cd QA-TECH-TEST

#Create and activate a new virtual environment 
python3 -m venv {{NAME_OF_YOUR_VENV}}
source {{NAME_OF_YOUR_VENV}}/bin/activate 

#Install project requirements
pip install -r requirements.txt
```

## Run Tests

<!-- TODO: Add scripts to run tests -->