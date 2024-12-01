import pytest
from base.webdriverfactory import WebDriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture()
def setUp():
  print("Running method level setUp")
  yield
  print("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    browser = request.config.getoption("--browser")
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.useWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
