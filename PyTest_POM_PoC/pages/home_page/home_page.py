from selenium.webdriver.common.by import By
from ..base_page import BasePage

class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, '[id="module-pytest"] h1')

    def page_header(self) -> str:
        page_header = self.wait_for_element(self.HEADER)
        return page_header.text
