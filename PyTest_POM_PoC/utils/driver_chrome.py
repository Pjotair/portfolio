from selenium import webdriver

def get_driver(driver_chrome):
    if driver_chrome == "chrome":
        return webdriver.Chrome()
