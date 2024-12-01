# Pet Store REST API Service 

## Objective
The objective of this project is to provide automated testing of the Pet Store REST API Service to ensure that all critical functionalities of the sample server `Petstore server` are reliable. These functionalities include managing pets, store orders and user management work as expected. 

## API endpoints
The following endpoints of this API will be tested:
- `/pet`
- `/store`
- `/user`

## Test Plan overview
Comprehensive test plans for this API service can be found in the `EXERCISE-2.md` of this activity which were written in relation to the [Swagger sample server](https://mandrillapp.com/track/click/30950621/petstore.swagger.io?p=eyJzIjoiWDlESEktZDdPVElkaDRjUHRwZ0NwVGl6SE80IiwidiI6MSwicCI6IntcInVcIjozMDk1MDYyMSxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL3BldHN0b3JlLnN3YWdnZXIuaW9cXFwvXCIsXCJpZFwiOlwiZGIzNzI4YWIwMDIwNGI4MmI4NTRiYjAyNjkzNjhkZDhcIixcInVybF9pZHNcIjpbXCJhNTk4N2FiNjI0ODQ0YTMzODE1MWQzODNkMDI1YjNkYTc5ZmY1ZmE1XCJdfSJ9) and cover the following:
1. Pet:
    - GET, PUT, POST and DELETE requests 
2. Store orders:
    - GET, POST and DELETE requests 
3. User:
    - GET, PUT, POST and DELETE requests 

## Tools and Technologies
- **Python:** Programming language for writing automated tests.
- **Pytest:** Executing automated test cases.
- **Python Requests Library:** To assist in the automation of the REST API. 
- **ConfigParser:** Managing configuration settings.
- **HTML Reports:** Capture and display test executions in HTML format.

## Prerequisites
1. Install Python v3.13.0: [Download Python](https://www.python.org/downloads/)
2. Install Git: [Download Git](https://git-scm.com/downloads)
3. Install Pip: [Download Pip](https://pip.pypa.io/en/stable/installation/)

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

#Navigate to ACTIVITY-2
cd ACTIVITY-2 

#Install project requirements
pip install -r requirements.txt
```

## Run Tests
Run the following commands to execute the tests:

- **Tests related to Pets**
```bash
# Run tests for the Pet endpoint
pytest tests/test_pet.py -v -s --html=reports/petReport.html
```
- **Tests related to Store**
```bash
# Run tests for the Store endpoint
pytest tests/test_store.py -v -s --html=reports/storeReport.html
```
- **Tests related to User**
```bash
# Run tests for the User endpoint
pytest tests/test_user.py -v -s --html=reports/userReport.html
```
- **Run tests using a specific pytest marker**
```bash
# Run tests for the User endpoint
python -m pytest -m {MARKER_NAME}
```
