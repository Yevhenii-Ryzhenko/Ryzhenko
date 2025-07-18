import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_log.log", mode="a", encoding="utf-8")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class TestLogger:
    def info(self, msg):
        logger.info(msg)
    def error(self, msg):
        logger.error(msg)
    def warning(self, msg):
        logger.warning(msg)
    def debug(self, msg):
        logger.debug(msg)

@pytest.fixture(autouse=True)
def log_test(request):
    test_name = request.node.name
    logger.info(f"Starting test: {test_name}")
    yield
    rep_call = getattr(request.node, "rep_call", None)
    if rep_call:
        if rep_call.failed:
            logger.error(f"FAILED TEST: {test_name}")
        elif rep_call.passed:
            logger.info(f"PASSED TEST: {test_name}")
        else:
            logger.warning(f"UNKNOWN RESULT: {test_name}")
    else:
        logger.warning(f"NO RESULT FOR TEST: {test_name}")
    logger.info(f"Finished test: {test_name}\n")

def pytest_runtest_makereport(item, call):
    outcome = pytest.TestReport.from_item_and_call(item, call)
    if outcome.when == "call":
        setattr(item, "rep_call", outcome)
    return outcome

@pytest.fixture(scope="class")
def auth_to_cars_app():
    print("Start authorization to cars app...")
    auth_bearer_token = requests.post(url='http://127.0.0.1:8080/auth',
                                      auth=requests.auth.HTTPBasicAuth(username='test_user',
                                                                       password='test_pass')).json()
    return auth_bearer_token

@pytest.fixture
def test_logger():
    return TestLogger()

