import pytest
import os
import yaml
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from os import path
from yaml import safe_load
from typing import Dict

CURRENT_DIRECTORY = os.path.dirname(__file__)
TEST_DATA = os.path.join(CURRENT_DIRECTORY, "tests", "data_test.yml")

@pytest.fixture
def driver() -> Chrome:
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    chrome_driver = Chrome(options=options)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture(scope="session")
def qa_config() -> Dict:
    with open(path.join(path.dirname(__file__), "qa_config.yml")) as config_file:
        return safe_load(config_file)


@pytest.fixture
def test_data():
    with open(TEST_DATA, 'r') as file:
        data = yaml.safe_load(file)
    return data
