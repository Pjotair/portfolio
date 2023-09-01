import pytest
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from os import path
from yaml import safe_load
from typing import Dict
from selenium import webdriver


@pytest.fixture
def driver() -> Chrome:
    # config = request.config
    options = Options()

    # TODO: fixture to read yml
    # headless = (
    #     False if config.option.disable_headless
    #     else qa_config['test_domains']['headless'])

    # if headless:
    #     options.add_argument("--headless")

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
    with open('tests/data_for_test.json', 'r') as file:
        data = json.load(file)
    return data
